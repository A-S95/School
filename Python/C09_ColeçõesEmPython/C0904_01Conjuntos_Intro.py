############################################################################
# EXEMPLO DE SET
############################################################################
# Definição de dois conjuntos ou "sets"
# - em extensão ( através dos seus elementos)

s1 = {10, 20, 12}
s2 = {100, 21, 12, 35, 40}

# Imprimir os conjuntos
print("Apresentação dos conjuntos: ")
print("s1: "+str(s1))
print("s2:", s2)
print()


# Obtém o número de elementos de um conjunto
print("Número de elementos do conjunto 's2': ", end ="")
print(len(s2))  # 5
print()

# Adiciona um elemento a um conjunto.
# Se o elemento já existe, operação é ignorada.
print("Adição de elemento '21' ao cojunto 's1':")
s1.add(21)
print(s1)
print()

# Atualiza os elementos de um conjunto.
# Acrescento de elementos
print("Atualização do conjunto 's1' com novos elementos: ")
s1.update({33, 30})
print(s1)
print()

# Remove um  elemento de um conjunto
# Gera uma excepção do tipo "KeyError"
# se remover um elemento que não existe.
print("Remoção do valor '33' do conjunto 's1': ")
s1.remove(33)
print(s1)
print()

# Reunião de dois Conjuntos (U)
print("s1: "+str(s1))
print("s2:", s2)
print("Reunião de dois conjuntos: ")
print(s1.union(s2))  # {33, 35, 100, 40, 10, 12, 20, 21, 30}
print("s1: "+str(s1))
print()

# Interseção de dois conjuntos
# - Apresenta os elementos comuns.
print("s1: "+str(s1))
print("s2:", s2)
print("Interseção de dois conjuntos: ")
print(s1.intersection(s2))   # {12, 21}
print("s1: "+str(s1))
print()