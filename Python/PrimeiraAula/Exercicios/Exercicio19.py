peso = (float(input("Informe o peso em kilos: ")))
altura = (float(input("Informe a altura em metros: ")))

imc = peso / (altura ** 2)

print(f"O IMC é: {imc:.2f}")