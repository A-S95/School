# Despesas mercearia
total_despesas = 0
contador = 1
iva = 23

while True:
    despesa = float(input(f"Insira o valor da despesa {contador} (ou 0 para terminar): "))
    
    if despesa == 0:
        break

    total_despesas += despesa
    contador += 1
    total_iva = total_despesas * iva/100



print(f"\nTotal de despesas inseridas: {contador - 1}")
print(f"Total gasto na mercearia sem IVA: {total_despesas:.2f} €")
print(f"Total de IVA na compra: {total_iva:.2f} €")
print(f"Total na mercearia com IVA: {total_despesas + total_iva:.2f}€")

