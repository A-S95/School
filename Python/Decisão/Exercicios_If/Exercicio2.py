# Digite o codigo de um programa que recebe um numero inteiro 
# indicando se esse numero e par ou nao. 

mensagem = ""
num1 = 0

print("Coloque o numero que pretende saber se é par ou não: ", end="")
num1 = int(input())

if num1 % 2 == 0:
    mensagem = "Par"
else:
    mensagem = "Impar"

print(mensagem)