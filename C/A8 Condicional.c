#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	int A,B;
	
	printf("Insira o valor a (A|B)"); 			//passo 1
	scanf("%d %d", &A, &B); 					// passo 2
	
	// Estrutura condicional
	if (A == B)
		printf("Os valores sao iguais\n");		// passo 3
	else 
	// sem { } ele so le o primeiro valor, ou seja o printf("fim") 
	// esta fora do ifelse
		printf("Os valores sao diferentes\n"); 	// passo 3
		printf("Fim"); 							// passo 4
}
