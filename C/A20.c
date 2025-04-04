#include <stdio.h>
#include <locale.h>

int menu() {
	
	int opcao;
	printf("Escolha uma opcao (1 a 3): \n");
	printf("1 - Para selecionar A \n");
	printf("2 - Para selecionar B \n");
	printf("3 - Para selecionar C \n");
	scanf("%d", &opcao);
	
	return opcao;
}


int main() {
	setlocale(LC_ALL, "");
	int opcao;
	
	opcao = menu();
	
	if (opcao ==1)
		printf("O utilizador escolheu A \n");
	else if (opcao == 2)
		printf("O utilizador escolheu B \n");
	else if (opcao == 3)
		printf("O utilizador escolheu C \n");	
	else 
		printf("O utilizador escolheu uma opcao invalida \n");	
	
}



