####################################################
# Capítulo 07 - Estruturas de Ciclo
####################################################
#  - Ciclo de Contagem
####################################################
#
# Enunciado:
#
#  Faça uma programa que permita ao Robot
#  Optimus da Tesla, subir 10 degraus de uma calçada
#  portuguesa.
#  Versão: subir como adulto.
#####################################################

for contaDegrau in range(1,11,2):
    print("Levantar o pé esquerdo e pousar no degrau "
          + str(contaDegrau) +".")   # 1  3  5  7  9
    print("Levantar o pé direito e pousar no degrau "
          + str(contaDegrau+1) +".")  # 2  4  6  8 10
    print()
print("Levantar o pé esquerdo e pousar no degrau 10.")