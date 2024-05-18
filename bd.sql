-- Tabela de Clientes
CREATE TABLE clientes (
    id_clie NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_clie VARCHAR2(100) NOT NULL,
    email_clie VARCHAR2(100) NOT NULL,
    cpf_cnpj VARCHAR2(14) NOT NULL
);

-- Tabela de Funcionários
CREATE TABLE funcionarios (
    id_fun NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_fun VARCHAR2(100) NOT NULL,
    cargo_fun VARCHAR2(100),
    email_fun VARCHAR2(100)
);

-- Tabela de Chatbots
CREATE TABLE chatbots (
    id_chatbot NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    data_inicio_cb DATE,
    api_token VARCHAR2(100)
);
