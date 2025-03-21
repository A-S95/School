###################################################
#  Capitulo 06 - Estruturas de Decisão
###################################################
#           Instrução Condicional
#
#  Enunciado/Problema:
#
#    Faça um programa que recebe a nota final de um
#  modulo ou UFCD e diz se o formando está validado
#    
#   Versao 2: Validação da entrada.
#
#   notaFinal < 0 - "Nota invalida, Numero negativo"
#   0 <= notaFinal <= 9.5 - "nao validado"
#   9.5 <= notaFinal <= 20 - "Validado"
#   notaFinal > 20 - "Nota invalida, Numero superior a 20"
#
####################################################
# Solução:
# 1. Dados
# 1.1 Quais são os dados do programa?
#     Análise de Entradas/Saídas
#           -Entrada(s): notaFinal
#
#           -Saida(s): mensagem(Validado/Invalidado)
#
# 1.2 Classificação dos dados
#
#       notaFinal - variavel numérica decimal (float)
#       mensagem - variavel alfanumérica 
#                    *cadeira de caracteres (string)
#
#
#######################################################
# 2. Algoritmo
#
# 2.1 Obter entradas
#
#    - Obter a notaFinal obtida à UFCD a partir do 
#      teclado
#      
#    - Obter o segundo número a partir do teclado
#      e atribuir esse valor à variável "num2".
#
# 2.2 Processamento das entradas
#
#      
#
# 2.3 Apresentação da(s) saída(s)
#
#     Apresentar a mensagem se validado ou não.
#
#####################################################
# 3. Programa

# 3.1 Dados
notaFinal = 0
mensagem = ""

# 3.2 Algoritmo
# 3.2.1 Obter entradas
print("Qual foi a sua Nota Final na UFCD", end="")
notaFinal = float(input())

# 3.2.2 Processamento das entradas
# Com melhor performance
if notaFinal >= 9.5 and notaFinal < 20:
    mensagem = "Validado"
elif notaFinal == 0 and notaFinal < 9.5:
    mensagem = "Nao validado"
else:
    mensagem = "Nota invalida, numero invalido"

# 3.2.3 Apresentação da saída
print(mensagem)



