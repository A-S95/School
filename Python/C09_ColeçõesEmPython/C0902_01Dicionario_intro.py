###########################################################
# Exemplo de um Dicionário em Python
###########################################################
# Definição de um dicionário
# d -> Variável que representa o dicionário
# 'nome', 'idade' -> chaves ou "keys" ou campos ou atributos
# 'Maria' e 10 -> são valores
#
d = {'nome': 'Maria', 'idade': 35}
# Imprimir o dicionário
print(d)


# Devolve o valor da chave ou associado à chave "nome".
print(d['nome'])  # Maria

# Devolve o comprimento do dicionario
print(len(d))  # 2

# Devolve a lista iterável de chaves
print(d.keys())  # dict_keys(['nome', 'idade'])

# Devolve a lista de valores (iteravel)
print(d.values()) # dict_values(['Maria', 35])

# Devolve os pares: chave - valor numa lista de Tuplos/Tuplas
print(d.items())
# dict_items([('nome', 'Maria'), ('age', 35)])

# Apaga o par chave-valor da idade
del d['idade']
# Imprimir o dicionário
print(d)   # {'nome': 'Maria'}


###############################################
# Acrescenta um novo par "chave-valor"
###############################################
d["Localidade"] = "Lisboa"
# Imprimir o dicionário
print(d)