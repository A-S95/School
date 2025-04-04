####################################################
#  Capítulo 09 - Dados Estruturados em Pyhton.
####################################################
###########################################################
# Exemplo 2
###########################################################
###########################################################
# Exemplo de uma Lista em Python
###########################################################
lista_vazia = []

cidades = []
print("0. Número de elementos da lista: ", end="")
print(len(cidades),".",end="\n")      # 0

print("1. Apresentação dos elementos da lista: ",end="\n")
print("a) Ciclo for")
for cElemento in range(0,len(cidades),1):
    print(cidades[cElemento]," ",end="")
print(".",end="\n")
print("b) Ciclo for para coleções")
for cidade in cidades:
    print(cidade, end="")
print("c) Impressão da lista")
print(cidades)
print(cidades.__str__())



print("2. Operações de Inserção:",end="\n")
print("2.1 Acrescentar um elemento no fim: 'append()'.")
cidades.append("Lisboa")     # Lisboa
cidades.append("Porto")      # Lisboa Porto
print("Número de elementos da lista: ", end="")
print(len(cidades),".",end="\n")   # 2
print("Apresentação dos elementos da lista: ",end="\n")
print("a) Ciclo for com a função range")
for cElemento in range(0,len(cidades),1):
    print(cidades[cElemento]," ",end="")  # Lisboa Porto
print(".",end="\n")
print("b) Impressão da lista")
print(cidades)                         # [´Lisboa´,´Porto´]
print(cidades.__str__())
print("c) Ciclo 'for' para coleções")
for elemento in cidades:
  print(elemento,end=" ")              # Lisboa Porto
print("\n")

print("2.2 Acrescentar um elemento numa posição: 'insert()'.")
cidades.insert(1,"Coimbra")
#  [´Lisboa´,'Coimbra',´Porto´]
print("Número de elementos da lista: ", end="")
print(len(cidades),".",end="\n")    # 3
print("Apresentação dos elementos da lista: ",end="\n")
print("a) Ciclo for")
for cElemento in range(0,len(cidades),1):
    print(cidades[cElemento]," ",end="")
print(".",end="\n")
print("b) Impressão da lista")
print(cidades)
print(cidades.__str__())

print("2.3 Acrescentar um elemento com substituição: [].")
cidades.append("Aveiro")
# [´Lisboa´,'Coimbra',´Porto´,'Aveiro']
print("Antes da substituição: ",end="")
print(cidades)
# [´Lisboa´,'Coimbra',´Porto´,'Aveiro']
print("Substituição da cidade de 'Aveiro' por 'Leiria'",end="\n")
cidades[cidades.index("Aveiro")] = "Leiria"
# [´Lisboa´,'Coimbra',´Porto´,'Leiria']
print("Depois da substituição: ",end="")
print(cidades)

print("2.4 Acrescentar um conjunto de elementos: 'extend()'.")
cidades2 =['Funchal','Ponta Delgada','Porto Santo']
print("Antes do acrescento: ",end="")
print(cidades)
cidades.extend(cidades2)
# [´Lisboa´,'Coimbra',´Porto´,'Leiria','Funchal','Ponta Delgada','Porto Santo']
print("Depois do acrescento: ",end="")
print(cidades)

print("3. Operações de Pesquisa:",end="\n")
cidades.append("Braga")
cidades.append("Faro")
cidades.append("braga")
cidades.append("Faro")
print(cidades)
print("3.1 Obter o elemento a partir do índice: [].",end="\n")
print("Qual é o terceiro elemento da lista? ",end="")
print(cidades[2],".",end="\n")

print("3.2 Obter o índice do elemento: index().",end="\n")
print("Obter é o índice de \"Braga\"? ",end="")
print(cidades.index("Braga"),".",end="\n")
print("3.3 Número de ocorrências de um elemento: cout().",end="\n")
print(cidades)
print("Quantas vezes aparece \"Faro\"? ",end="")
print(cidades.count("Faro"),".",end="\n")

print("4. Operações de Ordenação - Tabela ASCII:",end="\n")
print("Lista original: ",end="")
print(cidades)
print("4.1 Ordenação crescente: sort().",end="\n")
cidades.sort()
cidades_OrdC = cidades.copy()
print("Lista ordenada de forma crescente: ",end="\n")
print(cidades)
print(cidades_OrdC)
print("4.2 Ordenação decrescente: sort().",end="\n")
cidades.reverse()
cidades_OrdD = cidades.copy()
print("Lista ordenada de forma decrescente: ",end="\n")
print(cidades)
print(cidades_OrdD)

print("5. Operações de eliminação: ",end="\n")
print("Lista original: ",end="")
print(cidades)
print("5.1 Eliminação de um elemento por posição: pop().",end="\n")
print("Retirar o último elemento: ",end="\n")
cidades.pop()
print("Lista depois da eliminação: ",end="")
print(cidades)
print("Retirar o primeiro elemento: ",end="\n")
cidades.pop(0)
print("Lista depois da eliminação: ",end="")
print(cidades)
print("5.2 Eliminação de um elemento por valor: remove().",end="\n")
print("Retirar o elemento 'Faro': ",end="\n")
cidades.remove("Faro")
print("Lista depois da eliminação: ",end="")
print(cidades)
print("5.3 Eliminação de toda a lista: clear().",end="\n")
cidades.clear()
print("Lista depois da eliminação: ",end="")
print(cidades)




