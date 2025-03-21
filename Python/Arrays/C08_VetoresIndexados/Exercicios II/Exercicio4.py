# Estatisticas de notas

# Recebe notas final de seis alunos.

# INSERCAO DE NOTAS
# LISTAR NOTAS
# APRESENTAR MEDIA
# APRESENTAR NOTA MAXIMA
# APRESENTAR NOTA MINIMA
# APAGAR NOTAS
# SAIR DO PROGRAMA.

import os

numNotas = 6
queroSair = False
soma = 0

notas = [0.0 for contaNotas in range(0,numNotas,1)]

while not queroSair:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("")
    print("***********************************")
    print("*                                 *")
    print("*             Parque Gest         *")
    print("*                                 *")
    print("*      A. Inserir Notas.          *")
    print("*      B. Listar Notas.           *")
    print("*      C. Apresentar Média.       *")
    print("*      D. Apresentar Máxima.      *")
    print("*      E. Apresentar Mínima.      *")
    print("*      F. Apagar Notas.           *")
    print("*      G. Apagar todas as Notas.  *")
    print("*      H. Sair do programa.       *")
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
        case 'A' | 'a': # Inserior Notas.
            print("Inserir "+str(numNotas) +" Notas: ", end="\n")   
            for notasValor in range(0, numNotas, 1):
                while True:
                    print("Insira Nota " +str(notasValor+1) +": ", end="")
                    nota = float(input())
                    if 0 <= nota <= 20:
                        notas[notasValor] = nota
                        print("Nota inserida com sucesso")
                        break
                    else:
                        print("Notas devem ser entre 0 e 20. Tente novamente.")
            input("Prima ENTER para continuar")

        case 'B' | 'b': # Listar notas.
            print("Listar Notas:"+str(numNotas), end="\n")
            for notasValor in range(0, numNotas, 1):
                print("Nota " +str(notasValor+1)+": ", end="")
                print(notas[notasValor], end="\n")
            input("Prima ENTER para continuar")

        case 'C' | 'c': # Apresentar media.
            for i in range(numNotas):
                soma += notas[i]

            media = soma / numNotas
            print("Apresentar Média: ", end="")
            print(media, end="\n")
            input("Prima ENTER para continuar")

        case 'D' | 'd': # Apresentar Maxima
            maxima = notas[0]
            for i in range(numNotas):
                if notas[i] > maxima:
                    maxima = notas[i]

            print("Apresentar Nota Máxima: ", end="")
            print(maxima, end="\n")
            input("Prima ENTER para continuar")

        case 'E' | 'e': # Apresentar Minima
            minima = notas[0]
            for i in range(numNotas):
                if notas[i] < minima:
                    minima = notas[i]

            print("Apresentar Nota Mínima: ", end="")
            print(minima, end="\n")
            input("Prima ENTER para continuar")

        case 'F' | 'f': # Apagar uma nota da Lista
            print(f"Apagar a nota referente ao número do aluno: (1 - {numNotas}) ", end="")
            resposta = int(input())
            if 1 <= resposta <= numNotas:
                notas[resposta - 1] = 0.0
                print("Nota do aluno", (resposta), "apagada com sucesso", end="\n")
            else:
                print("Número de aluno inválido. Deve ser entre 1 e ", (numNotas))
            input("Prima ENTER para continuar")

        case 'G' | 'g': # Apagar todas as notas
            print("Tem a certeza que quer apagar todas as notas (S/N)? ", end="")
            resposta = input()
            if resposta == "S" or resposta == "s":
                print("Todas as notas foram apagadas com sucesso", end="")
                notas = [0.0 for contaNotas in range(0,numNotas,1)]
                print("Notas apagadas com sucesso")
                input("Prima ENTER para continuar")
            else:
                print("Erro a apagar as notas")

        case 'H' | 'h': # Sair do Programa.
            print("Tem a certeza que quer sair (S/N)? ", end="")
            resposta = input()
            if resposta == "S" or resposta == "s":
                print("Programa terminado.")
                queroSair = True
            else:
                print("Programa continuará")
            input("Prima ENTER para continuar")
