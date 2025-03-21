# Media de um conjunto de numeros
soma = 0
contador = 0
numero = float(input("Insira um número (ou -1 para terminar): "))

while numero != -1:
    soma += numero
    contador += 1
    numero = float(input("Insira um número (ou -1 para terminar): "))

if contador > 0:
    media = soma / contador
    print(f"A média dos {contador} números inseridos é: {media:.2f}")
else:
    print("Nenhum número foi inserido.")
    