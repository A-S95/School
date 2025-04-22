#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
    int opt=1;
    
	while(opt==1){
		printf("O valor e igual a %d \n", opt);
//		Para proceder a alteracao do valor da condicao
		scanf("%d", &opt);
	}
	
	printf("Fim da App.");
}

//	while(condicao)
//	{
//		Instrucoes // Enquanto a condicao for verdadeira,
//	}
