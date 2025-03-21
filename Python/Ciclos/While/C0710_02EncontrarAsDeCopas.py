####################################################
# Capítulo 07 - Estruturas de Ciclo
####################################################
#  - Ciclo com condicao: While
####################################################
#
# Enunciado:
#
#  Faca um programa que permita ao Robot ASIMO - HONDA 
#  Encontrar uma carta num baralho de cartas
#  Adaptacao : para qualquer carta
#
#####################################################
# Solucao
# 1. Dados
# 1.1 Quais são os dados do programa?
#   Analise de entradas-saidas.
#   - Entrada: cartaProcurada (string), cartaRetirada(string)
#   - Saida: Evolucao do retirar carta a carta
#   ate encontrar a carta procurada
#
#2. Algoritmo
#2.1 Obter entradas
#2.2 Processar as entradas
#2.3 Apresentar saida(s)
####################################################

# 3 programa

cartaProcurada = input("Qual a carta que procurar?", end="")

print("Retirar uma carta do baralho...", end=""  )

cartaRetirada = input()

while cartaRetirada != cartaProcurada:
    print("Retirar uma carta do baralho...")
    cartaRetirada = input()

print("Yahoo! Carta encontrada!")