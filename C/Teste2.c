#include <stdio.h>
#include <locale.h>

int menu() {
	printf("APP - CALCULADORA \n");
	printf("1 - Soma \n");
	printf("2 - Subtracao \n");
	printf("3 - Multiplicacao \n");
	printf("4 - Divisao \n");
	printf("5 - Sair do Programa \n");
}

int main() {
	setlocale(LC_ALL, "");
	
	int opcao, resultado;
	int num1, num2;
	int escolha = 1;
	char sair;
			
	while (escolha != 0) { 
		menu();
		scanf("%d", &opcao);
			switch (opcao) {
	        	case 1:
	            	printf("Escolheu a soma. \n");
	            	printf("Digite o primeiro valor a somar? \n");
	            	scanf("%d", &num1); // 
	            	printf("Digite o segundo valor a somar? \n");
	            	scanf("%d", &num2);
	            	resultado = num1 + num2;
	            	printf("Resultado: %d\n", resultado);
	            	printf("\n");
	            	break;
	        	case 2:
	        		printf("Escolheu a subtracao. \n");
	            	printf("Digite o primeiro valor a subtrair? \n");
	            	scanf("%d", &num1); // 
	            	printf("Digite o segundo valor a subtrair? \n");
	            	scanf("%d", &num2);
	            	resultado = num1 - num2;
	            	printf("Resultado: %d\n", resultado); 
	            	printf("\n");
	            	break;
	        	case 3:
	        		printf("Escolheu a multiplicacao. \n");
	            	printf("Digite o primeiro valor a multiplicar? \n");
	            	scanf("%d", &num1); // 
	            	printf("Digite o segundo valor a multiplicar? \n");
	            	scanf("%d", &num2);
	            	resultado = num1 * num2;
	            	printf("Resultado: %d\n", resultado); 
	            	printf("\n");
	            	break;
				case 4:
    				printf("Escolheu a divisao. \n");
    				printf("Digite o primeiro valor a dividir? \n");
    				scanf("%d", &num1);
    				printf("Digite o segundo valor a dividir? \n");
    				scanf("%d", &num2);
    				if (num2 == 0 || num1 == 0) {
        				printf("Erro: Divisao por zero nao permitida!\n");
    				} else {
        				resultado = num1 / num2;
        				printf("Resultado: %d\n", resultado);
    				}
    				printf("\n");
    				break;
				case 5:
    				printf("Tem a certeza que deseja sair do programa? (S | N) ");
    				scanf(" %c", &sair);  
    				switch (sair){
        				case 's':
        				case 'S':
            				printf("Saiu da aplicacao! \n");
            				escolha = 0;
            			break;  
        			default:
            			printf("Permaneceu na app \n");
            			escolha = 1;
            			break;  
    				}
    				break;
				default:
					printf("Operacao invalida.");
					escolha = 0;
			}
	}
}
