###################################################
#  Capitulo 06 - Estruturas de Decisão
###################################################
#           Instrução de Selecção
#
#  Enunciado/Problema:
#
#    Faça um programa que :
#   - Apresenta uma afirmacao no ecra:
#   - Pede ao utilizador para indicar se essa
#   Afirmacao e verdadeira ou falsa. 
#   - Com base na resposta do Utilizador apresenta uma 
#   mensagem de classificacao:
#   
#   
#  
####################################################
# Solução:
# 1. Dados
# 1.1 Quais são os dados do programa?
#     Análise de Entradas/Saídas
#           -Entrada(s): resposta, 
#
#           -Saida(s): mensagem:
#                       "Parabens acertou"
#                       "Errou"
#                       "Resposta Invalida"
#
#
# 1.2 Classificação dos dados
#
#       resposta (char)
#       mensagem (str)     
#
#######################################################
# 2. Algoritmo
#
# 2.1 Obter entradas
#
# 2.2 Processamento das entradas
#       
#
# 2.3 Apresentação da(s) saída(s)
#    
#
#####################################################
# 3. Programa
# 3.1 Dados

# '\0' - caractere nulo
resposta = '\0'
mensagem = ""

# 3.2 Algoritmo
# 3.2.1 Obter entradas

print("O criador da linguagem Python foi Guido van Rossum! ")
print("Verdadeiro ou Falso? (V/F) ", end="")
resposta = input()
resposta = resposta[0]

# 3.2.2 Processamento das entradas

if resposta == 'v' or resposta == 'V':
    mensagem = "Parabens acertou"
elif resposta.upper == 'f' or resposta == 'F':
    mensagem ="Errou"
else:
    mensagem = "Resposta invalida"

# 3.2.3 Apresentação da saída
print(mensagem)
print()