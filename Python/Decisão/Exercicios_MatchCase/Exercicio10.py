# Digite o codigo de um programa que le dois numeros reais 
# e pergunta ao utilizador qual operacao a realizar dando quatro hipoteeses.
# Soma, subtracao, multiplicacao e divisao
# O programa deve apresentar o resultado da operacao escolhida.
num1 = 0
num2 = 0
resposta = 0


num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

while True:
    resposta = int(input("Qual operacao deseja realizar?\n1 - Soma\n2 - Subtracao\n3 - Multiplicacao\n4 - Divisao\n"))
    match resposta:
        case 1:
            soma = num1 + num2
            print("A soma do ", num1, "e ", num2, "= ", soma, "\n")
            continue
        case 2:
            subtracao = num1 - num2
            print("A subtracao do ", num1, "e ", num2, "= ", subtracao, "\n")
            continue
        case 3:
            multiplicacao = num1 * num2
            print("A multiplicacao do ", num1, "e ", num2, "= ", multiplicacao, "\n")
            continue
        case 4:
            divisao = num1 / num2
            print("A divisao do ", num1, "e ", num2, "= ", divisao, "\n")
            continue
        case _:
            print("Operacao Invalida")
            break
