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


###########################################
# Exemplo 01 - Números de 1 até 10,
#              variando de 1 em 1.
#############################################
print("01. Números de 1 até 10, variando de 1 em 1:",
      end="")
for contaDegrau in range(1,11,1):
    print(" "+str(contaDegrau), end="")
print(".")
print()

###########################################
# Exemplo 02 - Números de 6 até 15,
#              variando de 2 em 2.
#############################################
print("02. Números de 6 até 15, variando de 2 em 2:",
      end="")
for contaDegrau in range(6,16,2):
    print(" "+str(contaDegrau), end="")
print(".")
print()

###########################################
# Exemplo 03 - Números de 15 até 6,
#              decrescendo de 1 em 1.
#############################################
print("03. Números de 15 até 6, decrescendo de 1 em 1:",
      end="")
for contaDegrau in range(15,5,-1):
    print(" "+str(contaDegrau), end="")
print(".")
print()


###########################################
# Exemplo 04- Números de 15 até 6,
#              decrescendo de 2 em 2.
#############################################
print("04. Números de 15 até 6, decrescendo de 2 em 2:",
      end="")
for contaDegrau in range(15,5,-2):
    print(" "+str(contaDegrau), end="")
print(".")
print()

###########################################
# Exemplo 05- Números de 1 até 10,
#             subindo de 1 em 1,
#             mas terminando no 6.
#############################################
print("05. Números de 1 até 10, subindo de 1 em 1,"
      + " terminando no 6:",
      end="")
for contaDegrau in range(1,11,1):
    print(" "+str(contaDegrau), end="")
    if contaDegrau == 6:
        break
print(".")
print()

###########################################
# Exemplo 06- Números de 1 até 10,
#             subindo de 1 em 1,
#             com excepção do 7.
#############################################
print("06. Números de 1 até 10, subindo de 1 em 1,"
      + " com excepção do 7:",
      end="")
for contaDegrau in range(1,11,1):
    if contaDegrau == 7:
        continue  # Passa para a próxima iteração.
    print(" "+str(contaDegrau), end="")

print(".")
print()