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
#
#####################################################

for contaDegrau in range(1,11,1):
    print("Levantar o pé esquerdo e pousar no degrau "
          + str(contaDegrau) +".")
    print("Levantar o pé direito e pousar no degrau "
          + str(contaDegrau) +".")
    print()