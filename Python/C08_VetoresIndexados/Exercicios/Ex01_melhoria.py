# Despesa de Mercearia
# faca um programa que recebe ate cinco despesas efetuadas numa mercearia.
# Depois apresenta o total sem e com IVA.
# Melhore o programa de modo a que leia um numero qualquer
# de despesas, indicado pelo utilizador.

# Segundo exercicio, com a melhoria
numDespesa = int(input("Digite o numero de despesas totais que ira colocar: "))
despesa = []
iva = []

despesa = [0] * numDespesa
iva = [0] * numDespesa

for contaGaveta in range(numDespesa):
    print("Insira o número "+str(contaGaveta+1)+": ",end="")
    despesa[contaGaveta] = float(input())
    iva[contaGaveta] = despesa[contaGaveta] * (23 / 100)

# Calcula a soma das despesas e do IVA usando a função sum()
# soma = sum(despesa)
# total_iva = sum(iva)

# Calcula a soma das despesas e do IVA sem usar a função sum()
soma = 0
total_iva = 0
for i in range(numDespesa):
    soma += despesa[i]
    total_iva += iva[i]

# Calcula o total com IVA
total_com_iva = soma + total_iva

# Apresenta os resultados
print(f"Valor Base: {soma:.2f}€")
print(f"IVA (23%): {total_iva:.2f}€")
print(f"Valor Total: {total_com_iva:.2f}€")
    
