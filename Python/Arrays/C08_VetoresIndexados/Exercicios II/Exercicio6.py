# Gestao de mesas de um restaurante 
# 10 mesas 

# Listar Mesas
# Reservar Mesas
# Ocupar Mesa
# Desocupar Mesa
# Sair do programa
import os

numMesas = 10
desocupado = 0
reservado = 1
ocupado = 2
queroSair = False

Mesas = [0 for contaMesas in range(0,numMesas,1)]

while not queroSair:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("***********************************")
    print("*                                 *")
    print("*        Restaurante Free         *")
    print("*                                 *")
    print("*      A. Listar Mesas.           *")
    print("*      B. Reservar Mesas.         *")
    print("*      C. Ocupar Mesa.            *")
    print("*      D. Desocupar Mesa.         *")
    print("*      E. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()

    print("Qual é a sua escolha (A-E)? ",end="")
    escolha = input()

    if len(escolha) == 0: 
        escolha='A' 
    else:
        escolha = escolha[0]


    match escolha:
        case 'A' | 'a':
            for contaMesas in range(numMesas):
                if Mesas[contaMesas] == desocupado: 
                    print("Mesa ", contaMesas+1, " - Desocupada")
                elif Mesas[contaMesas] == reservado:
                    print("Mesa ", contaMesas+1, " - Reservada")
                else:
                    print("Mesa ", contaMesas+1, " - Ocupada")
            input("Pressione ENTER para continuar...")

        case 'B' | 'b': # Reservar mesas.
            print("Qual a mesa a reservar (1-"
                  +str(numMesas)+"? ", end="")
            numDeMesa = int(input())
            if numDeMesa < 1 or numDeMesa > numMesas:
                print("Mesa inválida!")
                print("As mesas vão de 1 a "
                      +str(numMesas)+".")
            else: # mesa valida.
                if Mesas[numDeMesa-1] != desocupado:
                    print("A mesa já está reservada ou ocupada!")
                else: # Lugar válido e livre.
                    Mesas[numDeMesa-1] = reservado
                    print("Mesa reservada com sucesso!")
            input("Prima ENTER para continuar ... ")

        case 'C' | 'c': # Ocupar lugar.
            print("Qual a mesa a ocupar (1-"
                  +str(numMesas)+"? ", end="")
            numDeMesa = int(input())
            if numDeMesa < 1 or numDeMesa > numMesas:
                print("Mesa inválida!")
                print("As mesas vão de 1 a "
                      +str(numMesas)+".")
            else: # Lugar é valido.
                if Mesas[numDeMesa-1] == reservado or Mesas[numDeMesa-1] == ocupado:
                    print("Mesa já está ocupada!")
                elif Mesas[numDeMesa-1] == reservado:
                    print("Mesa já está reservada!")
                else: # Lugar válido e livre.
                    Mesas[numDeMesa-1] = ocupado
                    print("Mesa ocupada com sucesso!")
            input("Prima ENTER para continuar ... ")

        case 'D' | 'd': # Desmarcar lugar.
            print("Qual a mesa a desocupar (1-"
                  +str(numMesas)+"? ", end="")
            numDeMesa = int(input())
            if numDeMesa < 1 or numDeMesa > numMesas:
                print("Mesa inválido!")
                print("As mesas vão de 1 a "
                      +str(numMesas)+".")
            else: # Lugar é valido.
                if Mesas[numDeMesa-1] == desocupado:
                    print("O lugar já está desocupado!")
                else: # Lugar válido e ocupado.
                    Mesas[numDeMesa-1] = desocupado
                    print("Mesa desocupada com sucesso!")
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