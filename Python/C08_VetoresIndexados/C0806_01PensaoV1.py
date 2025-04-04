####################################################
# Capítulo 08 - Vetores Indexados
####################################################
####################################################
# PROBLEMA:
#
#   Faça um programa que gere uma pensão com
#    três andares e sete quartos por andar.
#
#   Pretende-se, nesta versão, apenas considerar
#   o estado de cada quarto.
#
#   O Programa deve apresentar o seguinte menu:
#
#    - Listar quartos
#    - Reservar quarto
#    - Check-in
#    - Check-out
#    - Sair do programa
#
########################################################
# Solução:
# 1.  Dados:
# 1.1 Quais são os dados do programa?
# 1.2 Classificação dos dados
#     Entrada(s): escolha (char) ,
#                 numAndar (int), numQuarto (int)
#                 resposta (char)
#     Saída(s):
#       - Listagem do estado de cada quarto.
#       - Mensagens de resposta
#
########################################################
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
# Estados de cada quarto
LIVRE = 'L'
RESERVADO = 'R'
OCUPADO = 'O'

NUMANDARES = 3
NUMQUARTOSPORANDAR = 7

queroSair = False

# 3.2 Algoritmo
#
# 3.2.0 Inicialização das Estrutura de Dados
quartos =[ [LIVRE for cQuarto in range(0,NUMQUARTOSPORANDAR,1)]
             for cAndar in range(0,NUMANDARES,1)
         ]

# 3.2.1 Ciclo principal do programa
while(not queroSair):
    # 3.2.1.1 Apresentar menu de opções
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o ecrã
    print("")
    print("***********************************")
    print("*                                 *")
    print("*       Pensão Meireles           *")
    print("*                                 *")
    print("*      1. Listar quartos.         *")
    print("*      2. Reservar quarto.        *")
    print("*      3. Ocupar quarto.          *")
    print("*      4. Libertar quarto.        *")
    print("*      5. Sair do programa.       *")
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
        case '1':  # Listagem dos quartos
            print("Listagem de quartos: ")
            for cAndar in range (0,NUMANDARES,1):
                print("Andar "+str(cAndar+1)+": ")
                for cQuarto in range (0,NUMQUARTOSPORANDAR,1):
                    print("-> Quarto "+str(cAndar+1)+".0"
                          +str(cQuarto+1)+": ",end="")
                    if quartos[cAndar][cQuarto] == LIVRE:
                        print("livre.")
                    elif quartos[cAndar][cQuarto] == RESERVADO:
                        print("reservado.")
                    else:
                        print("ocupado.")
                print("Prima ENTER para continuar ... ", end="")
                input()
        case '2':  # Reservar quarto
            print("Reserva de Quarto")
            print("Qual o andar a selecionar (1-"
                  +str(NUMANDARES)+")? ", end="")
            numAndar = input()
            print("Nesse andar, qual é o quarto a reservar (1-"
                  +str(NUMQUARTOSPORANDAR)+")? ", end= "")
            numQuarto = input()

            if not numAndar.isdigit() or not numQuarto.isdigit():
                print("Não inseriu um valor numérico de andar ou quarto!")
            else: # Os valores de andar e quarto são numéricos.
                numAndar = int(numAndar)
                numQuarto = int(numQuarto)
                if (numAndar < 1 or numAndar > NUMANDARES
                    or numQuarto < 1 or numQuarto > NUMQUARTOSPORANDAR):
                    print("Valores inseridos fora da gama válida!")
                else: # Valores válidos.
                    if quartos[numAndar-1][numQuarto-1] != LIVRE:
                        print("O quarto não está livre!")
                    else: # Quarto livre.
                        quartos[numAndar-1][numQuarto-1] = RESERVADO
                        print("Quarto reservado com sucesso!")
            print("Prima ENTER para continuar ... ", end="")
            input()
        case '3':  # Check-in
            print("Check-in")
            print("Qual o andar a selecionar (1-"
                  + str(NUMANDARES) + ")? ", end="")
            numAndar = input()
            print("Nesse andar, qual é o quarto a ocupar (1-"
                  + str(NUMQUARTOSPORANDAR) + ")? ", end="")
            numQuarto = input()

            if not numAndar.isdigit() or not numQuarto.isdigit():
                print("Não inseriu um valor numérico de andar ou quarto!")
            else:  # Os valores de andar e quarto são numéricos.
                numAndar = int(numAndar)
                numQuarto = int(numQuarto)
                if (numAndar < 1 or numAndar > NUMANDARES
                        or numQuarto < 1 or numQuarto > NUMQUARTOSPORANDAR):
                    print("Valores inseridos fora da gama válida!")
                else:  # Valores válidos.
                    if quartos[numAndar - 1][numQuarto - 1] == OCUPADO:
                        print("O quarto já está ocupado!")
                    else:  # Quarto livre ou reservado.
                        quartos[numAndar - 1][numQuarto - 1] = OCUPADO
                        print("Quarto ocupado com sucesso!")
            print("Prima ENTER para continuar ... ", end="")
            input()
        case '4':  # Check-out
            print("Check-out")
            print("Qual o andar a selecionar (1-"
                  + str(NUMANDARES) + ")? ", end="")
            numAndar = input()
            print("Nesse andar, qual é o quarto a libertar (1-"
                  + str(NUMQUARTOSPORANDAR) + ")? ", end="")
            numQuarto = input()

            if not numAndar.isdigit() or not numQuarto.isdigit():
                print("Não inseriu um valor numérico de andar ou quarto!")
            else:  # Os valores de andar e quarto são numéricos.
                numAndar = int(numAndar)
                numQuarto = int(numQuarto)
                if (numAndar < 1 or numAndar > NUMANDARES
                        or numQuarto < 1 or numQuarto > NUMQUARTOSPORANDAR):
                    print("Valores inseridos fora da gama válida!")
                else:  # Valores válidos.
                    if quartos[numAndar - 1][numQuarto - 1] == LIVRE:
                        print("O quarto já está livre!")
                    else:  # Quarto livre ou reservado.
                        quartos[numAndar - 1][numQuarto - 1] = LIVRE
                        print("Quarto libertado com sucesso!")
            print("Prima ENTER para continuar ... ", end="")
            input()
        case '5':
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








