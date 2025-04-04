############################################################################
# EXEMPLO DE TUPLO
############################################################################
# Definição de um tuplo
# Elementos do tuplo: 'Livro 1' e 12.99
# Estrutura indexável:
# - É possivel aceder aos elementos de um tuplo através
#   de índices
#  t[0] -> 'Livro 1';  t[1] -> 12.99
#
t = ('Livro 1', 12.99)
print(t)

# Obter o valor do segundo elemento
# Devolve o erro "IndexError" para valores inválidos de índice
print(t[1])   # 12.99
#print(t[2])  # Erro IndexError: tuple index out of range
#print(t(2))  # Erro - Tuple is not callable
              #        Não é função.

# Obter o comprimento do tuplo
print(len(t))  # 2

# Obter o indice a partir do valor
# Se o valor nã o for encontrado devolve o erro
# "value error" "ValueError".
print(t.index('Livro 1')) # 0
# print(t.index('Livro 2')) - Value Error

# Conta o número de vezes que um valor aparece no tuplo.
print(t.count(12))  # 0
print(t.count('Livro 1'))  # 1
