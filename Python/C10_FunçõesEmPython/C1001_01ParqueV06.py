####################################################
# Capítulo 08 - Vetores Indexados
####################################################
#
#  Enunciado:
#
#     Faça um programa que gere
#      a ocupação dos sete lugares de um parque de
#      estacionamento.
#
#     O programa deve apresentar um menu com
#     as seguintes opções:
#
#     A. Listar lugares.
#     B. Marcar lugar como ocupado.
#     C. Libertar lugar.
#     D. Sair do programa.
#
#####################################################
# Solução
# 1. Dados
# 1.1 Quais são os dados do programa?
#     Entrada(s):  escolhaMenu (char),
#                  numLugar (int), resposta (char)
#     Saída(s):
#        Listagem de lugares
#        Mensagem B = "Lugar ocupado com sucesso!"
#        Mensagem C = "Lugar libertado com sucesso!"
#
###################################################
# 2. Algoritmo
#
# 2.0 Inicialização das Estrutura de Dados
# 2.1 Ciclo principal do programa
#    2.1.0 Apresentação do Menu
#    2.1.1 Obter a escolha do utilizador
#    2.1.2 Processar a escolha
# 2.2 Despedida
#
###################################################
# 3. Programa
# 3.0 Bibliotecas ou Módulos Python
import os

# 3.2 Algoritmo
###############################################
# Funções
###############################################

###############################################
# Função "inicializaDados()"
###############################################
def inicializaDados(vetor, numLugares, estadoInicial):
    vetor = [estadoInicial for cLugar in range(0, numLugares, 1)]
    return vetor

###############################################
# Função "mostraMenu()"
###############################################
def mostraMenu(numLugaresOcupados):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("***********************************")
    print("*                                 *")
    print("*             Parque Gest         *")
    print("*                                 *")
    print("*      A. Listar lugares.         *")
    print("*      B. Marcar lugar.           *")
    print("*      C. Libertar lugar.         *")
    print("*      D. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()
    if numLugaresOcupados == NUMLUGARES:
        print("***********************************")
        print("*         PARQUE CHEIO!!!!        *")
        print("***********************************")
    print()
    return

###############################################
# Função "obtemEscolha()"
###############################################
def obtemEscolha(escolha):
    print("Qual é a sua escolha (A-D) [A]? ",end="")
    escolha = input()
    if len(escolha) == 0: # Fiz ENTER
        escolha='A' # ou "A"
    else:
        escolha = escolha[0]
    return escolha

###############################################
# Função "processaEscolha()"
###############################################
def processaEscolha(escolha, lugares, numLugares,
                        estadoLIVRE, estadoOCUPADO, numLugaresOcupados,
                    queroSair):
    match escolha:
        case 'A' | 'a':  # Listagem de lugares.
            print("Listagem de Lugares:")
            for contaLugar in range(0, numLugares, 1):
                print("-> Lugar " + str(contaLugar + 1) + ": ", end="")
                if lugares[contaLugar] == estadoLIVRE:
                    print("livre.")
                else:
                    print("ocupado.")
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
                        if lugares[numLugar - 1] == estadoOCUPADO:
                            print("O lugar já está ocupado!")
                        else:  # Lugar válido e livre.
                            lugares[numLugar - 1] = estadoOCUPADO
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
                    if lugares[numLugar - 1] == estadoLIVRE:
                        print("O lugar já está livre!")
                    else:  # Lugar válido e ocupado.
                        lugares[numLugar - 1] = estadoLIVRE
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

###############################################
# Função "cicloPrincipal()"
###############################################
def cicloPrincipal(lugares,numLugares, estadoLIVRE, estadoOCUPADO):
    # Dados locais
    # Só estão diosponiveis na função onde estão
    # declarados.
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

################################################
# Função "despedida()"
################################################
def despedida():
    print("Obrigado por ter usado o programa!")
    return

################################################
# Programa Principal
################################################
# 3.1 Dados Globais
#     Podem ser lidos ou alterados por qualquer
#     função.
NUMLUGARES = 7
LIVRE = 0
OCUPADO = 1
lugares = []


lugares = inicializaDados(lugares, NUMLUGARES, LIVRE)
cicloPrincipal(lugares, NUMLUGARES, LIVRE, OCUPADO)
despedida()






