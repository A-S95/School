#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main() {
	setlocale(LC_ALL, "");
	
	int num = 1;
	
	printf("Insira um valor: \n");
	scanf("%d", &num);
	
	do {
		printf("Numero %d \n", num);
		printf("Insira um valor: (dentro do ciclo)\n");
		scanf("%d", &num);	
	}
	while (num < 5);
}
