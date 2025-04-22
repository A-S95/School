#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");

	int numA, numB;

	printf("Introduza o primeiro numero: (0 - para sair)\n");
	scanf("%d", &numA);

	while (numA != 0) {
		printf("Introduza o segundo numero: (0 - para sair)\n");
		scanf("%d", &numB);

		if (numB == 0) {
			printf("Soma incompleta: recebeu apenas o primeiro número (%d).\n", numA);
			break;
		}

		printf("A soma de %d com %d e igual a %d\n", numA, numB, numA + numB);

		printf("Introduza o primeiro numero: (0 - para sair)\n");
		scanf("%d", &numA);

		if (numA == 0) {
			printf("Programa Encerrado.\n");
		}
	}
}
