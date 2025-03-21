# Recebe a nota final de um aluno e classifica a nota

notaFinal = 0

notaFinal = int(input("Insira o valor da Nota Final: (1 a 5)"))
if notaFinal == 3:
    print("Satisfaz")
elif notaFinal == 2:
    print("Insuficiente")
elif notaFinal == 4:
    print("Bom")
elif notaFinal == 5:
    print("Excelente")
elif notaFinal == 1:
    print("Mau")
else:
    print("Erro, nota invalida.")
