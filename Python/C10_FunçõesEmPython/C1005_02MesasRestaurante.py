####################################################
# Capítulo 10 - Funções
####################################################
#
#  Enunciado:
#
#     Faça um programa que gere
#      a ocupação dos 10 mesas de um restaurante.
#
#     O programa deve apresentar um menu com
#     as seguintes opções:
#
#     1. Listar mesas.
#     2. Reservar mesa.
#     3. Ocupar mesa.
#     4. Libertar mesa.
#     5. Sair do programa.
#
#####################################################
# Solução
# 1. Dados
# 1.1 Quais são os dados do programa?
#     Entrada(s):  escolha (char),
#                  numMesa (int), resposta (char)
#     Saída(s):
#        Listagem de mesas
#        Mensagem 2 = "Mesa reservada com sucesso!"
#        Mensagem 3 = "Mesa ocupada com sucesso!"
#        Mensagem 4 = "Mesa libertada com sucesso!"
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

###############################################
# Funções
###############################################

###############################################
# Função "main()"
###############################################
def arranque():
    # 1. Dados
    NUMMESAS = 10
    # Estados
    LIVRE ='L'
    RESERVADO = 'R'
    OCUPADO = 'O'
    mesas = []

    mesas = inicializaEstruturaDeDados(mesas, NUMMESAS, LIVRE)
    cicloPrincipal(mesas, LIVRE, RESERVADO,OCUPADO)
    despedida()
    return

###############################################
# Função "inicializaEstruturaDeDados()"
###############################################
def inicializaEstruturaDeDados(vetor,
                               numElementos, estadoInicial):
    for cMesa in range(0,numElementos,1):
        vetor.append(estadoInicial)
    return vetor



###############################################
# Função "inicializaEstruturaDeDados()"
###############################################
def cicloPrincipal(mesas,estadoLIVRE,
                   estadoRESERVADO, estadoOCUPADO):
    queroSair = False
    escolha = '\0'
    OPCAOINICIAL = 1
    OPCAOFINAL   = 5

    while not queroSair:
        mostraMenu(mesas, estadoOCUPADO)
        escolha = obtemEscolha(escolha,OPCAOINICIAL,
                               OPCAOFINAL)
        queroSair = processaEscolha(escolha,
                        OPCAOINICIAL, OPCAOFINAL,mesas,
                        estadoLIVRE,
                        estadoRESERVADO,
                        estadoOCUPADO, queroSair)
    return


