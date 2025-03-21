# Digite o codigo de um programa que:
# - Apresenta uma afirmacao na area da informatica. 
# Pede ao utilizador que indique se essa afirmacao
# e verdadeira ou falsa, atraves dos caracteres V e F.
# Apresenta no monitor acertou ou errou

mensagem = ""
resposta = 0

print("Responda apenas com V ou F à seguinte questao")

resposta = input("É verdade que o processador só faz calculos? ")

match resposta:
    case "V", "v":
        print("Acertou")
    case "F", "f":
        print("Errou")
    case _:
        print("Resposta invalida")