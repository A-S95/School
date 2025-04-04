#include <stdio.h>
#include <locale.h>

int main() {
	
	setlocale(LC_ALL, "");
	int i = 1;
	float soma, num;
	
	printf("APP - SOMA DE NUMEROS\n");
	printf("Permite somar 3 numeros ou terminar quando um for negativo \n");
	printf("%d. Introduza um numero: ", i);
	scanf("%f", &num);
	
	i++;
	if (num<0){
		goto final;
	}
	
	soma += num;
	printf("%d. Introduza um numero: ", i);
	scanf("%f", &num);
	
	i++;
	if (num<0) {
		goto final;
	}
	
	soma += num;
	printf("%d. Introduza um numero: ", i);
	scanf("%f", &num);
	i++;
	if (num<0) {
		goto final;
	}
	
	soma += num;
	printf("Soma dos numeros: %.2f\n ", soma);
	printf("Media dos numeros: %.2f\n ", soma/3);
	final:
	printf("Obrigado por ter usado a App");
}
