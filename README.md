# Azure Function Testes

## Descrição

Esta Azure Function foi criada para acessar um segredo armazenado no Azure Key Vault. A função é acionada por uma requisição HTTP e retorna o valor do segredo especificado. Ela utiliza a biblioteca `azure-identity` para autenticação e `azure-keyvault-secrets` para acessar o Key Vault.

### Funcionalidades

- **Autenticação:** Utiliza `DefaultAzureCredential` para autenticação automática com o Azure.
- **Acesso ao Key Vault:** Recupera o valor de um segredo armazenado no Key Vault.
- **Resposta HTTP:** Retorna o valor do segredo em uma resposta HTTP.

### Estrutura do Projeto

- `__init__.py`: Contém a lógica principal da Azure Function.
- `function.json`: Define as configurações de binding da função.
- `host.json`: Configurações do host para a Azure Function.
- `local.settings.json`: Configurações locais para desenvolvimento.
- `requirements.txt`: Lista de dependências do projeto.

### Como Executar

1. **Instalar Dependências:**
   ```bash
   pip install -r requirements.txt
