#include <stdio.h>
#include <locale.h>
#include <ctype.h> 

int main() {
	
	setlocale(LC_ALL, "");
//	int num;
	char letra;
		
//	input/output
//	printf("Introduza um numero (1 a 3): ");
//	scanf("%d", &num);
	printf("Introduza um caractere (a ate c): ");
	scanf("%c", &letra);
	
	switch(tolower(letra)) {
		case 'a':
			printf("a = Um");
			printf("Valor e valido\n");
			break;
		case 'b':
			printf("b = Dois");
			printf("Valor e valido\n");
			break;
		case 'c':
			printf("c = Tres");
			printf("Valor e valido\n");
			break;
		default:
			printf("Valor e invalido"); 
		// Nao ha necessidade de meter break; no ultimo resultado.
	}
	printf("Final de aplicacao \n");
}

//Estrutura Switch ...case
// {
// switch(variavel) (?)= 1
//		case valor(1);
//			codigo;
//			break; Termina o switch e passa para a posicao *
//		case valor(2);
//			codigo;
//			break; Termina o switch e passa para a posicao *
//	 	case valor(3);
//			codigo;
//			break; Termina o switch e passa para a posicao *
//		default:
//			codigo;
// }

// * codigo restante
