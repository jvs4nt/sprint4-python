import oracledb
import pandas as pd
import json

def main():
    conexao, inst_SQL, conn = conecta_BD()
    opc = 0
    while opc != 6 and conexao:
        print("1 - Cadastro de clientes")
        print("2 - Cadastro de funcionários")
        print("3 - Cadastro de chatbots")
        print("4 - Consultas")
        print("5 - Exportar dados para JSON")
        print("6 - Sair")

        opc = int(input("Digite a opção desejada (1-6): "))

        if opc == 1:
            cadastro_clientes(inst_SQL, conn)
        elif opc == 2:
            cadastro_funcionarios(inst_SQL, conn)
        elif opc == 3:
            cadastro_chatbots(inst_SQL, conn)
        elif opc == 4:
            consultas(inst_SQL)
        elif opc == 5:
            exportar_para_json(inst_SQL)
        elif opc == 6:
            print("Saindo...")

def cadastro_clientes(inst_SQL, conn):
    opc_clie = 0
    while opc_clie != 4:
        print("1 - Inserção")
        print("2 - Alteração")
        print("3 - Exclusão")
        print("4 - Voltar")
        opc_clie = int(input("Digite a opção desejada (1-4): "))

        if opc_clie == 1:  # Inserção
            try:
                id_clie = input("ID do cliente: ")
                nome_clie = input("Nome do cliente: ")
                email_clie = input("Email do cliente: ")
                cpf_cnpj = input("CPF ou CNPJ do cliente: ")
                str_insert = f"""INSERT INTO clientes (id_clie, nome_clie, email_clie, cpf_cnpj) VALUES ('{id_clie}', '{nome_clie}', '{email_clie}', '{cpf_cnpj}')"""
                executar_query(inst_SQL, conn, str_insert)
            except Exception as e:
                print("Erro: ", e)

        elif opc_clie == 2:  # Alteração
            try:
                id_clie = input("ID do cliente a ser alterado: ")
                novo_nome = input("Novo nome do cliente: ")
                novo_email = input("Novo email do cliente: ")
                novo_cpf_cnpj = input("Novo CPF ou CNPJ do cliente: ")
                str_update = f"""UPDATE clientes SET nome_clie='{novo_nome}', email_clie='{novo_email}', cpf_cnpj='{novo_cpf_cnpj}' WHERE id_clie='{id_clie}'"""
                executar_query(inst_SQL, conn, str_update)
            except Exception as e:
                print("Erro: ", e)

        elif opc_clie == 3:  # Exclusão
            try:
                id_clie = input("ID do cliente a ser excluído: ")
                str_delete = f"""DELETE FROM clientes WHERE id_clie='{id_clie}'"""
                executar_query(inst_SQL, conn, str_delete)
            except Exception as e:
                print("Erro: ", e)

def cadastro_funcionarios(inst_SQL, conn):
    opc_fun = 0
    while opc_fun != 4:
        print("1 - Inserção")
        print("2 - Alteração")
        print("3 - Exclusão")
        print("4 - Voltar")
        opc_fun = int(input("Digite a opção desejada (1-4): "))

        if opc_fun == 1:  # Inserção
            try:
                id_fun = input("ID do funcionário: ")
                nome_fun = input("Nome do funcionário: ")
                cargo_fun = input("Cargo do funcionário: ")
                email_fun = input("Email do funcionário: ")
                str_insert = f"""INSERT INTO funcionarios (id_fun, nome_fun, cargo_fun, email_fun) VALUES ('{id_fun}', '{nome_fun}', '{cargo_fun}', '{email_fun}')"""
                executar_query(inst_SQL, conn, str_insert)
            except Exception as e:
                print("Erro: ", e)

        elif opc_fun == 2:  # Alteração
            try:
                id_fun = input("ID do funcionário a ser alterado: ")
                novo_nome = input("Novo nome do funcionário: ")
                novo_cargo = input("Novo cargo do funcionário: ")
                novo_email = input("Novo email do funcionário: ")
                str_update = f"""UPDATE funcionarios SET nome_fun='{novo_nome}', cargo_fun='{novo_cargo}', email_fun='{novo_email}' WHERE id_fun='{id_fun}'"""
                executar_query(inst_SQL, conn, str_update)
            except Exception as e:
                print("Erro: ", e)

        elif opc_fun == 3:  # Exclusão
            try:
                id_fun = input("ID do funcionário a ser excluído: ")
                str_delete = f"""DELETE FROM funcionarios WHERE id_fun='{id_fun}'"""
                executar_query(inst_SQL, conn, str_delete)
            except Exception as e:
                print("Erro: ", e)

