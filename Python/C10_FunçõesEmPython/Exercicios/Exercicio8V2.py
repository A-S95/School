import os

NUM_ANDARES = 3
QUARTOS_POR_ANDAR = 5
LIVRE = 0
RESERVADO = 1
OCUPADO = 2

def inicializaDados():
    quartos = {}
    for andar in range(NUM_ANDARES):
        for quarto in range(QUARTOS_POR_ANDAR):
            quartos[(andar, quarto)] = LIVRE
    return quartos

def mostraMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("***********************************")
    print("***********************************")
    print("*        Gestão da Pensão         *")
    print("***********************************")
    print("* 1. Listar quartos.             *")
    print("* 2. Reservar quarto.            *")
    print("* 3. Ocupar quarto.              *")
    print("* 4. Desocupar quarto.           *")
    print("* 5. Sair do programa.           *")
    print("***********************************")
    print("***********************************")
    print()

def obtemEscolha():
    print("Qual é a sua escolha (1-5)? ", end="")
    escolha = input()
    return escolha

def processaEscolha(escolha, quartos):
    match escolha:
        case '1':  # Listar quartos.
            print("Listagem de Quartos:")
            for (andar, quarto), estado in quartos.items():
                estado_str = "Livre" if estado == LIVRE else "Reservado" if estado == RESERVADO else "Ocupado"
                print(f"Andar {andar + 1}, Quarto {quarto + 1}: {estado_str}")
            input("Prima ENTER para continuar ... ")
        case '2':  # Reservar quarto.
            andar = int(input("Andar (1-3): ")) - 1
            quarto = int(input("Quarto (1-5): ")) - 1
            if (andar, quarto) in quartos:
                if quartos[(andar, quarto)] == LIVRE:
                    quartos[(andar, quarto)] = RESERVADO
                    print("Quarto reservado com sucesso!")
                else:
                    print("Quarto não está livre.")
            else:
                print("Quarto inválido.")
            input("Prima ENTER para continuar ... ")
        case '3':  # Ocupar quarto.
            andar = int(input("Andar (1-3): ")) - 1
            quarto = int(input("Quarto (1-5): ")) - 1
            if (andar, quarto) in quartos:
                if quartos[(andar, quarto)] == RESERVADO:
                    quartos[(andar, quarto)] = OCUPADO
                    print("Quarto ocupado com sucesso!")
                else:
                    print("Quarto não está reservado.")
            else:
                print("Quarto inválido.")
            input("Prima ENTER para continuar ... ")
        case '4':  # Desocupar quarto.
            andar = int(input("Andar (1-3): ")) - 1
            quarto = int(input("Quarto (1-5): ")) - 1
            if (andar, quarto) in quartos:
                if quartos[(andar, quarto)] == OCUPADO:
                    quartos[(andar, quarto)] = LIVRE
                    print("Quarto desocupado com sucesso!")
                else:
                    print("Quarto não está ocupado.")
            else:
                print("Quarto inválido.")
            input("Prima ENTER para continuar ... ")
        case '5':  # Sair do Programa.
            return True
        case _:  # Escolha inválida
            print("Escolha inválida!")
            print("As escolhas vão de 1 a 5.")
            input("Prima ENTER para continuar ... ")
    return False

def cicloPrincipal():
    quartos = inicializaDados()
    queroSair = False

    while not queroSair:
        mostraMenu()
        escolha = obtemEscolha()
        queroSair = processaEscolha(escolha, quartos)
    return

def despedida():
    print("Obrigado por ter usado o programa!")
    return


cicloPrincipal()
despedida()