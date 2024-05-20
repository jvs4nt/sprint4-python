# Sistema de Gerenciamento de Cadastros

Este é um sistema de gerenciamento de cadastros desenvolvido em Python, que interage com um banco de dados Oracle. O sistema permite o cadastro, alteração, exclusão e consulta de clientes, funcionários e chatbots. O sistema conta com dois arquivos, um para realizar operações no banco de dados, e uma API para ser consumida em um projeto React disponibilizado no final da documentação.

## Pré-requisitos

- Python 3.x
- Oracle SQL Developer
- Módulo `oracledb` para Python (MAIN)
- Módulo `flask` para Python (API)
- Módulo `flask-cors` para Python (API)
- Pandas
- JSON

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu_usuario/sistema-gerenciamento-cadastros.git
   ```

2. Instale as dependências:

   ```bash
   pip install pandas oracledb
   pip install flask
   pip install flask-cors
   ```

## Configuração do Banco de Dados

1. Execute as instruções SQL fornecidas no arquivo `tabelas.sql` no Oracle SQL Developer para criar as tabelas necessárias no banco de dados.

## Uso

1. Execute o programa principal:

   ```bash
   python main.py
   ```
   --
   ```bash
   python api.py
   ```

2. No arquivo main.py, selecione uma das opções do menu para realizar operações de cadastro, alteração, exclusão ou consulta.

## Funcionalidades

- Cadastro de clientes
- Cadastro de funcionários
- Cadastro de chatbots
- Consultas por nome de cliente ou cargo de funcionário
- Exportação de dados para JSON

## Estrutura do Banco de Dados

### Tabela `clientes`

| Coluna      | Tipo      | Descrição               |
|-------------|-----------|-------------------------|
| id_clie     | NUMBER    | Identificador (PK)      |
| nome_clie   | VARCHAR2  | Nome do cliente         |
| email_clie  | VARCHAR2  | Email do cliente        |
| cpf_cnpj    | VARCHAR2  | CPF ou CNPJ do cliente |

### Tabela `funcionarios`

| Coluna      | Tipo      | Descrição               |
|-------------|-----------|-------------------------|
| id_fun      | NUMBER    | Identificador (PK)      |
| nome_fun    | VARCHAR2  | Nome do funcionário     |
| cargo_fun   | VARCHAR2  | Cargo do funcionário    |
| email_fun   | VARCHAR2  | Email do funcionário    |

### Tabela `chatbots`

| Coluna          | Tipo      | Descrição                       |
|-----------------|-----------|---------------------------------|
| id_chatbot      | NUMBER    | Identificador (PK)              |
| data_inicio_cb  | DATE      | Data de início do chatbot       |
| api_token       | VARCHAR2  | Token de API do chatbot         |

3. No arquivo api.py, visualize o retorno da api utilizando o endpoint "/clientes". Sinta-se à vontade para consumir a API para testes.

Exemplo do retorno:
{
   "CPF_CNPJ":"0192019201",
   "EMAIL_CLIE":"willian@willian",
   "ID_CLIE":26,"NOME_CLIE":"willian"
},
{
      "CPF_CNPJ":"12801822342",
      "EMAIL_CLIE":"ryan@teste",
      "ID_CLIE":30,
      "NOME_CLIE":"ryan"
},
{
   "CPF_CNPJ":"001",
   "EMAIL_CLIE":
   "joao@teste",
   "ID_CLIE":10,
   "NOME_CLIE":"joao edit teste"
}

## Testes disponíveis:

API (Replit): https://replit.com/@joaovit342/APISPRINT4PYTHON#main.py
Website (API foi utilizada para gerar a tabela na aba "Clientes"): https://salesforce-sprint4.vercel.app/ 

## Contribuição

Contribuições são bem-vindas! Para sugestões, correções ou novas funcionalidades, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
