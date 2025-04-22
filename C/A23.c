#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	int numA = 1, numB = 1;  // inicialização necessária para entrar no loop

	// executa enquanto o numA e numB forem diferentes de 0
	while (numA != 0 && numB != 0) {
		printf("Introduza o primeiro numero: (0 - para sair)\n");
		scanf("%d", &numA);
		
		if (numA == 0) // se o primeiro for 0, sair antes de pedir o segundo
			break;

		printf("Introduza o segundo numero: (0 - para sair)\n");
		scanf("%d", &numB);

		if (numB == 0) // se o segundo for 0, sair antes de mostrar resultado
			break;

		// apenas mostra o resultado com numeros diferentes de zero
		printf("A soma de %d com %d e igual a %d\n", numA, numB, numA + numB);
	}

	return 0;
}
