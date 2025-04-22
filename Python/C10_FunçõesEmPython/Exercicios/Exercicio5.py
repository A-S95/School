# Fazer um programa que gere um parque de estacionamento com sete posições.
# Para cada lugar deve guardar o estado do lugar e a matrícula do veículo que ocupa esse lugar.
# O programa deve apresentar um menu com as seguintes opções:
# - Listar lugares;
# - Marcar lugar;
# - Libertar lugar;
# - Sair do programa.

import os

def inicializaDados(vetor, numLugares, estadoInicial):
    vetor = [(estadoInicial, "") for cLugar in range(0, numLugares, 1)]
    return vetor

def mostraMenu(numLugaresOcupados):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("***********************************")
    print("***********************************")
    print("******** Parque Guest *************")
    print("***********************************")
    print("*        A. Listar lugares.       *")
    print("*        B. Marcar lugares.       *")
    print("*        C. Libertar lugar.       *")
    print("*       D. Sair do programa.      *")
    print("***********************************")
    print("***********************************")
    print()
    if numLugaresOcupados == NUMLUGARES:
        print("***********************************")
        print("* PARQUE CHEIO!!!!        *")
        print("***********************************")
    print()
    return

def obtemEscolha(escolha):
    print("Qual é a sua escolha (A-D) [A]? ", end="")
    escolha = input()
    if len(escolha) == 0:  # Fiz ENTER
        escolha = 'A'  # ou "A"
    else:
        escolha = escolha[0]
    return escolha

def processaEscolha(escolha, lugares, numLugares,
                    estadoLIVRE, estadoOCUPADO, numLugaresOcupados,
                    queroSair):
    match escolha:
        case 'A' | 'a':  # Listagem de lugares.
            print("Listagem de Lugares:")
            for contaLugar in range(0, numLugares, 1):
                print("-> Lugar " + str(contaLugar + 1) + ": ", end="")
                if lugares[contaLugar][0] == estadoLIVRE:
                    print("livre.")
                else:
                    print("ocupado. Matrícula:", lugares[contaLugar][1])
            print("Prima ENTER para continuar ... ", end="")
            input()
        case 'B' | 'b':  # Marcar lugar.
            if numLugaresOcupados == numLugares:
                print(" Parque Cheio!! ")
            else:
                print("Qual o lugar a ocupar (1-"
                      + str(numLugares) + ")? ", end="")
                numLugar = input()
                if not numLugar.isdigit():
                    print("Não inseriu um valor numérico!")
                else:  # Inseriu um valor numérico.
                    numLugar = int(numLugar)
                    if numLugar < 1 or numLugar > numLugares:
                        print("Lugar inválido!")
                        print("Os lugares vão de 1 a "
                              + str(numLugares) + ".")
                    else:  # Lugar é valido.
                        if lugares[numLugar - 1][0] == estadoOCUPADO:
                            print("O lugar já está ocupado!")
                        else:  # Lugar válido e livre.
                            matricula = input("Digite a matrícula do veículo: ")
                            lugares[numLugar - 1] = (estadoOCUPADO, matricula)
                            print("Lugar ocupado com sucesso!")
                            numLugaresOcupados += 1
                print("Prima ENTER para continuar ... ", end="")
                input()
        case 'C' | 'c':  # libertar lugar.
            print("Qual o lugar a libertar (1-"
                  + str(numLugares) + ")? ", end="")
            numLugar = input()
            if not numLugar.isdigit():
                print("Não inseriu um valor numérico!")
            else:  # Inseriu um valor numérico.
                numLugar = int(numLugar)
                if numLugar < 1 or numLugar > numLugares:
                    print("Lugar inválido!")
                    print("Os lugares vão de 1 a "
                          + str(numLugares) + ".")
                else:  # Lugar é valido.
                    if lugares[numLugar - 1][0] == estadoLIVRE:
                        print("O lugar já está livre!")
                    else:  # Lugar válido e ocupado.
                        lugares[numLugar - 1] = (estadoLIVRE, "")
                        print("Lugar libertado com sucesso!")
                        numLugaresOcupados -= 1
            print("Prima ENTER para continuar ... ", end="")
            input()
        case 'D' | 'd':  # Sair do Programa.
            print("Tem a certeza que quer sair (S/N) [N]? ", end="")
            # print("Tem a certeza que quer sair (s/N)? ", end="")
            resposta = input()
            resposta = resposta.upper()
            if resposta == "S":
                queroSair = True
        case _:  # Escolha inválida
            print("Escolha inválida!")
            print("As escolhas vão de A a D.")
            print("Prima ENTER para continuar ... ", end="")
            input()
    return queroSair


def cicloPrincipal(lugares, numLugares, estadoLIVRE, estadoOCUPADO):
    queroSair = False
    numLugaresOcupados = 0
    escolha = '\0'

    while(not queroSair):
        mostraMenu(numLugaresOcupados)
        escolha = obtemEscolha(escolha)
        queroSair = processaEscolha(escolha, lugares, numLugares,
                                    estadoLIVRE, estadoOCUPADO, numLugaresOcupados,
                                    queroSair)
    return


def despedida():
    print("Obrigado por ter usado o programa!")
    return

NUMLUGARES = 7
LIVRE = 0
OCUPADO = 1
lugares = []

lugares = inicializaDados(lugares, NUMLUGARES, LIVRE)
cicloPrincipal(lugares, NUMLUGARES, LIVRE, OCUPADO)
despedida()