####################################################
# Capítulo 08 - Vetores Indexados
####################################################
####################################################
#
# Enunciado:
#
#     Faça um programa que apresente a média
#     de cinco números.
#
###################################################
# Solução
# 1. Dados
# 1.1 Quais são os dados do programa?
# 1.2 Classificação dos valores
#     Análise de Entradas/Saídas
#     Entrada(s): numeros[5] (float)
#     Saída(s): media        (float)
#
#######################################
# 1. Dados
# Declaração e Inicialização do Vetor
numeros = [0 for contaGaveta in range(0,5,1)]

# 2. Algoritmo
# 2.1 Obter entradas
for contaGaveta in range(0,5,1):
    print("Insira o número "+str(contaGaveta+1)+": ",end="")
    numeros[contaGaveta] = float(input())

# 2.2 Processar entradas
soma = 0

for contaGaveta in range(0,5,1):
    soma = soma + numeros[contaGaveta]
media = soma / 5

# 2.3 Apresentação da saída
print("Média: "+str(media)+".")


