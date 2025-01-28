import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP-triggered function that retrieves a secret from Azure Key Vault.
    
    Parameters:
        req (func.HttpRequest): The HTTP request object
        
    Returns:
        func.HttpResponse: The HTTP response containing the secret value or error message
    """
    logging.info('Python HTTP trigger function processed a request.')

    # URL do Key Vault
    key_vault_name = "engdadoskey2"
    KVUri = f"https://{key_vault_name}.vault.azure.net"

    # Nome do segredo
    secret_name = req.params.get('secret_name', 'db-password')

    try:
        # Autenticar e criar um cliente
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)

        # Recuperar o segredo
        retrieved_secret = client.get_secret(secret_name)

        # Exibir valor do segredo
        return func.HttpResponse(f"Secret value: {retrieved_secret.value}")

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)