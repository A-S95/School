#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
int idade;

printf("Diga a sua idade: ");
scanf("%d", &idade);

if (idade >= 18)
	printf("Pode entrar Utilizador\n");
else
	printf("O utilizador e demasiado novo para utilizar a nossa APP\n");
		 		
printf("Obrigado por usar a nossa aplicação ");
}
