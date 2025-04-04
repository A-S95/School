# Gestao de Cinema
# Sete filas
# Cinco Lugares por fila

# / MENU /
# - Listar Lugares
# - Reservar Lugares
# - Marcar Lugares
# - Libertar lugar
# - Fim de sessao
# - Sair do Programa

import os

# 3.1 Dados
# Estados de cada quarto
LIVRE = 'L'
RESERVADO = 'R'
OCUPADO = 'O'

NUMFILAS = 7
NUMLUGARESPORFILA = 5

queroSair = False


lugares =[ [LIVRE for cLugar in range(0,NUMLUGARESPORFILA,1)]
             for cFila in range(0,NUMFILAS,1)
         ]

# 3.2.1 Ciclo principal do programa
while(not queroSair):
    # 3.2.1.1 Apresentar menu de opções
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã
    print("")
    print("***********************************")
    print("*                                 *")
    print("*          Cinema MAX             *")
    print("*                                 *")
    print("*      1. Listar Lugares.         *")
    print("*      2. Reservar Lugar.        *")
    print("*      3. Marcar Lugar.          *")
    print("*      4. Libertar Lugar.        *")
    print("*      5. Fim da sessao.          *")
    print("*      6. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()

    # 3.2.1.2 Obter escolha do utilizador
    print("Qual é a sua escolha (1-6) [1]? ", end="")
    escolha = input()
    if len(escolha) == 0:  # Fiz ENTER
        escolha = '1'
    else:
        escolha = escolha[0]

    # 3.2.1.3 Processar a escolha
    match escolha:
        case '1':  # Listagem dos lugares
            print("Listagem de Lugares: ")
            for cFila in range (0,NUMFILAS,1):
                print("Fila "+str(cFila+1)+": ")
                for cLugar in range (0,NUMLUGARESPORFILA,1):
                    print("-> Lugar "+str(cFila+1)+".0"
                          +str(cLugar+1)+": ",end="")
                    if lugares[cFila][cLugar] == LIVRE:
                        print("livre.")
                    elif lugares[cFila][cLugar] == RESERVADO:
                        print("reservado.")
                    else:
                        print("ocupado.")
                print("Prima ENTER para continuar ... ", end="")
                input()
        case '2':  # Reservar lugar
            print("Reserva de Lugar")
            print("Qual a fila a selecionar (1-"
                  +str(NUMFILAS)+")? ", end="")
            numFila = input()
            print("Nessa fila, qual é o lugar a reservar (1-"
                  +str(NUMLUGARESPORFILA)+")? ", end= "")
            numLugar = input()

            if not numFila.isdigit() or not numLugar.isdigit():
                print("Não inseriu um valor numérico de fila ou lugar!")
            else: # Os valores de fila e lugar são numéricos.
                numFila = int(numFila)
                numLugar = int(numLugar)
                if (numFila < 1 or numFila > NUMFILAS
                    or numLugar < 1 or numLugar > NUMLUGARESPORFILA):
                    print("Valores inseridos fora da gama válida!")
                else: # Valores válidos.
                    if lugares[numFila-1][numLugar-1] != LIVRE:
                        print("O lugar não está livre!")
                    else: # Quarto livre.
                        lugares[numFila-1][numLugar-1] = RESERVADO
                        print("Lugar reservado com sucesso!")
            print("Prima ENTER para continuar ... ", end="")
            input()
        case '3':  # Marcar Lugar
            print("Marcar lugar")
            print("Qual a fila a selecionar (1-"
                  + str(NUMFILAS) + ")? ", end="")
            numFila = input()
            print("Nessa fila, qual é o lugar a ocupar (1-"
                  + str(NUMLUGARESPORFILA) + ")? ", end="")
            numLugar = input()

            if not numFila.isdigit() or not numLugar.isdigit():
                print("Não inseriu um valor numérico de fila ou lugar!")
            else:  # Os valores de andar e quarto são numéricos.
                numFila = int(numFila)
                numLugar = int(numLugar)
                if (numFila < 1 or numFila > NUMFILAS
                        or numLugar < 1 or numLugar > NUMLUGARESPORFILA):
                    print("Valores inseridos fora da gama válida!")
                else:  # Valores válidos.
                    if lugares[numFila - 1][numLugar - 1] == OCUPADO:
                        print("O lugar já está ocupado!")
                    else:  # Quarto livre ou reservado.
                        lugares[numFila - 1][numLugar - 1] = OCUPADO
                        print("Lugar ocupado com sucesso!")
            print("Prima ENTER para continuar ... ", end="")
            input()
        case '4':  # Libertar Lugar
            print("Libertar Lugar")
            print("Qual a fila a selecionar (1-"
                  + str(NUMFILAS) + ")? ", end="")
            numFila = input()
            print("Nessa fila, qual é o lugar a libertar (1-"
                  + str(NUMLUGARESPORFILA) + ")? ", end="")
            numLugar = input()

            if not numFila.isdigit() or not numLugar.isdigit():
                print("Não inseriu um valor numérico de fila ou lugar!")
            else:  # Os valores de andar e quarto são numéricos.
                numFila = int(numFila)
                numLugar = int(numLugar)
                if (numFila < 1 or numFila > NUMFILAS
                        or numLugar < 1 or numLugar > NUMLUGARESPORFILA):
                    print("Valores inseridos fora da gama válida!")
                else:  # Valores válidos.
                    if lugares[numFila - 1][numLugar - 1] == LIVRE:
                        print("O lugar já está livre!")
                    else:  # Quarto livre ou reservado.
                        lugares[numFila - 1][numLugar - 1] = LIVRE
                        print("Lugar libertado com sucesso!")
            print("Prima ENTER para continuar ... ", end="")
            input()
        case '5': # Fim da sessao / Limpar todos os registos
            print("Finalização de sessão completa")
            lugares = [[LIVRE for cLugar in range(NUMLUGARESPORFILA)] 
                    for cFila in range(NUMFILAS)]
            print("Todos os lugares foram redefinidos como livres.")
            input("Prima ENTER para continuar")
        case '6':
            print("Tem a certeza que quer sair (S/N) [N]? ", end="")
                # print("Tem a certeza que quer sair (s/N)? ", end="")
            resposta = input()
            resposta = resposta.upper()
            if resposta == "S":
                queroSair = True
        case _:  # Escolha inválida
            print("Escolha inválida!")
            print("As escolhas vão de 1 a 5.")
            print("Prima ENTER para continuar ... ", end="")
            input()

# 3.2.2 Despedida
print("Obrigado por ter usado o programa!")
