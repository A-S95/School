# escreva um programa que faz a tabuada de um ate 10, de acordo com a escolha do utilizador.

#1(numEscolhido) x 1 = 1
#1(numEscolhido) x 2 = 2

# Entrada: Um numero inteiro de 1 a 10.

numEscolhido = int(input("Escolha um numero de 1 a 10: "))
contador = 1


while contador <= 10:
    resultado = numEscolhido * contador
    print(f"{numEscolhido} x {contador} = {resultado}") 
    contador += 1