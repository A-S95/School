# Potenciais de 1/2
base = 1/2
expoente = 1
limite = 10

print("Potências de 1/2:")

while expoente <= limite:
    resultado = base ** expoente
    print(f"(1/2)^{expoente} = {resultado:.10f}")
    expoente += 1