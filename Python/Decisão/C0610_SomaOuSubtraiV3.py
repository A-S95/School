###################################################
#  Capitulo 06 - Estruturas de Decisão
###################################################
#           Instrução de Selecção
#
#  Enunciado/Problema:
#
#    Faça um programa que recebe dois numeros e apresenta 
#   o resultado de uma operacao escolhida pelo utilizador:
#   Soma ou Subtração
#  
####################################################
# Solução:
# 1. Dados
# 1.1 Quais são os dados do programa?
#     Análise de Entradas/Saídas
#           -Entrada(s): num1, num2, opcao
#
#           -Saida(s): resultado
#
#
# 1.2 Classificação dos dados
#
#       num1 - variavel numérica decimal (float)
#       num2 - variavel numérica decimal (float)
#       op - (char).
#       resultado - variavel alfanumérica (float)
#
#
#######################################################
# 2. Algoritmo
#
# 2.1 Obter entradas
#
#    - Obter o numero 1 obtida do teclado 
#    - Obter o numero 2 obtida do teclado 
#    - Dar a escolher a opção ao utilizador
#    - Resultado
#
# 2.2 Processamento das entradas
#
#     
#        
#     
#        
#
# 2.3 Apresentação da(s) saída(s)
#
#     
#
#####################################################
# 3. Programa
# 3.1 Dados

num1 = 0.0
num2 = 0.0
op = '\0'
resultado = 0.0

# 3.2 Algoritmo
# 3.2.1 Obter entradas

#print("Ïnsira o primeiro operando: ", end="")
#num1 = float(input())
#print("Ïnsira o segundo operando: ", end="")
#num2 = float(input())

num1 = float(input("Insira o primeiro operando: "))
num2 = float(input("Insira o primeiro operando: "))

print("Qual a operacao a efetuar (+/-)? ", end="")
op = input()
# Capta o primeiro caracter da cadeia lida.
op = op[0]

# 3.2.2 Processamento das entradas

match op:
    case '+':
        resultado = num1 + num2
        print("resultado: "+str(resultado)+ ".")
    case '-':
        resultado = num1 - num2
        print("resultado: "+str(resultado)+ ".")
    case _:
        print("Operador Invalido")

# 3.2.3 Apresentação da saída
print()