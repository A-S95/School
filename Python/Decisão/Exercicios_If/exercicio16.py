# Crie o codigo de um programa que apresenta uma pergunta de informatica no ecrã
# dando quatro hipoteses de resposta (pergunta de escolha múltipla).
# O programa deve ler a resposta do utilizador e indicar se o utilizador acertou ou errou.
mensagem = ""
resposta = 0

print("Escolha a opcao correta, entre estas 4 opcoes")
print("Qual o monitor tem maior Refresh Rate? ")
print(" A) 144Hz\n","B) 60Hz\n","C) 240Hz\n","D) 280Hz\n")
resposta = input()
print("A resposta que escolheu foi a ", resposta)

if resposta.lower() == "d":
    print("Acertou")
else:
    print("Errou, a resposta correta era a D)\n")