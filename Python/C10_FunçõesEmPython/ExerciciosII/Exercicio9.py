# FT1001H_ExRev_09_Cinema.py

def criar_cinema(filas=7, lugares_por_fila=5):
    return [['Livre' for _ in range(lugares_por_fila)] for _ in range(filas)]

def listar_lugares(cinema):
    print("\nEstado atual dos lugares:")
    for i, fila in enumerate(cinema, start=1):
        print(f"Fila {i}: {', '.join(fila)}")

def reservar_lugar(cinema, fila, lugar):
    if cinema[fila - 1][lugar - 1] == 'Livre':
        cinema[fila - 1][lugar - 1] = 'Reservado'
        print("Lugar reservado com sucesso!")
    else:
        print("Lugar indisponível para reserva.")

def marcar_lugar(cinema, fila, lugar):
    if cinema[fila - 1][lugar - 1] in ['Livre', 'Reservado']:
        cinema[fila - 1][lugar - 1] = 'Ocupado'
        print("Lugar marcado com sucesso!")
    else:
        print("Lugar já está ocupado.")

def libertar_lugar(cinema, fila, lugar):
    if cinema[fila - 1][lugar - 1] != 'Livre':
        cinema[fila - 1][lugar - 1] = 'Livre'
        print("Lugar libertado com sucesso!")
    else:
        print("O lugar já está livre.")

def fim_sessao(cinema):
    for fila in range(len(cinema)):
        for lugar in range(len(cinema[0])):
            cinema[fila][lugar] = 'Livre'
    print("Sessão encerrada! Todos os lugares foram libertados.")

def menu():
    cinema = criar_cinema()
    while True:
        print("\nMenu:")
        print("1. Listar lugares")
        print("2. Reservar lugar")
        print("3. Marcar lugar")
        print("4. Libertar lugar")
        print("5. Fim de sessão")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_lugares(cinema)
        elif opcao in ['2', '3', '4']:
            try:
                fila = int(input("Informe a fila (1 a 7): "))
                lugar = int(input("Informe o lugar (1 a 5): "))
                if fila < 1 or fila > 7 or lugar < 1 or lugar > 5:
                    print("Fila ou lugar inválido.")
                    continue
                if opcao == '2':
                    reservar_lugar(cinema, fila, lugar)
                elif opcao == '3':
                    marcar_lugar(cinema, fila, lugar)
                elif opcao == '4':
                    libertar_lugar(cinema, fila, lugar)
            except ValueError:
                print("Entrada inválida. Use apenas números.")
        elif opcao == '5':
            fim_sessao(cinema)
        elif opcao == '6':
            print("Encerrar programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
