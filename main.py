import json

clientes = []
funcionarios = []
chatbots = []

def main():
    menu_principal()

def criar_cliente():
    try:
        id_clie = input("ID do cliente: ")
        nome_clie = input("Nome do cliente: ")
        email_clie = input("Email do cliente: ")
        cpf_cnpj = input("CPF ou CNPJ do cliente: ")
        clientes.append({"id_clie": id_clie, "nome_clie": nome_clie, "email_clie": email_clie, "cpf_cnpj": cpf_cnpj})
        print("Cliente criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar cliente: {e}")

def listar_clientes():
    for cliente in clientes:
        print(cliente)

def atualizar_cliente():
    try:
        id_clie = input("ID do cliente a ser atualizado: ")
        for cliente in clientes:
            if cliente["id_clie"] == id_clie:
                cliente["nome_clie"] = input("Novo nome do cliente: ")
                cliente["email_clie"] = input("Novo email do cliente: ")
                cliente["cpf_cnpj"] = input("Novo CPF ou CNPJ do cliente: ")
                print("Cliente atualizado com sucesso.")
                return
        print("Cliente não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar cliente: {e}")

def deletar_cliente():
    try:
        id_clie = input("ID do cliente a ser deletado: ")
        for cliente in clientes:
            if cliente["id_clie"] == id_clie:
                clientes.remove(cliente)
                print("Cliente deletado com sucesso.")
                return
        print("Cliente não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar cliente: {e}")

def criar_funcionario():
    try:
        id_fun = input("ID do funcionário: ")
        nome_fun = input("Nome do funcionário: ")
        cargo_fun = input("Cargo do funcionário: ")
        email_fun = input("Email do funcionário: ")
        funcionarios.append({"id_fun": id_fun, "nome_fun": nome_fun, "cargo_fun": cargo_fun, "email_fun": email_fun})
        print("Funcionário criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar funcionário: {e}")

def listar_funcionarios():
    for funcionario in funcionarios:
        print(funcionario)

def atualizar_funcionario():
    try:
        id_fun = input("ID do funcionário a ser atualizado: ")
        for funcionario in funcionarios:
            if funcionario["id_fun"] == id_fun:
                funcionario["nome_fun"] = input("Novo nome do funcionário: ")
                funcionario["cargo_fun"] = input("Novo cargo do funcionário: ")
                funcionario["email_fun"] = input("Novo email do funcionário: ")
                print("Funcionário atualizado com sucesso.")
                return
        print("Funcionário não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar funcionário: {e}")

def deletar_funcionario():
    try:
        id_fun = input("ID do funcionário a ser deletado: ")
        for funcionario in funcionarios:
            if funcionario["id_fun"] == id_fun:
                funcionarios.remove(funcionario)
                print("Funcionário deletado com sucesso.")
                return
        print("Funcionário não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar funcionário: {e}")

def criar_chatbot():
    try:
        id_chatbot = input("ID do chatbot: ")
        data_inicio_cb = input("Data de início de funcionamento do chatbot(DD/MM/YYY): ")
        api_token = input("API token do chatbot: ")
        chatbots.append({"id_chatbot": id_chatbot, "data_inicio_cb": data_inicio_cb, "api_token": api_token})
        print("Chatbot criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar chatbot: {e}")

def listar_chatbots():
    for chatbot in chatbots:
        print(chatbot)

def atualizar_chatbot():
    try:
        id_chatbot = input("ID do chatbot a ser atualizado: ")
        for chatbot in chatbots:
            if chatbot["id_chatbot"] == id_chatbot:
                chatbot["data_inicio_cb"] = input("Nova data de início de funcionamento do chatbot(DD/MM/YYY): ")
                chatbot["api_token"] = input("Novo API token do chatbot: ")
                print("Chatbot atualizado com sucesso.")
                return
        print("Chatbot não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar chatbot: {e}")

def deletar_chatbot():
    try:
        id_chatbot = input("ID do chatbot a ser deletado: ")
        for chatbot in chatbots:
            if chatbot["id_chatbot"] == id_chatbot:
                chatbots.remove(chatbot)
                print("Chatbot deletado com sucesso.")
                return
        print("Chatbot não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar chatbot: {e}")

def exportar_para_json():
    try:
        with open("dados.json", "w") as arquivo:
            json.dump({"clientes": clientes, "funcionarios": funcionarios, "chatbots": chatbots}, arquivo)
        print("Dados exportados para dados.json com sucesso.")
    except Exception as e:
        print(f"Erro ao exportar dados para JSON: {e}")

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Cliente")
        print("2. Funcionário")
        print("3. Chatbot")
        print("4. Exportar dados para JSON")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cliente()
        elif opcao == "2":
            menu_funcionario()
        elif opcao == "3":
            menu_chatbot()
        elif opcao == "4":
            exportar_para_json()
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_cliente():
    while True:
        print("\nMenu Cliente:")
        print("1. Criar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            atualizar_cliente()
        elif opcao == "4":
            deletar_cliente()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcionario():
    while True:
        print("\nMenu Funcionário:")
        print("1. Criar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Deletar Funcionário")
        print("5. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            atualizar_funcionario()
        elif opcao == "4":
            deletar_funcionario()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_chatbot():
    while True:
        print("\nMenu Chatbot:")
        print("1. Criar Chatbot")
        print("2. Listar Chatbots")
        print("3. Atualizar Chatbot")
        print("4. Deletar Chatbot")
        print("5. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_chatbot()
        elif opcao == "2":
            listar_chatbots()
        elif opcao == "3":
            atualizar_chatbot()
        elif opcao == "4":
            deletar_chatbot()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
