#UM Numero de despesas indicado pelo utilizador e respectivo IVA, soma do total gasto.
totalgasto = 0
iva = 23

for despesas in range(1):
    despesas = float(input("Insira o valor total das despesas: "))
    totalgasto = despesas + despesas * iva/100
    print("O total gasto com despesas e IVA e: ", totalgasto, "euros")
    print("O total gasto com despesas e sem Iva e : ", despesas, "euros")
    print("O total de IVA e: ", despesas * iva/100, "euros")
