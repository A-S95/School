#######################################################
# Exemplo 1
#######################################################
# Para declarar "arrays" numéricos é preciso
# importar o módulo "array"
# https:#docs.python.org/3/library/array.html


# Importação de um módulo com atribuição de
# um nome alternativo ("alias")
import array as moduloArr

# a.1) Inicialização explícita:
# a.1.1) Utilização da Função array() do módulo

# Declaração de um vetor com 3 números reais ("d" - "double")
numerosD = moduloArr.array('d', [1.1, 3.5, 4.5])

# Apresentar todo o "array"
print(numerosD)

# Primeiro Elemento do "Array"
print("Primeiro elemento: "
      + str(numerosD[0]) + ".")
print("Segundo elemento: "
      + str(numerosD[1]) + ".")
print("Terceiro elemento: "
      + str(numerosD[2]) + ".")
# Acrescenta no fim
numerosD.append(5.6)
print(numerosD)
numerosD.append(1)
print(numerosD)
# Num Array todos os valores tem que ser do mesmo tipo
#numerosD.append('a')
#print(numerosD)
print("Número de elementos do 'array': "
     + str(len(numerosD)) + ".")
# Remove o primeiro elemento do "Array".
numerosD.remove(1.1)
print(numerosD)
print("Número de elementos do 'array': "
     + str(len(numerosD)) + ".")
# Acrescenta um determinado valor numa determinada posição
numerosD.insert(0,7.4)
print(numerosD)
print("Número de elementos do 'array': "
     + str(len(numerosD)) + ".")
# Remove o terceiro elemento
numerosD.pop(2)
print(numerosD)
print("Número de elementos do 'array': "
     + str(len(numerosD)) + ".")

# Operação de Inserção
# append               - insere no fim
# insert(index, valor) - Insere na poisção 'index' o 'valor'.

# Operação de Remoção
# pop(index)      - Remove o valor na posição 'index'.
# remove(valor)   - Remove o valor do "arrays"

numerosD.reverse()
print(numerosD)

ListaNumeros = numerosD.tolist()
print(ListaNumeros)

print("Ordena a lista de forma ascendente.")
ListaNumeros.sort()
print(ListaNumeros)
print("Ordena a lista de forma descendente.")
ListaNumeros.sort(reverse=True)
print(ListaNumeros)
# Numa lista os valores podem ser de tipos diferentes
ListaNumeros.append("a")
print(ListaNumeros)


