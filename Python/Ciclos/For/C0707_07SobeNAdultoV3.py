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


print("Este algoritmo irá permitir um robô subir um "
     +"determinado número de degraus.\n")

steps = int(input("Quantos degraus pretende subir? "))

for x in range(1, steps + 1):
    if x % 2 == 1:
        print(f"\nLevantar o pé esquerdo e pousar no degrau {str(x)}.")
        if x == steps:
            print(f"Levantar o pé direito e pousar no degrau {str(x)}.")
    else:
        print(f"Levantar o pé direito e pousar no degrau {str(x)}.")
        if x == steps:
            print(f"\nLevantar o pé esquerdo e pousar no degrau {str(x)}.")