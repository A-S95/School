#include <stdio.h>
#include <locale.h>

int main() {
	
	setlocale(LC_ALL, "");
	int i = 1;
	int soma = 0;
	
	while (i <= 4) {
		soma += i*i;
		i++;
	}
	
	printf("A soma dos primeiros 4 quadrados : %d\n", soma);
}
