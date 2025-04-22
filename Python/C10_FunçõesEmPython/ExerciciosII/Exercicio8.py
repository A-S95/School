# FT1001H_ExRev_08_Pensao.py

def criar_pensao(andares=3, quartos_por_andar=5):
    return [['Livre' for _ in range(quartos_por_andar)] for _ in range(andares)]

def mostrar_quartos(pensao):
    for andar, quartos in enumerate(pensao, start=1):
        print(f"Andar {andar}: {', '.join(quartos)}")

def reservar_quarto(pensao, andar, quarto):
    if pensao[andar - 1][quarto - 1] == 'Livre':
        pensao[andar - 1][quarto - 1] = 'Reservado'
        print("Quarto reservado com sucesso!")
    else:
        print("Quarto não está disponível para reserva.")

def ocupar_quarto(pensao, andar, quarto):
    if pensao[andar - 1][quarto - 1] in ['Livre', 'Reservado']:
        pensao[andar - 1][quarto - 1] = 'Ocupado'
        print("Quarto ocupado com sucesso!")
    else:
        print("Quarto já está ocupado.")

def desocupar_quarto(pensao, andar, quarto):
    if pensao[andar - 1][quarto - 1] != 'Livre':
        pensao[andar - 1][quarto - 1] = 'Livre'
        print("Quarto desocupado com sucesso!")
    else:
        print("O quarto já está livre.")

def menu():
    pensao = criar_pensao()
    while True:
        print("\nMenu:")
        print("1. Listar quartos")
        print("2. Reservar quarto")
        print("3. Ocupar quarto")
        print("4. Desocupar quarto")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            mostrar_quartos(pensao)
        elif opcao in ['2', '3', '4']:
            try:
                andar = int(input("Informe o andar (1 a 3): "))
                quarto = int(input("Informe o quarto (1 a 5): "))
                if opcao == '2':
                    reservar_quarto(pensao, andar, quarto)
                elif opcao == '3':
                    ocupar_quarto(pensao, andar, quarto)
                elif opcao == '4':
                    desocupar_quarto(pensao, andar, quarto)
            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif opcao == '5':
            print("Encerrar programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
