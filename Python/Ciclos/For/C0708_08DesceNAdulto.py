####################################################
# Capítulo 07 - Estruturas de Ciclo
####################################################
#  - Ciclo de Contagem
####################################################
#
# Enunciado:
#
#  Faça uma programa que permita ao Robot
#  Optimus da Tesla, descer n degraus de uma calçada
#  portuguesa.
#  Versão: descer como adulto.
#####################################################

# 2. Algoritmo
# 2.1 Obter entradas
print()
print("Quantos degraus quer descer? ", end="")
numDegraus = int(input())

# 2.2 Processar entradas
# 2.3 Apresentar a saída

for contaDegrau in range(numDegraus,0,-2):
    print("Levantar o pé esquerdo e pousar no degrau ",contaDegrau,".")
    print("Levantar o pé direito  e pousar no degrau ",(contaDegrau-1),".\n")


if (numDegraus % 2 != 0):
    print("Levantar o pé esquerdo e pousar no degrau 0.")
else:
    print("Levantar o pé esquerdo e pousar no degrau 0.")
    print("Levantar o pé direito  e pousar no degrau 0.\n")
print()