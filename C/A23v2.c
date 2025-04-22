#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	int numA = 1, numB = 1;  

	while (numA != 0 && numB != 0) {
		printf("Introduza o primeiro numero: (0 - para sair)\n");
		scanf("%d", &numA);
		
		if (numA == 0) 
			break;

		printf("Introduza o segundo numero: (0 - para sair)\n");
		scanf("%d", &numB);

		if (numB == 0) 
			break;

		printf("A soma de %d com %d e igual a %d\n", numA, numB, numA + numB);
	}
}
