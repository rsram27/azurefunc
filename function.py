from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError

def get_secret(secret_name: str = "db-server") -> str:
    """
    Recupera um segredo do Azure Key Vault
    """
    try:
        # URL do Key Vault
        key_vault_name = "engdadoskey2"
        KVUri = f"https://{key_vault_name}.vault.azure.net"

        # Autenticar e criar um cliente
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)

        # Recuperar o segredo
        retrieved_secret = client.get_secret(secret_name)
        return retrieved_secret.value

    except AzureError as e:
        print(f"Erro ao acessar o Key Vault: {e}")
        return None

def main():
    secret = get_secret()
    if secret:
        print(f"Valor do segredo recuperado com sucesso: {secret}")
    else:
        print("Falha ao recuperar o segredo")

if __name__ == "__main__":
    main()