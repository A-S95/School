#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
    int numA=1, numB=1;
    
    // executa enquanto o numA e numB forem diferentes de 0
    while (numA != 0 && numB != 0) {
    	printf("Introduza o primeiro numero: (0 - para sair)\n");
    	scanf("%d", &numA);
    	if (numA != 0) {
    		printf("Introduza o segundo numero: (0 - para sair)\n");
    		scanf("%d", &numB);
		}
		// apenas mostra o resultado com numeros diferentes de zero
		if (numA!=0 && numB != 0)
			printf("A soma de %d com %d e igual a %d\n", numA, numB, numA+numB);
	}
}




    int numA, numB; // 0 , 1
    
    printf("introduza o primeiro numero: (0 - para sair)\n");
    scanf("%d", &numA);
    // executa enquanto o numA e numB forem diferentes de 0
    while (numA != 0 && numB != 0) {
    	
    	printf("Introduza o segundo numero: (0 - para sair)\n");
    	scanf("%d", &numB);
    	if (numB != 0) {
    		printf("Introduza o primeiro numero: (0 - para sair)\n");
    		scanf("%d", &numB);
		}
		// apenas mostra o resultado com numeros diferentes de zero
		if (numA!=0 && numB != 0)
			printf("A soma de %d com %d e igual a %d\n", numA, numB, numA+numB);
