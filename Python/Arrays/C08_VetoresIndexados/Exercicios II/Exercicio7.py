# Gestao de 10 Taxis

# Listar taxis
# Reservar Taxi
# Chamar Taxi
# Libertar Taxi
# Sair do programa

import os

numDeTaxi = 10
desocupado = 0
reservado = 1
ocupado = 2
queroSair = False

Taxi = [0 for contaTaxis in range(0,numDeTaxi,1)]

while not queroSair:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("")
    print("***********************************")
    print("*                                 *")
    print("*             Taxi APP            *")
    print("*                                 *")
    print("*      A. Listar Taxis.           *")
    print("*      B. Reservar Taxi.          *")
    print("*      C. Chamar Taxi.            *")
    print("*      D. Libertar Taxi.          *")
    print("*      E. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()
    # 3.2.1.1 Obter escolha do utilizador
    print("Qual é a sua escolha (A-J)? ",end="")
    escolha = input()
    
    if len(escolha) == 0: 
        escolha='A' 
    else:
        escolha = escolha[0]

    match escolha:
        case 'A' | 'a':
            for contaTaxis in range(numDeTaxi):
                if Taxi[contaTaxis] == desocupado: 
                    print("Taxi ", contaTaxis+1, " - Desocupado")
                elif Taxi[contaTaxis] == reservado:
                    print("Taxi ", contaTaxis+1, " - Reservado")
                else:
                    print("Taxi ", contaTaxis+1, " - Ocupado")
            input("Pressione ENTER para continuar...")

        case 'B' | 'b': # Reservar Taxis.
            print("Qual o Taxi a reservar (1-"
                  +str(numDeTaxi)+"? ", end="")
            numeroDeTaxi = int(input())
            if numeroDeTaxi < 1 or numeroDeTaxi > numDeTaxi:
                print("Mesa inválida!")
                print("As mesas vão de 1 a "
                      +str(numDeTaxi)+".")
            else: # Taxi valido.
                if Taxi[numeroDeTaxi-1] != desocupado:
                    print("O taxi que escolheu, já está reservado ou ocupado!")
                else: # Lugar válido e livre.
                    Taxi[numeroDeTaxi-1] = reservado
                    print("Taxi reservado com sucesso!")
            input("Prima ENTER para continuar ... ")

        case 'C' | 'c': # Chamar Taxi.
            print("Qual o Taxi a chamar (1-"
                  +str(numDeTaxi)+"? ", end="")
            numeroDeTaxi = int(input())
            if numeroDeTaxi < 1 or numeroDeTaxi > numDeTaxi:
                print("Taxi inválido!")
                print("Os taxis vão de 1 a "
                      +str(numDeTaxi)+".")
            else: # Taxi valido.
                if Taxi[numeroDeTaxi-1]!= desocupado:
                    print("O taxi que escolheu, já está reservado ou ocupado!")
                else: # Lugar válido e livre.
                    Taxi[numeroDeTaxi-1] = ocupado
                    print("Taxi chamado com sucesso!")
            input("Prima ENTER para continuar...")

        case 'D' | 'd': # Desmarcar Taxi.
            print("Qual o Taxi a desocupar (1-"
                  +str(numDeTaxi)+"? ", end="")
            numeroDeTaxi = int(input())
            if numeroDeTaxi < 1 or numeroDeTaxi > numDeTaxi:
                print("Taxi inválido!")
                print("A lista de taxi vai de 1 a "
                      +str(numDeTaxi)+".")
            else: # Lugar é valido.
                if Taxi[numeroDeTaxi-1] == desocupado:
                    print("O Taxi que escolheu, já está desocupado!")
                else: # Lugar válido e ocupado.
                    Taxi[numeroDeTaxi-1] = desocupado
                    print("Taxi desocupado com sucesso!")
            input("Prima ENTER para continuar ... ")

        case 'E' | 'e': # Sair do programa.
            print("Tem a certeza que quer sair (S/N) [N]? ", end="")
            #print("Tem a certeza que quer sair (s/N)? ", end="")
            resposta = input()
            resposta = resposta.upper()
            if resposta == "S":
                queroSair = True
        case _ : # Escolha inválida
            print("Escolha inválida!")
            print("As escolhas vão de A a E.")
            print("Prima ENTER para continuar ... ",end="")
            input()