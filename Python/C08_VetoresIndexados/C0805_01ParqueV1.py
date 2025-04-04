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

# 3.1 Dados
NUMLUGARES = 7
LIVRE = 0
OCUPADO = 1
queroSair = False

# 3.2 Algoritmo
# 3.2.0 Inicialização das Estrutura de Dados
lugares = [LIVRE for contaLugar in range(0,NUMLUGARES,1)]

# 3.2.1 Ciclo principal do programa.
while not queroSair:
    # 3.2.1.0 Apresentar o menu
    os.system('cls' if os.name == 'nt' else 'clear')
    # Limpa o ecrã
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
    # 3.2.1.1 Obter escolha do utilizador
    print("Qual é a sua escolha (A-D)? ",end="")
    escolha = input()

    # 3.2.1.2 Processar a escolha
    match escolha:
        case 'A' | 'a': # Listagem de lugares.
           print("Listagem de Lugares:")
           for contaLugar in range(0,NUMLUGARES,1):
               print("-> Lugar "+str(contaLugar+1)+": ",end="")
               if lugares[contaLugar] == LIVRE:
                   print("livre.")
               else:
                   print("ocupado.")
           print("Prima ENTER para continuar ... ", end="")
           input()
        case 'B' | 'b': # Marcar lugar.
            print("Qual o lugar a ocupar (1-"
                  +str(NUMLUGARES)+"? ", end="")
            numLugar = int(input())
            if numLugar < 1 or numLugar > NUMLUGARES:
                print("Lugar inválido!")
                print("Os lugares vão de 1 a "
                      +str(NUMLUGARES)+".")
            else: # Lugar é valido.
                if lugares[numLugar-1] == OCUPADO:
                    print("O lugar já está ocupado!")
                else: # Lugar válido e livre.
                    lugares[numLugar-1] = OCUPADO
                    print("Lugar ocupado com sucesso!")
            print("Prima ENTER para continuar ... ",end="")
            input()
        case 'C' | 'c': # libertar lugar.
            print("Qual o lugar a libertar (1-"
                  + str(NUMLUGARES) + "? ", end="")
            numLugar = int(input())
            if numLugar < 1 or numLugar > NUMLUGARES:
                print("Lugar inválido!")
                print("Os lugares vão de 1 a "
                      + str(NUMLUGARES) + ".")
            else:  # Lugar é valido.
                if lugares[numLugar - 1] == LIVRE:
                    print("O lugar já está livre!")
                else:  # Lugar válido e ocupado.
                    lugares[numLugar - 1] = LIVRE
                    print("Lugar libertado com sucesso!")
            print("Prima ENTER para continuar ... ",end="")
            input()
        case 'D' | 'd': # Sair do Programa.
            print("Tem a certeza que quer sair (S/N)? ", end="")
            resposta = input()
            if resposta == "S" or resposta == "s":
                queroSair = True
        case _ : # Escolha inválida
            print("Escolha inválida!")
            print("As escolhas vão de A a D.")
            print("Prima ENTER para continuar ... ",end="")
            input()

# 3.2.2 Despedida
print("Obrigado por ter usado o programa!")


