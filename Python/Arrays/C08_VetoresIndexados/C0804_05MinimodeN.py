####################################################
# Capítulo 08 - Vetores Indexados
####################################################
# O que é um vetor ou "array"?
# Um vetor ou "array" é um agrupamento de valores
# todos do mesmo tipo.
#
# "array" -> array.array()
# "array" -> lista - array dinâmico
#            - Uma lista em Python pode ter valores
#            de tipos diferentes.
#            - Nas outras linguagens, a lista deve
#            ter elementos do mesmo tipo:
#            C - malloc
#            C++ -> <vector> - array dinâmico
#            Java -> ArrayList
#            C#   -> List
#####################################################
#
# Enunciado:
#
#     Faça um programa que apresente o valor mínimo
#     de um conjunto de n números.
#
###################################################
# Solução
# 1. Dados
# 1.1 Quais são os dados do programa?
# 1.2 Classificação dos valores
#     Análise de Entradas/Saídas
#     Entrada(s): numeros[n] (float)
#     Saída(s): minimo       (float)
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

# 2.2 Processamento das entradas
minimo = numeros[0]
for contaGaveta in range(1,numValores,1):
    if numeros[contaGaveta] < minimo:
        minimo = numeros[contaGaveta]

# 2.3 Apresentação da saída
#     "+" - Operador de concatenação de
#     de "Strings"
print("Mínimo: "+str(minimo)+".")