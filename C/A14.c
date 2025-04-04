#include <stdio.h>
#include <locale.h>

int menu();

int main() {
    setlocale(LC_ALL, "");

	int opc;
	
	printf("App - Faca voce mesmo...\n");
	
// Menu
//	printf("Escolha a opcao a realizar: \n");
//	printf("1 - Para realizar a opcao A \n");
//	printf("2 - Para realizar a opcao B \n");
//	printf("3 - Para realizar a opcao C \n");
//	printf("4 - Para realizar a opcao D \n");
	//menu(); // Chamar a funcao menu()
	scanf("%d", &opc);
	
	switch (opc) {
		case 1:	
			printf("A opcao a realizar e A ");
			break;
		case 2:	
			printf("A opcao a realizar e B ");
			break;
		case 3:	
			printf("A opcao a realizar e C ");
			break;
		case 4:	
			printf("A opcao a realizar e D ");
			break;
		default:
			printf("Valor invalido.");
		}

int menu() {
	printf("Escolha a opcao a realizar: \n");
	printf("1 - Para realizar a opcao A \n");
	printf("2 - Para realizar a opcao B \n");
	printf("3 - Para realizar a opcao C \n");
	printf("4 - Para realizar a opcao D \n");
}		
	printf("Fim do programa.");
}
