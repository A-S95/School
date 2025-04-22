#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");

	char l1,l2,l3;
	printf("App - Leitura de caracteres\n");
	printf("Insira caracteres na aplicacao\n");
	
	while (l1 != '0' && l2 != '0' && l3 != '0') {
		printf("Insira 3 caracteres (0 - para sair)\n");
		l1 = getchar();
		fflush(stdin);
		if (l1 != '0'){
			l2 = getchar();
			fflush(stdin);
			if (l2 != '0'){
				l3 = getchar();
				fflush(stdin);
			}
		}
		
		printf("letra 1 --> %c || letra 2 --> %c || letra 3 --> %c  \n", l1, l2,l3);
		printf("Clique em qualquer tecla para prosseguir.\n");
		getchar();
		//semelhante ao getchar
//		system("pause");
		system("cls");
	}
	
}
