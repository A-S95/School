#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main() {
	setlocale(LC_ALL, "");

	float ufcd[4];
	float nfinal;
	float somaNotas = 0;
	int i;
	
	printf("App - Calculo de avaliação \n");
	printf("Digite as avaliações da UFCD \n");
	// inputs
	for (i=0; i<4; i++) {
		printf("Insira a avaliação da UFCD %d \n", i+809);
		scanf("%f", &ufcd[i]);
		somaNotas += ufcd[i];
	}
	// Outputs
	printf("Mostrar o resumo das avaliações: ");
	for (i=0; i<4; i++) {
		printf(" UFCD %d -> %.2f	||", i+809, ufcd[i]);
	}
	
	nfinal = somaNotas / i;
	printf("Média final: %.2f ", nfinal);
	
}


////	Representação do Array ! indica o numero de posicoes para guardar valores.
//	int n[5] = {3, 5, 8, 1, 12};
//	int pos;
//	int i=0;
//	
//// Representação do array serve para mostrar o valor na posicao.
////	printf("Insira os valores no array \n");
////	scanf("%d", &n[0]); // Posição 1
////	scanf("%d", &n[1]);
////	scanf("%d", &n[2]);
////	scanf("%d", &n[3]);
////	scanf("%d", &n[4]); // Posição 5
//	printf("Indique a Posicao que quer escrever: \n");
//	scanf("%d", &pos);
//	printf("Indique o valor da posicao: \n");
//	scanf("%d", &n[pos-1]);
//	
//	while(i<5) {
//		printf("Mostrar o valor da posicao nº%d -> %d\n",i+1 , n[i]); // Posicao N[Todas]
//		i++;
//	}
//	
////	printf("Mostrar o valor de n posicao 1-> %d\n", n[0]); // Posição 1
////	printf("Mostrar o valor de n posicao 2-> %d\n", n[1]);
////	printf("Mostrar o valor de n -> %d\n", n[2]);
////	printf("Mostrar o valor de n -> %d\n", n[3]);
////	printf("Mostrar o valor de n -> %d\n", n[4]); // Posição 5
