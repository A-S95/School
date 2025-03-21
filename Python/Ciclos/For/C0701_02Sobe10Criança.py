#Numeros de 1 ate 10, variando de 1 em 1

print("Contagem decrescente de 1 ate 10:")

for contaDegraus in range(1,11,1):
    print(str(contaDegraus) + " ", end="")
print(".")

################################################

print("Contagem decrescente de 6 ate 15: de dois em dois")

for contaDegraus in range(6,15,2):
    print(" "+str(contaDegraus) + " ", end="")
print(".")
print()

#################################################

print("Contagem decrescente de 15 ate 6:")

for contaDegraus in range(15,5,-1):
    print(str(contaDegraus) + " ", end="")
print(".")

###################################################

print("Contagem decrescente de 15 ate 6: de dois em dois")

for contaDegraus in range(15,6,-2):
    print(str(contaDegraus) + " ", end="")
print(".")

#####################################################

print("Contagem decrescente de 1 ate 10: subindo de 1 em 1, termina no 6")

for contaDegraus in range(1,11,1):
    print(str(contaDegraus) + " ", end="")
    if contaDegraus == 6:
        break # para a execucao do loop
print(".")

######################################################


print("Contagem decrescente de 1 ate 10: subindo de 1 em 1, c excepcao ao 7")

for contaDegraus in range(1,11,1):
    print(str(contaDegraus) + " ", end="")
    if contaDegraus == 7:
        continue #passa para a proxima iteracao
    print(""+str(contaDegraus) + " ", end="")
print(".")
