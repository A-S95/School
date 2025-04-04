# Gestao do parque de estacionamento.

# Com Sete Posicoes.

# LISTAR LUGARES
# MARCAR LUGAR
# LIBERTAR LUGAR
# SAIR DO PROGRAMA.


lugares = [0] * 7 

while True:
    print("---------------------------------")
    print("1 - Listar Lugares")
    print("2 - Marcar Lugar")
    print("3 - Libertar Lugar")
    print("4 - Sair do Programa")
    print("---------------------------------")
    print()
    print("Escolha: ", end="")
    escolha = int(input())
    print()

    if escolha == 1:
        print("---------------------------------")
        for cLugar in range(7):
            status = "Livre" if lugares[cLugar] == 0 else "Ocupado"
            print(f"Lugar {cLugar+1}: {status}")
        print("---------------------------------")
    elif escolha == 2:
        print("---------------------------------")
        print("Qual Lugar deseja marcar (1-7)? ", end="")
        lugar = int(input()) - 1
        if lugar < 0 or lugar >= 7:
            print("Lugar Inválido!")
        elif lugares[lugar] == 1:
            print("Lugar já está ocupado!")
        else:
            lugares[lugar] = 1
            print("Lugar Marcado com Sucesso!")
    elif escolha == 3:
        print("---------------------------------")
        print("Qual Lugar deseja libertar (1-7)? ", end="")
        lugar = int(input()) - 1
        if lugar < 0 or lugar >= 7:
            print("Lugar Inválido!")
        elif lugares[lugar] == 0:
            print("Lugar já está Livre!")
        else:
            lugares[lugar] = 0
            print("Lugar Libertado com Sucesso!")
    elif escolha == 4:
        print("---------------------------------")
        print("Tem a certeza que deseja sair (S/N)? ", end="")
        resposta = input().upper()
        if resposta == "S":
            break
    else:
        print("Opção inválida!")

    print()
    input("Prima ENTER para continuar ... ")
    print()