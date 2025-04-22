import os

NUM_ANDARES = 3
QUARTOS_POR_ANDAR = 5
TOTAL_QUARTOS = NUM_ANDARES * QUARTOS_POR_ANDAR

LIVRE = "Livre"
RESERVADO = "Reservado"
OCUPADO = "Ocupado"

def inicializa_pensao():
    """Inicializa a pensão com todos os quartos livres."""
    pensao = []
    for andar in range(NUM_ANDARES):
        for quarto in range(QUARTOS_POR_ANDAR):
            pensao.append({
                "andar": andar + 1,
                "quarto": quarto + 1,
                "estado": LIVRE
            })
    return pensao

def listar_quartos(pensao):
    """Lista todos os quartos e seus estados."""
    print("\nListagem de Quartos:")
    for quarto in pensao:
        print(f"Andar: {quarto['andar']}, Quarto: {quarto['quarto']}, Estado: {quarto['estado']}")

def reservar_quarto(pensao):
    """Reserva um quarto específico."""
    andar = int(input("Andar do quarto: "))
    quarto_numero = int(input("Número do quarto: "))

    for quarto in pensao:
        if quarto['andar'] == andar and quarto['quarto'] == quarto_numero:
            if quarto['estado'] == LIVRE:
                quarto['estado'] = RESERVADO
                print("Quarto reservado com sucesso!")
            else:
                print("Quarto não disponível para reserva.")
            return

    print("Quarto não encontrado.")

def ocupar_quarto(pensao):
    """Ocupa um quarto específico."""
    andar = int(input("Andar do quarto: "))
    quarto_numero = int(input("Número do quarto: "))

    for quarto in pensao:
        if quarto['andar'] == andar and quarto['quarto'] == quarto_numero:
            if quarto['estado'] == LIVRE or quarto['estado'] == RESERVADO:
                quarto['estado'] = OCUPADO
                print("Quarto ocupado com sucesso!")
            else:
                print("Quarto não disponível para ocupação.")
            return

    print("Quarto não encontrado.")

def desocupar_quarto(pensao):
    """Desocupa um quarto específico."""
    andar = int(input("Andar do quarto: "))
    quarto_numero = int(input("Número do quarto: "))

    for quarto in pensao:
        if quarto['andar'] == andar and quarto['quarto'] == quarto_numero:
            if quarto['estado'] == OCUPADO:
                quarto['estado'] = LIVRE
                print("Quarto desocupado com sucesso!")
            else:
                print("Quarto não está ocupado.")
            return

    print("Quarto não encontrado.")

def mostra_menu():
    """Mostra o menu de opções."""
    print("\n*** Gestão da Pensão ***")
    print("1. Listar quartos")
    print("2. Reservar quarto")
    print("3. Ocupar quarto")
    print("4. Desocupar quarto")
    print("5. Sair")

def obtem_escolha():
    """Obtém a escolha do usuário."""
    return input("Escolha uma opção: ")

def processa_escolha(pensao, escolha):
    """Processa a escolha do usuário."""
    if escolha == '1':
        listar_quartos(pensao)
    elif escolha == '2':
        reservar_quarto(pensao)
    elif escolha == '3':
        ocupar_quarto(pensao)
    elif escolha == '4':
        desocupar_quarto(pensao)
    elif escolha == '5':
        return True  # Sair do programa
    else:
        print("Opção inválida.")
    return False

# Programa principal
pensao = inicializa_pensao()
sair = False

while not sair:
    mostra_menu()
    escolha = obtem_escolha()
    sair = processa_escolha(pensao, escolha)

print("Programa encerrado.")