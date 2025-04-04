# Gestao de um estadio

import os

# 3.1 Dados
# Estados de cada lugar
LIVRE = 'L'
RESERVADO = 'R'
OCUPADO = 'O'

NUMFILAS = 6
NUMLUGARESPORFILA = 7

queroSair = False

lugares = [[LIVRE for _ in range(NUMLUGARESPORFILA)] for _ in range(NUMFILAS)]

# 3.2.1 Ciclo principal do programa
while not queroSair:
    # 3.2.1.1 Apresentar menu de opções
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o ecrã
    print("")
    print("***********************************")
    print("*                                 *")
    print("*          Estadio Fut            *")
    print("*                                 *")
    print("*      1. Listar Lugares          *")
    print("*      2. Reservar Lugares        *")
    print("*      3. Ocupar Lugar            *")
    print("*      4. Fim do jogo             *")
    print("*      5. Sair do programa        *")
    print("*                                 *")
    print("***********************************")
    print()

    # 3.2.1.2 Obter escolha do utilizador
    print("Qual é a sua escolha (1-5) [1]? ", end="")
    escolha = input()
    if len(escolha) == 0:  # Fiz ENTER
        escolha = '1'
    else:
        escolha = escolha[0]

    # 3.2.1.3 Processar a escolha
    match escolha:
        case '1':  # Listagem dos lugares
            print("Listagem de Lugares: ")
            for cFila in range(NUMFILAS):
                print(f"Fila {cFila + 1}: ", end="")
                for cLugar in range(NUMLUGARESPORFILA):
                    if lugares[cFila][cLugar] == LIVRE:
                        print("[ ]", end=" ")
                    elif lugares[cFila][cLugar] == RESERVADO:
                        print("[R]", end=" ")
                    else:
                        print("[O]", end=" ")
                print()  # Nova linha após cada fila
            input("Prima ENTER para continuar ... ")

        case '2':  # Reservar lugar
            print("Reserva de Lugar")
            print(f"Qual a fila a selecionar (1-{NUMFILAS})? ", end="")
            numFila = input()
            print(f"Nessa fila, qual é o lugar a reservar (1-{NUMLUGARESPORFILA})? ", end="")
            numLugar = input()

            if not numFila.isdigit() or not numLugar.isdigit():
                print("Não inseriu um valor numérico de fila ou lugar!")
            else:
                numFila = int(numFila)
                numLugar = int(numLugar)
                if (numFila < 1 or numFila > NUMFILAS
                        or numLugar < 1 or numLugar > NUMLUGARESPORFILA):
                    print("Valores inseridos fora da gama válida!")
                else:
                    if lugares[numFila - 1][numLugar - 1] != LIVRE:
                        print("O lugar não está livre!")
                    else:
                        lugares[numFila - 1][numLugar - 1] = RESERVADO
                        print("Lugar reservado com sucesso!")
            input("Prima ENTER para continuar ... ")

        case '3':  # Ocupar Lugar
            print("Ocupar Lugar")
            print(f"Qual a fila a selecionar (1-{NUMFILAS})? ", end="")
            numFila = input()
            print(f"Nessa fila, qual é o lugar a ocupar (1-{NUMLUGARESPORFILA})? ", end="")
            numLugar = input()

            if not numFila.isdigit() or not numLugar.isdigit():
                print("Não inseriu um valor numérico de fila ou lugar!")
            else:
                numFila = int(numFila)
                numLugar = int(numLugar)
                if (numFila < 1 or numFila > NUMFILAS
                        or numLugar < 1 or numLugar > NUMLUGARESPORFILA):
                    print("Valores inseridos fora da gama válida!")
                else:
                    if lugares[numFila - 1][numLugar - 1] == OCUPADO:
                        print("O lugar já está ocupado!")
                    else:
                        lugares[numFila - 1][numLugar - 1] = OCUPADO
                        print("Lugar ocupado com sucesso!")
            input("Prima ENTER para continuar ... ")

        case '4':  # Fim do jogo
            print("Fim do jogo")
            lugares = [[LIVRE for _ in range(NUMLUGARESPORFILA)] for _ in range(NUMFILAS)]
            print("Todos os lugares foram redefinidos como livres.")
            input("Prima ENTER para continuar")

        case '5':  # Sair do programa
            print("Tem a certeza que quer sair (S/N) [N]? ", end="")
            resposta = input().upper()
            if resposta == "S":
                queroSair = True

        case _:  # Escolha inválida
            print("Escolha inválida!")
            print("As escolhas vão de 1 a 5.")
            input("Prima ENTER para continuar ... ")

# 3.2.2 Despedida
print("Obrigado por ter usado o programa!")