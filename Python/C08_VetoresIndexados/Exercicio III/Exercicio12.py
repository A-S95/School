# VideoProjetores
# 4 projetores
# 10 salas

import os

# Dados
LIVRE = 'L'
OCUPADO = 'O'

NUMPROJETORES = 4
NUMSALAS = 10

queroSair = False

# Estado dos projetores: [projetor, sala]
projetores = [[LIVRE, 0] for _ in range(NUMPROJETORES)]

# 3.2.1 Ciclo principal do programa
while not queroSair:
    # 3.2.1.1 Apresentar menu de opções
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o ecrã
    print("")
    print("*********************************************")
    print("*                                           *")
    print("*     Gestão de Videoprojetores             *")
    print("*                                           *")
    print("*  1. Listar estado dos videoprojetores     *")
    print("*  2. Requisitar videoprojetor              *")
    print("*  3. Devolver videoprojetor                *")
    print("*  4. Sair do programa                      *")
    print("*                                           *")
    print("*********************************************")
    print()

    # 3.2.1.2 Obter escolha do utilizador
    print("Qual é a sua escolha (1-4) [1]? ", end="")
    escolha = input()
    if len(escolha) == 0:  # Fiz ENTER
        escolha = '1'
    else:
        escolha = escolha[0]

    # 3.2.1.3 Processar a escolha
    match escolha:
        case '1':  # Listar estado dos videoprojetores
            print("Estado dos Videoprojetores:")
            for cProjetor in range(0, len(projetores), 1):
                print("Videoprojetor "+str(cProjetor+1)+": ", end="")
                if projetores[cProjetor][0] == LIVRE:
                    print("livre.")
                else:
                    print("ocupado (Sala "+str(projetores[cProjetor][1])+").")
            print("Prima ENTER para continuar ... ", end="")
            input()

        case '2':  # Requisitar videoprojetor
            print("Requisitar Videoprojetor")
            print("Qual a sala a selecionar (1-"
                  + str(NUMSALAS) + ")? ", end="")
            numSala = input()

            if not numSala.isdigit():
                print("Não inseriu um valor numérico de sala!")
            else:  # O valor da sala é numérico.
                numSala = int(numSala)
                if numSala < 1 or numSala > NUMSALAS:
                    print("Valores inseridos fora da gama válida!")
                else:  # Valores válidos.
                    projetor_livre = None
                    for cProjetor in range(0, len(projetores), 1):
                        if projetores[cProjetor][0] == LIVRE:
                            projetor_livre = cProjetor
                            break
                    
                    if projetor_livre is not None:
                        projetores[projetor_livre] = [OCUPADO, numSala]
                        print("Videoprojetor "+str(projetor_livre+1)+" atribuído à Sala "+str(numSala)+".")
                    else:
                        print("Não há videoprojetores disponíveis no momento.") 
            print("Prima ENTER para continuar ... ", end="")
            input()

        case '3':  # Devolver videoprojetor
            print("Devolver Videoprojetor")
            print("Qual videoprojetor deseja devolver (1-"
                  + str(NUMPROJETORES) + ")? ", end="")
            numProjetor = input()

            if not numProjetor.isdigit():
                print("Não inseriu um valor numérico de videoprojetor!")
            else:  # O valor do videoprojetor é numérico.
                numProjetor = int(numProjetor)
                if numProjetor < 1 or numProjetor > NUMPROJETORES:
                    print("Valores inseridos fora da gama válida!")
                else:  # Valores válidos.
                    if projetores[numProjetor - 1][0] == LIVRE:
                        print("Este videoprojetor já está livre!")
                    else:  # Videoprojetor ocupado.
                        projetores[numProjetor - 1] = [LIVRE, 0]
                        print("Videoprojetor "+str(numProjetor)+" devolvido com sucesso.")
            
            print("Prima ENTER para continuar ... ", end="")
            input()

        case '4':  # Sair do programa
            print("Tem a certeza que quer sair (S/N) [N]? ", end="")
            resposta = input().upper()
            if resposta == "S":
                queroSair = True

        case _:  # Escolha inválida
            print("Escolha inválida!")
            print("As escolhas vão de 1 a 4.")
            input("Prima ENTER para continuar ... ")

# 3.2.2 Despedida
print("Obrigado por ter usado o programa!")