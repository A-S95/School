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
	printf(" 10 a 18 - Aprovado \n");
	printf("19 a 20 - Excelente \n");
	
	printf("A classificacao do aluno e: ");
	printf("%.2f\n", classificacao);
	
	if (classificacao > 18)
		printf("Aluno Excelente"); 					//verdadeiro 1
	else if (classificacao >= 10)	
		printf("Aluno Aprovado"); 					//verdadeiro 2
	else if (classificacao < 8)
		printf("Aluno Reprovado");					//verdadeiro 3
	else
		printf("Aluno vai a Exame"); 				//falso 
}
