import os

def inicializaDados():
    return {}

def mostraMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("***********************************")
    print("***********************************")
    print("*       Gestão de Armazém         *")
    print("***********************************")
    print("* 1. Listar produtos.             *")
    print("* 2. Inserir produto.             *")
    print("* 3. Alterar preço.               *")
    print("* 4. Registar venda.              *")
    print("* 5. Registar reposição.          *")
    print("* 6. Eliminar produto.            *")
    print("* 7. Sair do programa.            *")
    print("***********************************")
    print("***********************************")
    print()

def obtemEscolha():
    print("Qual é a sua escolha (1-7)? ", end="")
    escolha = input()
    return escolha

def processaEscolha(escolha, inventario):
    match escolha:
        case '1':  # Listar produtos.
            print("Listagem de Produtos:")
            for nome, dados in inventario.items():
                print(f"Nome: {nome}, Preço: {dados['preco']}, Unidades: {dados['unidades']}")
            input("Prima ENTER para continuar ... ")
        case '2':  # Inserir produto.
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            unidades = int(input("Número de unidades: "))
            inventario[nome] = {'preco': preco, 'unidades': unidades}
            print("Produto inserido com sucesso!")
            input("Prima ENTER para continuar ... ")
        case '3':  # Alterar preço.
            nome = input("Nome do produto: ")
            if nome in inventario:
                novo_preco = float(input("Novo preço: "))
                inventario[nome]['preco'] = novo_preco
                print("Preço alterado com sucesso!")
            else:
                print("Produto não encontrado.")
            input("Prima ENTER para continuar ... ")
        case '4':  # Registar venda.
            nome = input("Nome do produto: ")
            if nome in inventario:
                quantidade = int(input("Quantidade vendida: "))
                if inventario[nome]['unidades'] >= quantidade:
                    inventario[nome]['unidades'] -= quantidade
                    print("Venda registada com sucesso!")
                else:
                    print("Quantidade insuficiente em stock.")
            else:
                print("Produto não encontrado.")
            input("Prima ENTER para continuar ... ")
        case '5':  # Registar reposição.
            nome = input("Nome do produto: ")
            if nome in inventario:
                quantidade = int(input("Quantidade reposta: "))
                inventario[nome]['unidades'] += quantidade
                print("Reposição registada com sucesso!")
            else:
                print("Produto não encontrado.")
            input("Prima ENTER para continuar ... ")
        case '6':  # Eliminar produto.
            nome = input("Nome do produto: ")
            if nome in inventario:
                del inventario[nome]
                print("Produto eliminado com sucesso!")
            else:
                print("Produto não encontrado.")
            input("Prima ENTER para continuar ... ")
        case '7':  # Sair do Programa.
            return True
        case _:  # Escolha inválida
            print("Escolha inválida!")
            print("As escolhas vão de 1 a 7.")
            input("Prima ENTER para continuar ... ")
    return False

def cicloPrincipal():
    inventario = inicializaDados()
    queroSair = False

    while not queroSair:
        mostraMenu()
        escolha = obtemEscolha()
        queroSair = processaEscolha(escolha, inventario)
    return

def despedida():
    print("Obrigado por ter usado o programa!")
    return

cicloPrincipal()
despedida()