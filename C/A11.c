#include <stdio.h>
#include <locale.h>
#include <stdbool.h>

int main() {
    setlocale(LC_ALL, "");
    
// 	variaveis
 	int ano;
 
// 	inputs / outputs
 	printf("App - Ano bissexto");
 	printf("Descubra se o ano é Bissexto\n");
 	printf("Introduza o ano que pretende saber: ");
 	scanf("%d", &ano);
 
//	Estrutura Condicional
	if( ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0 )
	printf("O ano %d é bissexto.", ano);
	else
	printf("O ano %d não é bissexto.", ano);
}