def cadastro_chatbots(inst_SQL, conn):
    opc_cb = 0
    while opc_cb != 4:
        print("1 - Inserção")
        print("2 - Alteração")
        print("3 - Exclusão")
        print("4 - Voltar")
        opc_cb = int(input("Digite a opção desejada (1-4): "))

        if opc_cb == 1:  # Inserção
            try:
                id_chatbot = input("ID do chatbot: ")
                data_inicio_cb = input("Data de início do chatbot (DD/MM/YYYY): ")
                api_token = input("API token: ")
                str_insert = f"""INSERT INTO chatbots (id_chatbot, data_inicio_cb, api_token) VALUES ('{id_chatbot}', TO_DATE('{data_inicio_cb}', 'DD/MM/YYYY'), '{api_token}')"""
                executar_query(inst_SQL, conn, str_insert)
            except Exception as e:
                print("Erro: ", e)

        elif opc_cb == 2:  # Alteração
            try:
                id_chatbot = input("ID do chatbot a ser alterado: ")
                nova_data_inicio = input("Nova data de início do chatbot (DD/MM/YYYY): ")
                novo_api_token = input("Novo API token: ")
                str_update = f"""UPDATE chatbots SET data_inicio_cb=TO_DATE('{nova_data_inicio}', 'DD/MM/YYYY'), api_token='{novo_api_token}' WHERE id_chatbot='{id_chatbot}'"""
                executar_query(inst_SQL, conn, str_update)
            except Exception as e:
                print("Erro: ", e)

        elif opc_cb == 3:  # Exclusão
            try:
                id_chatbot = input("ID do chatbot a ser excluído: ")
                str_delete = f"""DELETE FROM chatbots WHERE id_chatbot='{id_chatbot}'"""
                executar_query(inst_SQL, conn, str_delete)
            except Exception as e:
                print("Erro: ", e)

def consultas(inst_SQL):
    resp = 1
    while resp != 0:
        print("1 - Consultar clientes por nome")
        print("2 - Consultar funcionários por cargo")
        print("3 - Voltar")
        opc_sub = int(input("Digite a opção desejada (1-3): "))

        if opc_sub == 1:
            try:
                nome_clie = input("Digite o nome do cliente a ser buscado: ")
                str_consulta = f"SELECT * FROM clientes WHERE nome_clie LIKE '%{nome_clie}%'"
                consulta_tabela(inst_SQL, str_consulta, ['ID', 'Nome', 'Email', 'CPF_CNPJ'])
            except Exception as e:
                print("Erro: ", e)

        elif opc_sub == 2:
            try:
                cargo_fun = input("Digite o cargo do funcionário a ser buscado: ")
                str_consulta = f"SELECT * FROM funcionarios WHERE cargo_fun LIKE '%{cargo_fun}%'"
                consulta_tabela(inst_SQL, str_consulta, ['ID', 'Nome', 'Cargo', 'Email'])
            except Exception as e:
                print("Erro: ", e)

        elif opc_sub == 3:
            resp = 0

def consulta_tabela(inst_SQL, str_consulta, colunas, gera_txt=False):
    try:
        inst_SQL.execute(str_consulta)
        dados = inst_SQL.fetchall()
        df = pd.DataFrame.from_records(dados, columns=colunas)
        if df.empty:
            print("Não há registros com esses critérios.")
        else:
            print(df)
            if gera_txt:
                texto = df.to_string()
                nome_arq = input("Digite o nome do arquivo texto a ser gerado: ")
                with open(nome_arq, "w", encoding="utf-8") as arq:
                    arq.write(texto)
                print("Arquivo gerado com sucesso!")
    except Exception as e:
        print("Erro: ", e)

def exportar_para_json(inst_SQL):
    try:
        inst_SQL.execute("SELECT * FROM clientes")
        clientes = inst_SQL.fetchall()

        inst_SQL.execute("SELECT * FROM funcionarios")
        funcionarios = inst_SQL.fetchall()

        inst_SQL.execute("SELECT * FROM chatbots")
        chatbots = inst_SQL.fetchall()

        data = {
            "clientes": [dict(zip([key[0] for key in inst_SQL.description], row)) for row in clientes],
            "funcionarios": [dict(zip([key[0] for key in inst_SQL.description], row)) for row in funcionarios
],
            "chatbots": [dict(zip([key[0] for key in inst_SQL.description], row)) for row in chatbots]
        }

        # Exportar para arquivo JSON
        with open("dados.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        print("Dados exportados para 'dados.json' com sucesso!")
    except Exception as e:
        print("Erro: ", e)

def conecta_BD():
    try:
        dnStr = oracledb.makedsn("oracle.fiap.com.br", "1521", "ORCL")
        conn = oracledb.connect(user="RM552671", password="051204", dsn=dnStr)
        inst_SQL = conn.cursor()
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        inst_SQL = None
        conn = None
    else:
        print("Conexão bem-sucedida ao banco de dados.")
    return conn is not None, inst_SQL, conn

def executar_query(inst_SQL, conn, query):
    try:
        inst_SQL.execute(query)
        conn.commit()
        print("Operação realizada com sucesso.")
    except Exception as e:
        print("Erro ao executar a query:", e)

if __name__ == "__main__":
    main()
