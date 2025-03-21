# Digite o codigo de um programa que recebe um numero inteiro 
# indicando se esse numero e par ou nao. 

mensagem = ""
resposta = 0

print("Coloque o numero que pretende saber se é par ou não: ", end="")
resposta = int(input())


match resposta % 2 == 0:
    case 1:
        mensagem = "Par"
    case _:
        mensagem = "Impar"

print(mensagem)