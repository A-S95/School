# Digite o codigo de um programa que le dois numeros reais 
# e pergunta ao utilizador qual operacao a realizar dando quatro hipoteeses.
# Soma, subtracao, multiplicacao e divisao
# O programa deve apresentar o resultado da operacao escolhida.
num1 = 0
num2 = 0

print("Insira o primeiro valor? ")
num1 = float(input())
print("Insira o segundo valor? ")
num2 = float(input())

print("Primeiro valor: ", num1)
print("Segundo valor: ", num2)

while True:
    resposta = int(input("Que calculo pretende fazer: 1 - Soma, 2 - Subtracao, 3 - Multiplicacao, 4 - Divisao, 5- Alterar Valores, 0 - para cancelar "))
    if resposta == 1:
        soma = num1 + num2
        print("A soma do ", num1, "e ", num2, "= ", soma, "\n")
        continue
    elif resposta == 2:
        subtracao = num1 - num2
        print("A subtracao do ", num1, "e ", num2, "= ", subtracao, "\n")
        continue
    elif resposta == 3:
        multiplicacao = num1 * num2
        print("A multiplicacao do ", num1, "e ", num2, "= ", multiplicacao, "\n")
        continue
    elif resposta == 4:
        divisao = num1 / num2
        print("A divisao do ", num1, "e ", num2, "= ", divisao, "\n")
        continue
    elif resposta == 5:
        num1 = float(input("Altere o primeiro valor: "))
        num2 = float(input("Altere o segundo valor: "))
    else:
        print("Operacao cancelada""\n")
        break
    