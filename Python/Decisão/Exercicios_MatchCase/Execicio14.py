# Escreva um programa que calcula os perimetros do quadrado, do circulo
# ou do triangulo de acordo com a escolha do utilizador.
lq1 = 0
lq2 = 0
lq3 = 0
lq4 = 0
raio = 0
lt1 = 0
lt2 = 0
lt3 = 0
bR = 0
aR = 0

resposta = 0

while True:
    resposta = int(input("Escolhe uma das opcoes: 1 - Perimetro do Quadrado, 2 - Perimetro do Circulo, 3 - Perimetro do Triangulo, 4- Perimetro do Rectangulo "))
    match resposta:
        case 1:
            print("Escolheu a opção 1 - Perimetro do Quadrado")
            lq1 = input("Digite o primeiro lado do quadrado")
            lq2 = input("Digite o segundo lado do quadrado")
            lq3 = input("Digite o terceiro lado do quadrado")
            lq4 = input("Digite o quarto lado do quadrado")
            pQ = int(lq1) + int(lq2) + int(lq3) + int(lq4)
            print("O perimetro do Quadrado é :", pQ)
        case 2:
            print("Escolheu a opção 2 - Perimetro do Circulo")
            raio = input("Digite o raio do circulo")
            pC = int(2) * float(3.14) * int(raio)
            print("O perimetro do Circulo é :", pC)
        case 3:
            print("Escolheu a opção 1 - Perimetro do Triangulo")
            lt1 = input("Digite o primeiro lado do Triangulo")
            lt2 = input("Digite o segundo lado do Triangulo")
            lt3 = input("Digite o terceiro lado do Triangulo")
            pT = int(lt1) + int(lt2) + int(lt3)
            if pT > 180:
                print("Invalido, o perimetro do Triangulo não pode passar dos 180 graus")
            else:
                print("O perimetro do triangulo é :", pT)
        case 4:
            print("Escolheu a opção 1 - Perimetro do Rectangulo")
            bR = input("Digite a base do rectangulo")
            aR = input("Digite a altura do rectangulo")
            pR = 2 *(int(bR) + int(aR))
            print("O perimetro do Rectangulo é :", pR)
        case _:
            print("Opcao invalida")


