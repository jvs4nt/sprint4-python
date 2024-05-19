drop table clientes cascade constraints;
drop table funcionarios cascade constraints;
drop table chatbots cascade constraints;

-- Tabela de Clientes
CREATE TABLE clientes (
    id_clie NUMBER PRIMARY KEY,
    nome_clie VARCHAR2(100) NOT NULL,
    email_clie VARCHAR2(100) NOT NULL,
    cpf_cnpj VARCHAR2(14) NOT NULL
);

-- Tabela de Funcionários
CREATE TABLE funcionarios (
    id_fun NUMBER PRIMARY KEY,
    nome_fun VARCHAR2(100) NOT NULL,
    cargo_fun VARCHAR2(100),
    email_fun VARCHAR2(100)
);

-- Tabela de Chatbots
CREATE TABLE chatbots (
    id_chatbot NUMBER PRIMARY KEY,
    data_inicio_cb DATE,
    api_token VARCHAR2(100)
);

