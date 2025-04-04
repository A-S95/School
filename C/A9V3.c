#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	float classificacao;
	printf("Insira a classificacao do Aluno \n");
	scanf("%f", &classificacao);					// Aceita valor feito pelo Utilizador
	
	printf("App de avaliacao: \n");
	printf(" 0 a 7 - Reprovado \n");
	printf(" 8 a 9 - Exame \n");
	printf(" 10 a 20 - Aprovado \n");
	
	printf("A classificacao do aluno e: ");
	printf("%.2f\n", classificacao);
	
	if (classificacao >= 10)
		printf("Aluno Aprovado"); 					//verdadeiro 1
	else if (classificacao >= 8)	
	//else if (classificacao > 8 && classificacao < 10) // comparativo entre(&& ||) condicoes
		printf("Aluno vai a Exame"); 				//verdadeiro 2
	else
		printf("Aluno Reprovado"); 					//falso 
}
