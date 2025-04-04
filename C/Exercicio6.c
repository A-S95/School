#include <stdio.h>

int main(){

	float valorHora;
	int horaTrabalho;
	float valorTotal;
//	float valorAlimentacao = 10;
	float valAlimentacao;
//	float bonusAli;
	
	printf("Indique o valor hora: ");
	scanf("%f", &valorHora);
	printf("Indique o numero total de horas: ");
	scanf("%d", &horaTrabalho);
	printf("Indique o valor do alimentacao (por dia): ");
	scanf("%f", &valAlimentacao);
	
	valorTotal = (valorHora + (valAlimentacao/8))* horaTrabalho;
//	bonusAli = horaTrabalho * valAlimentacao;
	
	printf("Resumo:");
	printf("Valor hora: %.2f euros\n", valorHora);
	printf("Total de Horas: %d\n", horaTrabalho);
	printf("Custo do projeto: %.2f\n", valorTotal);
}
