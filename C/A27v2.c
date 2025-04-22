#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

float soma(float num, float nDois){
	return num + nDois;
}

float subtrair(float num, float nDois){
	return num - nDois;
}

float multiplicar(float num, float nDois){
	return num * nDois;
}

float dividir(float num, float nDois){
	return num / nDois;
}

int main() {
	setlocale(LC_ALL, "");
	
	int opc;
	float numUm, numDois, res;
	
	printf("App - Calculadora\n");
	
	do {
		printf("Escolha o calculo a realizar \n");
		printf("1. Somar     || 2. Subtrair    || 3. Multiplicar      || 4. Dividir\n");
		printf("5. Sair\n");
		scanf("%d", &opc);
		
		if (opc < 1 || opc > 5) {
			printf("Opção inválida. Por favor, escolha entre 1 e 5.\n");
			continue;
		}

		if (opc >= 1 && opc <= 4) {
			printf("Insira o primeiro valor (positivo e diferente de 0): ");
			scanf("%f", &numUm);
			printf("Insira o segundo valor (positivo e diferente de 0): ");
			scanf("%f", &numDois);

			if (numUm <= 0 || numDois <= 0) {
				printf("Erro: Apenas valores positivos e diferentes de 0 são permitidos.\n");
				continue;
			}
		}
		
		switch (opc){
			case 1:
				res = soma(numUm, numDois);
				printf("O resultado é: %.2f\n", res);
				break;
			case 2:
				res = subtrair(numUm, numDois);
				printf("O resultado é: %.2f\n", res);
				break;
			case 3:
				res = multiplicar(numUm, numDois);
				printf("O resultado é: %.2f\n", res);
				break;				
			case 4:
				res = dividir(numUm, numDois);
				printf("O resultado é: %.2f\n", res);
				break;				
			case 5:
				printf("A sair da app...\n");
				break;				
		}	
	} while(opc != 5);
}
