#include <stdio.h>
#include <locale.h>

int main() {
	
	setlocale(LC_ALL, "");
	char letra, letra2, letra3;
	
	printf("APP - leitura de caracter\n");
	printf("Insira 3 caracteres:");
	printf("Faça ENTER depois de inserir\n");
	// getchar apanha um unico caracter e transforma o valor para int automaticamente.
	letra = getchar();
	// fflush, serve para limpar inputs inutilizados, neste caso o ENTER.
	fflush(stdin);
	letra2 = getchar();
	fflush(stdin);
	letra3 = getchar();
	printf("1-> %c || 2-> %c || 3-> %c", letra, letra2, letra3);
	
}
