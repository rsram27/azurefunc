import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # URL do Key Vault
    key_vault_name = "engdadoskey2"
    KVUri = f"https://{key_vault_name}.vault.azure.net"

    # Nome do segredo
    secret_name = "db-name"

    try:
        # Autenticar e criar um cliente
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)

        # Recuperar o segredo
        retrieved_secret = client.get_secret(secret_name)

        # Exibir valor do segredo
        if retrieved_secret.value:
            return func.HttpResponse(f"Valor do segredo '{secret_name}': {retrieved_secret.value}")
        else:
            return func.HttpResponse(f"Segredo '{secret_name}' está vazio", status_code=404)

    except AzureError as e:
        logging.error(f"Ocorreu um erro ao acessar o Key Vault: {e}")
        return func.HttpResponse(f"Ocorreu um erro ao acessar o Key Vault: {e}", status_code=500)