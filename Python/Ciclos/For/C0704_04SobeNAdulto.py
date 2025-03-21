####################################################
# Capítulo 07 - Estruturas de Ciclo
####################################################
#  - Ciclo de Contagem
####################################################
#
# Enunciado:
#
#  Faça uma programa que permita ao Robot
#  Optimus da Tesla, subir n degraus de uma calçada
#  portuguesa.
#  Versão: subir como adulto.
#####################################################
# 3. Programas
# 3.1 Dados
# numDegraus = 0

# 3.2 Algoritmo
numDegraus = int(input("Quantos degraus deseja subir? "))

for contaDegrau in range(1, numDegraus + 1, 2):
    print("Levantar o pé esquerdo e pousar no degrau " + str(contaDegrau) + ".")
    
    if contaDegrau + 1 <= numDegraus:
        print("Levantar o pé direito e pousar no degrau " + str(contaDegrau + 1) + ".")
    else:
        print("Levantar o pé direito e pousar no degrau " + str(contaDegrau) + ".")
    
    print()

if numDegraus % 2 != 0:
    print("")
else:
    print("Levantar o pé esquerdo e pousar no degrau " + str(numDegraus) + ".")

print()
