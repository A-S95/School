###################################################
#  Primeiro Programa
###################################################
#
#  Enunciado/Problema:
#
#    Faça um programa que apresenta a soma de dois
#    números.
#
####################################################
# Solução:
# 1. Dados
# 1.1 Quais são os dados do programa?
#     Análise de Entradas/Saídas
#
#                 +-----------+
#       num1 ---->|           |
#       num2 ---->|           | --> soma
#                 |           |
#                 |           |
#                 +-----------+
#
# 1.2 Classificação dos dados
#
#     num1 - Dado não literal variável numérica decimal
#            (float).
#     num2 - Dado não literal variável numérica decimal
#            (float).
#     soma - Dado não literal variável numérica decimal
#            (float).
#
#######################################################
# 2. Algoritmo
#
# 2.1 Obter entradas
#
#    - Obter o primeiro número a partir do teclado
#      e atribuir esse valor à variável "num1".
#    - Obter o segundo número a partir do teclado
#      e atribuir esse valor à variável "num2".
#
# 2.2 Processamento das entradas
#
#     Somar os dois números e atribuir o resultado
#     à variável "soma".
#
# 2.3 Apresentação da(s) saída(s)
#
#     Apresentar o valor da soma no monitor.
#
#####################################################
# 3. Programa

# 3.1 Dados
num1 = 0.0
num2 = 0.0
soma = 0.0

# 3.2 Algoritmo
# 3.2.1 Obter entradas
print("Insira o primeiro número: ",end="\n")
num1 = float(input())

print("Insira o segundo número: ",end="\n")
num2 = float(input())

# 3.2.2 Processamento das entradas
soma = num1 + num2

# 3.2.3 Apresentação da saída
print("Soma: "+str(soma)+".")

