#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

//Desenvolva a aplicação E3.c com base na A25.c
//O objetivo é ter a tabuada na mesma mas o utilizador procede à forma como quer realizar a tabuada.  As opções são:
//Faz apenas uma tabuada. Deve ser o utilizador a escolher qual a tabuada a ser realizada. 
//Faz um intervalo entre tabuadas(1 ao 10 como está realizado).
//A aplicação só deverá fechar por ordem do utilizador. Dessa forma opte por selecionar uma opção como 0 para "sair".

int menu() {
	printf("Como deseja que seja feita a tabuada:\n");
	printf("Apenas a tabuada que pretende [1] || todas as tabuadas de 1 a 10 [2]?\n");
	printf("Escolha [0] se quiser sair da app.\n");
}	

int main() {
    setlocale(LC_ALL, "");

    int i;
    int a=1;
	int escolha;
	int opcao;

	inicio:
	menu();
	scanf("%d", &escolha);
		
	while (escolha != 0) {
		if (escolha == 1) {
			printf("\n");
			printf("Escolha o numero que quer fazer a tabuada: \n");
			scanf("%d", &opcao);
			printf("\n");
			
    		for (i=1; i<=10; i++) {
            	printf("%d X %d = %d\n", opcao, i, opcao*i);
			}
			printf("\n");
		    goto inicio;
		} else if (escolha ==2) {
			    printf("\n Tabuada do 1 ao 10\n");
    			for(i=1; i<=10; i++){
        			for(a=1; a<=10; a++){
            			printf("%d X %d = %d\n", i, a, i*a);
        			}
        		printf("Prima Enter para continuar\n");
        		getchar();
				}
			goto inicio;
		}
	}
}

    
