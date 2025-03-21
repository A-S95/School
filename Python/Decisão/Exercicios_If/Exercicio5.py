# Digite um codigo de um programa que recebe dois numeros e apresenta
# o menor deles. 
num1 = 0
num2 = 0


print("Insira o primeiro número: ",end="\n")
num1 = (input())
print("Insira o segundo número: ",end="\n")
num2 = (input())

print("Os valores escolhidos foram ", num1, " e ", num2)

if num1 < num2:
    print("Numero 1 é menor que numero 2 >>>>>> ", num1, ">", num2)
else:
    print("Numero 2 é menor que numero 1 >>>>>> ", num2, ">", num1)