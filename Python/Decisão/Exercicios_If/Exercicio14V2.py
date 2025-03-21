# Escreva um programa que calcula os perimetros do quadrado, do circulo
# ou do triangulo de acordo com a escolha do utilizador.
# Extras »»» Calculo de Angulos com limitador de 180.

lq1 = 0
raio = 0
lt1 = 0
aT = 0
anG = 0
pT = 0
resposta = 0
bR = 0
aR = 0

while True:
    resposta = int(input("Escolhe uma das opcoes: 1 - Perimetro do Quadrado, 2 - Perimetro do Circulo, 3 - Perimetro do Triangulo "))
    if resposta == 1:
        print("Escolheu a opção 1 - Perimetro do Quadrado")
        lq1 = int(input("Digite o primeiro lado do quadrado ")) + int(input("Digite o segundo lado do quadrado ")) + int(input("Digite o terceiro lado do quadrado ")) + int(input("Digite o quarto lado do quadrado "))
        pQ = int(lq1)
        print("O perimetro do Quadrado é :", pQ)
        break
    elif resposta == 2:
        print("Escolheu a opção 2 - Perimetro do Circulo")
        raio = input("Digite o raio do circulo")
        pC = int(2) * float(3.14) * int(raio)
        print("O perimetro do Circulo é :", pC)
        break
    elif resposta == 3:
        print("Escolheu a opção 1 - Perimetro do Triangulo")
        lt1 = int(input("Digite o primeiro lado do Triangulo ")) + int(input("Digite o segundo lado do Triangulo ")) + int(input("Digite o segundo lado do Triangulo "))
    
        anG = input("Deseja inserir o valor dos angulos do triangulo? (Sim ou nao) ")
        if anG.lower() in ['s', 'sim']:  #
            aT = int(input("Insira o valor de um angulo ")) + int(input("Insira o valor de um angulo ")) + int(input("Insira o valor de um angulo "))
            if aT != 180:
                print("Invalido, a amplitude do Triangulo não pode passar dos 180 graus, nem ser menor a 180.")
            else:
                print("A amplitude do triangulo é :", aT, "O perimetro do triangulo é :", lt1)
                break
        print("O perimetro do triangulo é :", lt1)
    elif resposta == 4:
        print("Escolheu a opção 1 - Perimetro do Rectangulo")
        bR = input("Digite a base do rectangulo")
        aR = input("Digite a altura do rectangulo")
        pR = 2 *(int(bR) + int(aR))
        print("O perimetro do Rectangulo é :", pR)
    else:
        print("Opcao invalida")

