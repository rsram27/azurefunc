from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# URL do Key Vault
key_vault_name = "engdadoskey2"
KVUri = f"https://{key_vault_name}.vault.azure.net"

# Nome do segredo
secret_name = "db-server"

# Autenticar e criar um cliente
# Esse metodo é usado para autenticar com a identidade do sistema
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

# Recuperar o segredo
retrieved_secret = client.get_secret(secret_name)

# Exibir valor do segredo
print(f"Valor do segredo '{secret_name}': {retrieved_secret}")