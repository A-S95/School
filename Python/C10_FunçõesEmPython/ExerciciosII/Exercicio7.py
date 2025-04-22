# FT1001H_ExRev_07_Taxis.py

def criar_frota(qtd_taxis=10):
    return ['Livre' for _ in range(qtd_taxis)]

def listar_taxis(frota):
    for i, status in enumerate(frota, start=1):
        print(f"Táxi {i}: {status}")

def reservar_taxi(frota, numero):
    if frota[numero - 1] == 'Livre':
        frota[numero - 1] = 'Reservado'
        print("Táxi reservado com sucesso!")
    else:
        print("Táxi não está disponível para reserva.")

def chamar_taxi(frota, numero):
    if frota[numero - 1] in ['Livre', 'Reservado']:
        frota[numero - 1] = 'Em serviço'
        print("Táxi chamado com sucesso!")
    else:
        print("Táxi já está em serviço.")

def libertar_taxi(frota, numero):
    if frota[numero - 1] != 'Livre':
        frota[numero - 1] = 'Livre'
        print("Táxi libertado com sucesso!")
    else:
        print("O táxi já está livre.")

def menu():
    frota = criar_frota()
    while True:
        print("\nMenu:")
        print("1. Listar táxis")
        print("2. Reservar táxi")
        print("3. Chamar táxi")
        print("4. Libertar táxi")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_taxis(frota)
        elif opcao in ['2', '3', '4']:
            try:
                numero = int(input("Informe o número do táxi (1 a 10): "))
                if numero < 1 or numero > 10:
                    print("Número de táxi inválido.")
                    continue
                if opcao == '2':
                    reservar_taxi(frota, numero)
                elif opcao == '3':
                    chamar_taxi(frota, numero)
                elif opcao == '4':
                    libertar_taxi(frota, numero)
            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif opcao == '5':
            print("Encerrar programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
