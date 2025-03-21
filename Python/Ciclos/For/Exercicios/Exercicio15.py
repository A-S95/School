#uma media entre um numero de notas indicados pelo utilizador
soma = 0.0
numNotas = int(input("Quantas notas deseja calcular a media? "))

for i in range(numNotas):
    notas = float(input(f"Digite a nota {i+1}: "))
    soma += notas

media = soma / numNotas

print("A media das notas introduzidas e: ", media)