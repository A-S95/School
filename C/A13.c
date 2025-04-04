#include <stdio.h>
#include <locale.h>

int main() {
	
	setlocale(LC_ALL, "");
	int mes;
	
	printf("App - Dias do Mes \n");
	printf("Introduza o mes (1 a 12): \n");
	scanf("%d", &mes);
		
	switch (mes) {	
		case 1 :
		case 3 :
		case 5 :
		case 7 :
		case 8 :
		case 10 :
		case 12 :
			printf("O mes tem 31 dia \n");
			printf(mes);
			break;
		case 2 :
			printf("O mes tem 28/29 dias \n");
			break;
		case 4 :
		case 6 :
		case 9 :
		case 11 :
			printf("O mes tem 30 dias \n");
			break;
		default:
			printf("Mes invalido. Valores entre 1 e 12 \n");
	}
	printf("Fim da app.");
}
