# Sistema de Login em Python com MySQL e PySimpleGUI 🐍🔐📲

Este é um projeto de sistema de login em Python que utiliza o banco de dados MySQL para autenticação e a biblioteca PySimpleGUI para criar uma interface gráfica interativa. Abaixo, você encontrará uma descrição detalhada das principais funcionalidades e estrutura do código.

## Funcionalidades Principais:

### Autenticação de Usuários:
- **Banco de Dados MySQL:** O projeto utiliza o MySQL como sistema de gerenciamento de banco de dados para armazenar e verificar as credenciais dos usuários.
  
### Interface Gráfica com PySimpleGUI:
- **Layout Atrativo:** Utiliza a biblioteca PySimpleGUI para criar uma interface gráfica atraente e de fácil utilização.
- **Campos de Entrada:** Permite que os usuários insiram seu e-mail e senha para efetuar login.
- **Botões de Ação:** Inclui botões para logar e cadastrar-se, proporcionando uma navegação intuitiva.

### Feedback Visual:
- **Mensagens de Feedback:** Exibe mensagens de feedback na interface, informando sobre o sucesso ou falha no login.

### Estrutura do Código:

- **`conectar.py`:** Contém a função `validar_db` para verificar as credenciais do usuário no banco de dados MySQL.
  
- **`main.py`:** Implementa a interface gráfica usando PySimpleGUI e integra a função `validar_db` para autenticação.

## Como Executar o Projeto:

1. **Configuração do Banco de Dados:**
   - Certifique-se de ter um servidor MySQL em execução localmente.
   - Crie um banco de dados chamado `users_db` e uma tabela `usuarios` com as colunas `id`, `nome`, `email` e `senha`.

2. **Instalação das Dependências:**
   - Instale as dependências necessárias utilizando `pip install PySimpleGUI mysql-connector-python`.

3. **Execução:**
   - Execute o arquivo `main.py` para iniciar a interface gráfica do sistema de login.

Este projeto proporciona uma implementação prática da autenticação de usuários em Python, integrando um banco de dados MySQL e uma interface gráfica intuitiva com PySimpleGUI.
