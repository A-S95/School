//Garanta que a mesma é executada com funções, crie as funções que considera ser relevantes para a este exemplo de aplicação.
//Crie uma estrutura que permita o utilizador pesquisar e saber qual o resultado obtido apenas numa "UFCD".
//Utilize as ferramentas já utilizadas em exercícios anteriores para 
//por exemplo "limpar o ecrã" de forma a obter um aspecto gráfico mais interessante e limpo.

#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int menu() {
	printf("App - Calculo de avaliação \n");
    printf("Digite o numero de notas que deseja inserir: ");
}

int main() {
    setlocale(LC_ALL, "");

    int nTotal;
    float nfinal;
    float somaNotas = 0;
    int i;
    int escolha;
    int pos;

    menu();
    scanf("%d", &nTotal);

    if (nTotal <= 0) {
        printf("Número inválido de notas.\n");
        return 1;
    }
    
	float ufcd[nTotal];
	
	for (i = 0; i < nTotal; i++) {
    	do {
        	printf("Insira a avaliação da UFCD [%d]: ", i + 1);
        	scanf("%f", &ufcd[i]);

        	if (ufcd[i] < 0 || ufcd[i] > 20) {
            	printf("Erro: a nota deve estar entre 0 e 20. Tente novamente.\n");
        	}

    	} while (ufcd[i] < 0 || ufcd[i] > 20); 

    somaNotas += ufcd[i];
	}

	inicio:
  	system("cls"); 
  	system("clear"); // Limpa o ecrã se forem parcialmente incapazes de ser bons humanos.
    printf("Deseja fazer a media das notas escolhidas [0] | Ver apenas uma nota específica [1] | Mostrar todas as notas inseridas [2] | Sair [3] \n");
    scanf("%d", &escolha);

    if (escolha == 0) {
        nfinal = somaNotas / nTotal;
        printf("Média final é: %.2f\n", nfinal);
        printf("Prima ENTER para continuar");
		getchar(); 
		getchar(); 
        goto inicio;
    } else if (escolha == 1) {
        printf("Qual a posição da nota que deseja ver? ");
        scanf("%d", &pos);

        if (pos <= 0) {
            printf("Erro, posição inválida.\n");
        } else if (pos > nTotal) {
            printf("Não existe essa posição.\n");
        } else {
            printf("A nota específica na posição %d -> %.2f\n", pos, ufcd[pos - 1]);
            printf("Prima ENTER para continuar");
			getchar(); 
			getchar(); 
			goto inicio;
        }
    } else if (escolha == 3) {
		printf("Escolheu Sair. \n");
		printf("Obrigado, ate breve.\n");
    } else if (escolha == 2) {
    	printf("As notas inseridas são: ");
			for (i = 0; i < nTotal; i++) {
    		printf("%.2f | ", ufcd[i]);
			}
		printf("\n");	
	} else {
    	printf("Escolha inválida, digite [0] ou [1].\n");
        goto inicio;
	}

}