###############################################
# Função "mostraMenu()"
###############################################
def mostraMenu(mesas, estadoOCUPADO):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("***********************************")
    print("*                                 *")
    print("*          Rest Gest              *")
    print("*                                 *")
    print("*      1. Listar mesas.           *")
    print("*      2. Reservar mesa.          *")
    print("*      3. Ocupar mesa.            *")
    print("*      4. Libertar mesa.          *")
    print("*      5. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()
    if (obtemNumMesasOcupadas(mesas, estadoOCUPADO)
            == len(mesas)):
        print("***********************************")
        print("*      RESTAURANTE CHEIO!!!!      *")
        print("***********************************")
    print()
    return

###############################################
# Função "obtemNumMesasOcupadas()"
###############################################
def obtemNumMesasOcupadas(mesas, estadoOCUPADO):
    numMesasOcupadas = 0
    for cMesa in range(0,len(mesas),1):
        if mesas[cMesa] == estadoOCUPADO:
            numMesasOcupadas += 1
    return numMesasOcupadas

###############################################
# Função "obtemEscolha()"
###############################################
def obtemEscolha(escolha,opcaoInicial, opcaoFinal):
    print("Qual é a sua escolha ("
          +str(opcaoInicial)+"-"
          +str(opcaoFinal)+") [1]? ",end="")
    escolha = input()
    if len(escolha) == 0:
        escolha = '1'
    else:
        escolha = escolha[0]
    return escolha

###############################################
# Função "processaEscolha()"
###############################################
def processaEscolha(escolha, opcaoInicial,opcaoFinal,
                    mesas, estadoLIVRE,
                        estadoRESERVADO,
                        estadoOCUPADO, queroSair):
    if escolha == '1':
        listarMesas(mesas, estadoLIVRE, estadoRESERVADO)
    elif escolha == '2':
        mesas = reservarMesa(mesas, estadoRESERVADO,
                             estadoOCUPADO)
    elif escolha == '3':
        mesas = ocuparMesa(mesas, estadoOCUPADO)
    elif escolha == '4':
        mesas = libertarMesa(mesas, estadoLIVRE)
    elif escolha == '5':
        queroSair = sairDoPrograma()
    else:
        escolhaInvalida(opcaoInicial,opcaoFinal)
    return queroSair

###############################################
# Função "listarMesas()"
###############################################
def listarMesas(mesas,estadoLIVRE,estadoRESERVADO):
    print("Listagem das Mesas")
    for cMesa in range(0,len(mesas),1):
        print("-> Mesa "+str(cMesa+1)+": ", end="")
        if mesas[cMesa] == estadoLIVRE:
            print("livre.")
        elif mesas[cMesa] == estadoRESERVADO:
            print("reservada.")
        else:
            print("ocupada.")
    pausa()
    return

###############################################
# Função "reservarMesa()"
###############################################
def reservarMesa(mesas, estadoRESERVADO, estadoOCUPADO):
    if (obtemNumMesasOcupadas(mesas,estadoOCUPADO) ==
       len(mesas)):
       print ("Restaurante cheio!")
    else:
        print("Qual a mesa a reservar (1-"
              +str(len(mesas))+")? ",end="")
        numMesa = input()
        teste1 = validaMesa(mesas, numMesa, estadoRESERVADO,
                      "reservada")
        teste2 = validaMesa(mesas, numMesa, estadoOCUPADO,
                       "ocupada")
        if  teste1 and teste2:
            numMesa = int(numMesa)
            mesas[numMesa-1] = estadoRESERVADO
            print("Mesa "
                 +str(numMesa) +
                  " reservada com sucesso!")
    pausa()
    return mesas


###############################################
# Função "ocuparMesa()"
###############################################
def ocuparMesa(mesas, estadoOCUPADO):
    if (obtemNumMesasOcupadas(mesas,estadoOCUPADO) ==
       len(mesas)):
       print ("Restaurante cheio!")
    else:
        print("Qual a mesa a ocupar (1-"
              + str(len(mesas)) + ")? ",end="")
        numMesa = input()
        if validaMesa(mesas, numMesa, estadoOCUPADO,
                      "ocupada"):
            numMesa = int(numMesa)
            mesas[numMesa - 1] = estadoOCUPADO
            print("Mesa "
                 +str(numMesa) +
                  " ocupada com sucesso!")
    pausa()
    return mesas

###############################################
# Função "validaMesa()"
###############################################
def validaMesa(mesas, numMesa, estadoValidar,
               estadoCadeia):
    if not numMesa.isdigit():
        print("Não inseriu um valor numérico!")
        return False
    else:
        numMesa = int(numMesa)
        if numMesa < 1 or numMesa > len(mesas):
            print("Mesa não existe!")
            return False
        else:
            if mesas[numMesa-1] == estadoValidar:
                print("Mesa "+str(numMesa)
                      +" já está "+estadoCadeia+".")
                return False
            else:
                return True

###############################################
# Função "libertarMesa()"
###############################################
def libertarMesa(mesas, estadoLIVRE):
    print("Qual a mesa a libertar (1-"
          + str(len(mesas)) + ")? ",end="")
    numMesa = input()
    if validaMesa(mesas, numMesa, estadoLIVRE,
                  "livre"):
        numMesa = int(numMesa)
        mesas[numMesa - 1] = estadoLIVRE
        print("Mesa "
             +str(numMesa) +
              " libertada com sucesso!")
    pausa()
    return mesas

###############################################
# Função "pausa()"
###############################################
def pausa():
    print("Prima qq tecla para continuar ... ", end="")
    input()
    return

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
def escolhaInvalida(opcaoInicial, opcaoFinal):
    print("Escolha inválida!")
    print("As escolhas vão de "
         +str(opcaoInicial)+" até "
         +str(opcaoFinal)+".")
    print("Prima ENTER para continuar ... ", end="")
    input()

################################################
# Função "despedida()"
################################################
def despedida():
    print("Obrigado por ter usado o programa!")
    return


##########################################
# Chamada à Função Principal
##########################################
if __name__ == "__main__":
     arranque()
     # main()