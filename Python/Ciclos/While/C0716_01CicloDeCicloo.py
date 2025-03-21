####################################################
# Capítulo 07 - Estruturas de Ciclo
####################################################
#  - Ciclo de Contagem
####################################################
#
# Enunciado:
#
#  Faça uma programa que permita ao Robot
#  aspirador limpar os quartos de uma pensão.
#  A pensão tem três andares e cada andar tem
#  sete quartos.
#####################################################
# Programa
NUMANDARES = 3
NUMQUARTOSPORANDAR = 7

for contaAndar in range(1,NUMANDARES+1,1):
    print("Chegada ao andar : "+str(contaAndar))
    for contaQuarto in range (1,NUMQUARTOSPORANDAR+1,1):
        print("-> Limpeza do quarto: "
              +str(contaAndar)+".0"+str(contaQuarto)+".")


