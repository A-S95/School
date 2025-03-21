####################################################
# Capítulo 07 - Estruturas de Ciclo
####################################################
#  - Ciclo com condição: while
####################################################
#
# Enunciado:
#
#   Faça um programa que permita ao
#   ASIMO - HONDA / OPTIMUS - TESLA
#   aquecer um copo de café.
#
#####################################################
# Solução:
# 1. Dados
# 1.1 Quais são os dados do programa?
#     Análise de entradas-saída.
# 1.2 Classificação de dados
#     Entrada(s): tempAtual (float), tempPretendida (float)
#     Saída(s):   Evolução da temperatura do café.
#
# 2. Algoritmo
# 2.1 Obter entradas
# 2.2 Processar as entradas
# 2.3 Apresentar saída(s)
#####################################################
# 3. Programa

print("Qual é a temperatura pretendida (º.C)? ", end="")
tempPretendida = float(input())  # 60

print("Medindo a temperatura atual ... ", end="")
tempAtual = float(input())      # 40

while tempAtual < tempPretendida:
    print("Ligar o aquecedor durante 1 segundo!")
    tempAtual = tempAtual + 2    # 42 -> 60
    print("Temperatura atual: "+str(tempAtual)+".")

print("O seu café está pronto!")
