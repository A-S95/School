# Gestao de Inventario num Armazem

# Nome produto, preço do produto, numero de unidades.

# Listar Produtos
# Inserir produto
# Alterar preço
# Registar venda
# Registar reposição
# Eliminar produto
# Sair do programa.

# Gestao de Inventario num Armazem

import os

# Dados
produtos = []
queroSair = False

# Ciclo principal do programa
while(not queroSair):
    # Apresentar menu de opções
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o ecrã
    print("")
    print("***********************************")
    print("*                                 *")
    print("*    Gestão de Inventário         *")
    print("*                                 *")
    print("*      1. Listar Produtos         *")
    print("*      2. Inserir Produto         *")
    print("*      3. Alterar Preço           *")
    print("*      4. Registar Venda          *")
    print("*      5. Registar Reposição      *")
    print("*      6. Eliminar Produto        *")
    print("*      7. Sair do Programa        *")
    print("*                                 *")
    print("***********************************")
    print()

    # Obter escolha do utilizador
    print("Qual é a sua escolha (1-7) [1]? ", end="")
    escolha = input()
    if len(escolha) == 0:  # Fiz ENTER
        escolha = '1'
    else:
        escolha = escolha[0]

    # Processar a escolha
    match escolha:
        case '1':  # Listar Produtos
            print("Listagem de Produtos:")
            if not produtos:
                print("Não há produtos no inventário.")
            else:
                for i, produto in enumerate(produtos, 1):
                    print(f"{i}. Nome: {produto['nome']}, Preço: {produto['preco']:.2f}€, Unidades: {produto['unidades']}")
            input("Prima ENTER para continuar...")

        case '2':  # Inserir Produto
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            unidades = int(input("Número de unidades: "))
            produtos.append({"nome": nome, "preco": preco, "unidades": unidades})
            print("Produto inserido com sucesso!")
            input("Prima ENTER para continuar...")

        case '3':  # Alterar Preço
            nome = input("Nome do produto para alterar o preço: ")
            for produto in produtos:
                if produto['nome'].lower() == nome.lower():
                    novo_preco = float(input("Novo preço: "))
                    produto['preco'] = novo_preco
                    print("Preço alterado com sucesso!")
                    break
            else:
                print("Produto não encontrado.")
            input("Prima ENTER para continuar...")

        case '4':  # Registar Venda
            nome = input("Nome do produto vendido: ")
            for produto in produtos:
                if produto['nome'].lower() == nome.lower():
                    quantidade = int(input("Quantidade vendida: "))
                    if quantidade <= produto['unidades']:
                        produto['unidades'] -= quantidade
                        print("Venda registada com sucesso!")
                    else:
                        print("Quantidade insuficiente em stock.")
                    break
            else:
                print("Produto não encontrado.")
            input("Prima ENTER para continuar...")

        case '5':  # Registar Reposição
            nome = input("Nome do produto para repor: ")
            for produto in produtos:
                if produto['nome'].lower() == nome.lower():
                    quantidade = int(input("Quantidade a repor: "))
                    produto['unidades'] += quantidade
                    print("Reposição registada com sucesso!")
                    break
            else:
                print("Produto não encontrado.")
            input("Prima ENTER para continuar...")

        case '6':  # Eliminar Produto
            nome = input("Nome do produto a eliminar: ")
            for produto in produtos:
                if produto['nome'].lower() == nome.lower():
                    produtos.remove(produto)
                    print("Produto eliminado com sucesso!")
                    break
            else:
                print("Produto não encontrado.")
            input("Prima ENTER para continuar...")

        case '7':  # Sair do Programa
            print("Tem a certeza que quer sair (S/N) [N]? ", end="")
            resposta = input().upper()
            if resposta == "S":
                queroSair = True

        case _:  # Escolha inválida
            print("Escolha inválida!")
            print("As escolhas vão de 1 a 7.")
            input("Prima ENTER para continuar...")

# Despedida
print("Obrigado por ter usado o programa!")