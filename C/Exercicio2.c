#include <stdio.h>
#include <locale.h>

//A aplicação deve pedir quantos produtos o utilizador compra.
//A aplicação deve pedir o valor da compra.

int main() {
	setlocale(LC_ALL, "");
	
	int numProdutos;
	float valorCompra;
	float descontoMax = 2;
	float valorDescontoMax = 0.5;
	float descontoMin = 0.60;
	float valorDesconto = 0.4;
	float resultado;


	
	printf("APP - Bazar do digital\n");
	printf("As nossas promoções de Primavera\n");
	printf("Na compra de 3 ou mais produtos recebe um desconto de 40%%\n");
	printf("Numa compra de valor superior a 100 euros recebe um desconto de 40%%\n");
	printf("Numa compra de 3 ou mais produtos e num total de superior a 100€ recebe desconto de 50%%\n\n");
	
	
	printf("Insira o valor de produtos escolhidos: \n");
	scanf("%d", &numProdutos);
	printf("Valor da compra total: \n");
	scanf("%f", &valorCompra);
	
	if (numProdutos >= 3 && valorCompra > 100) {
		printf("O desconto sera de 50%% \n");
		resultado = valorCompra / descontoMax;
		valorDescontoMax =valorCompra * valorDescontoMax;
		printf("O valor da compra com desconto e: ");
		printf("%.2f euros \n", resultado); 
		printf("O valor descontado foi de: ");
		printf("%.2f euros", valorDescontoMax);
	} else if (numProdutos >= 3 || valorCompra > 100){
		printf("O desconto sera de 40%%\n");
		resultado = valorCompra * descontoMin;
		valorDesconto = valorCompra * valorDesconto;
		printf("O valor da compra com desconto e: ");
		printf("%.2f euros \n", resultado); 
		printf("O valor descontado foi de:");
		printf("%.2f euros", valorDesconto);
	} else {
		printf("Sem desconto: ");
		printf("%.2f euros", valorCompra);
	}
}
