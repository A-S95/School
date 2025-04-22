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
# Função "cicloPrincipal()"
###############################################
def cicloPrincipal(lugares, estadoLIVRE, estadoOCUPADO):
    # Dados locais
    # Só estão diosponiveis na função onde estão
    # declarados.
    queroSair = False
    escolha = '\0'

    while(not queroSair):
        mostraMenu(lugares, estadoOCUPADO)
        escolha = obtemEscolha(escolha)
        queroSair = processaEscolha(escolha, lugares,
                        estadoLIVRE, estadoOCUPADO,
                         queroSair)
    return

###############################################
# Função "mostraMenu()"
###############################################
def mostraMenu(lugares, estadoOCUPADO):
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
    if (obtemNumLugaresOcupados(lugares, estadoOCUPADO)
            == len(lugares)):
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
def processaEscolha(escolha, lugares, estadoLIVRE,
                    estadoOCUPADO, queroSair):
    match escolha:
        case 'A' | 'a':  # Listagem de lugares.
            listarLugares(lugares,estadoLIVRE)
        case 'B' | 'b':  # Marcar lugar.
            lugares = marcarLugar(lugares,estadoOCUPADO)
        case 'C' | 'c':  # libertar lugar.
            lugares = libertarLugar(lugares,estadoLIVRE)
        case 'D' | 'd':  # Sair do Programa.
            queroSair = sairDoPrograma()
        case _:  # Escolha inválida
            escolhaInvalida()
    return queroSair

###############################################
# Função "listarLugares()"
###############################################
def listarLugares(lugares, estadoLIVRE):
    print("Listagem de Lugares:")
    for contaLugar in range(0, len(lugares), 1):
        print("-> Lugar " + str(contaLugar + 1) + ": ", end="")
        if lugares[contaLugar] == estadoLIVRE:
            print("livre.")
        else:
            print("ocupado.")
    print("Prima ENTER para continuar ... ", end="")
    input()
    return

###############################################
# Função "obtemNumLugaresOcupados()"
###############################################
def obtemNumLugaresOcupados(lugares, estadoOCUPADO):
    numLugaresOcupados = 0
    for cLugar in range(0,len(lugares),1):
        if lugares[cLugar] == estadoOCUPADO:
            numLugaresOcupados += 1
    return numLugaresOcupados

###############################################
# Função "marcarLugar()"
###############################################
def marcarLugar(lugares, estadoOCUPADO):
    if (obtemNumLugaresOcupados(lugares, estadoOCUPADO)
            == len(lugares)):
        print(" Parque Cheio!! ")
    else:
        print("Qual o lugar a ocupar (1-"
              + str(len(lugares)) + ")? ", end="")
        numLugar = input()
        if not numLugar.isdigit():
            print("Não inseriu um valor numérico!")
        else:  # Inseriu um valor numérico.
            numLugar = int(numLugar)
            if numLugar < 1 or numLugar > len(lugares):
                print("Lugar inválido!")
                print("Os lugares vão de 1 a "
                      + str(len(lugares)) + ".")
            else:  # Lugar é valido.
                if lugares[numLugar - 1] == estadoOCUPADO:
                    print("O lugar já está ocupado!")
                else:  # Lugar válido e livre.
                    lugares[numLugar - 1] = estadoOCUPADO
                    print("Lugar ocupado com sucesso!")
    print("Prima ENTER para continuar ... ", end="")
    input()
    return lugares

###############################################
# Função "libertarLugar()"
###############################################
def libertarLugar(lugares, estadoLIVRE):
    print("Qual o lugar a libertar (1-"
          + str(len(lugares)) + ")? ", end="")
    numLugar = input()
    if not numLugar.isdigit():
        print("Não inseriu um valor numérico!")
    else:  # Inseriu um valor numérico.
        numLugar = int(numLugar)
        if numLugar < 1 or numLugar > len(lugares):
            print("Lugar inválido!")
            print("Os lugares vão de 1 a "
                  + str(len(lugares)) + ".")
        else:  # Lugar é valido.
            if lugares[numLugar - 1] == estadoLIVRE:
                print("O lugar já está livre!")
            else:  # Lugar válido e ocupado.
                lugares[numLugar - 1] = estadoLIVRE
                print("Lugar libertado com sucesso!")
    print("Prima ENTER para continuar ... ", end="")
    input()
    return lugares

###############################################
# Função "sairDoPrograma()"
###############################################
def sairDoPrograma():
    print("Tem a certeza que quer sair (S/N) [N]? ", end="")
    # print("Tem a certeza que quer sair (s/N)? ", end="")
    resposta = input()
    resposta = resposta.upper()
    if resposta == "S":
        return True
    else:
        return False

###############################################
# Função "escolhaInvalida()"
###############################################
def escolhaInvalida():
    print("Escolha inválida!")
    print("As escolhas vão de A a D.")
    print("Prima ENTER para continuar ... ", end="")
    input()

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
cicloPrincipal(lugares, LIVRE, OCUPADO)
despedida()







