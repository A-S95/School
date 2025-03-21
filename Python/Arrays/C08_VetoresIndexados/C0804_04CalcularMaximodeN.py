####################################################
# Capítulo 08 - Vetores Indexados
####################################################
# O que e um vetor ou array
# Um vetor ou array e um agrupamento de 
# valores do mesmo tipo.
#
# "array" -> array.array()
# "array" -> lista - array dinamico.
#           -> Uma lista em Python pode ter valores de tipos diferentes.
#           -> Nas outras linguagens, a lista deve ter valores do mesmo tipo.
#           -> C - malloc
#           -> C++ - <vector> - array dinamico.
#           -> Java - ArrayList
#           -> C# - List
#
####################################################
####################################################
####################################################
#
# Enunciado:
#
#     Faça um programa que apresente o valor maximo de
#     um conjunto de N numeros.
#
###################################################
# Solução
# 1. Dados
# 1.1 Quais são os dados do programa?
# 1.2 Classificação dos valores
#     Análise de Entradas/Saídas
#     Entrada(s): numeros[N] (float)
#     Saída(s): maximo       (float)
#
#######################################
# 1. Dados
# Declaração e Inicialização do Vetor
print("Quantos valores quer inserir? ", end="")
numValores = int(input())
numeros = [0 for contaGaveta in range(0,numValores,1)]

# 2. Algoritmo
# 2.1 Obter entradas
for contaGaveta in range(0,numValores,1):
    print("Insira o número "+str(contaGaveta+1)+": ",end="")
    numeros[contaGaveta] = float(input())

# 2.2 Processar entradas
maximo = numeros[0]

for contaGaveta in range(1,numValores,1):
    if numeros[contaGaveta] > maximo:
        maximo = numeros[contaGaveta]

# 2.3 Apresentação da saída
print("Maximo: "+str(maximo)+".")