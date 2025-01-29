import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Função acionada por HTTP que recupera um segredo do Azure Key Vault.
    
    Parâmetros:
        req (func.HttpRequest): O objeto de requisição HTTP
        
    Retorna:
        func.HttpResponse: A resposta HTTP contendo o valor do segredo ou mensagem de erro
    """
    logging.info('Função Python HTTP trigger processou uma requisição.')

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
        if retrieved_secret and retrieved_secret.value:
            return func.HttpResponse(
                body=f"Valor do segredo '{secret_name}': {retrieved_secret.value}",
                status_code=200,
                mimetype="text/plain"
            )
        else:
            return func.HttpResponse(
                body=f"Segredo '{secret_name}' não encontrado ou vazio",
                status_code=404,
                mimetype="text/plain"
            )

    except AzureError as e:
        erro_mensagem = f"Erro ao acessar o Key Vault: {str(e)}"
        logging.error(erro_mensagem)
        return func.HttpResponse(
            body=erro_mensagem,
            status_code=500,
            mimetype="text/plain"
        )
    except Exception as e:
        erro_mensagem = f"Erro inesperado: {str(e)}"
        logging.error(erro_mensagem)
        return func.HttpResponse(
            body=erro_mensagem,
            status_code=500,
            mimetype="text/plain"
        )