#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	// Quadro de jogo:
    printf("Bem vindos ao Quiz ADN \n");
	printf("=====================================\n");
    printf("            REGRAS DO QUIZ           \n");
    printf("=====================================\n");
    printf("1 - Responda a 10 perguntas! No fim de cada pergunta, se errar, ir� ter uma quest�o b�nus! \n");
    printf("2 - 4 op��es em cada pergunta, apenas 1 est� correta. \n");
    printf("3 - Cada pergunta vale 20 pontos. \n");
    printf("4 - Caso erre a pergunta, haver� uma quest�o b�nus que vale 10 pontos. \n");
    printf("5 - Cada questao b�nus vale 10 pontos. \n");
    printf("6 - Ao errar a pergunta + a quest�o b�nus, o jogo termina e fica s� com os pontos at� a� acumulados. \n");
    printf("Pontua��o m�xima = 200 pontos || 10 perguntas = 20 pontos cada | 10 quest�es b�nus = 10 pontos cada. \n");
    
    
    // Variaveis
	int questionario;
	int pontuacao = 20;
	int bonus = 10;
	int resultado = 0;
	int ajuda = 3;
	
	printf("\n");
	printf("Que comece o jogo \n");
	printf("\n");
	
	if (ajuda <= 0) {
		printf("Nao pode usar mais ajudas");
	} 
	else {		
	//Primeira pergunta : O que significa a sigla CPU?
	printf("O que significa a sigla CPU? \n");
	//Opcoes
	printf("1) Central Processing Unit \n");
	printf("2) Computer Personal Unit \n");
	printf("3) Control Processing Unit \n");
	printf("4) Central Personal Unit \n");
	printf("5) Pedir ajuda \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
		if (questionario == 5) {
			printf("Usou uma ajuda \n");
			ajuda = ajuda - 1;
			printf("O que significa a sigla CPU? \n");
			printf("1) Central Processing Unit \n");
			printf("4) Central Personal Unit \n");
			scanf("%d", &questionario);
			resultado = resultado + pontuacao;
			printf("Tem %d pontos \n", resultado);
			printf("\n");
		} 
		else if (questionario == 1) {
			printf("Acertou!!! \n");
			resultado = resultado + pontuacao;
			printf("Tem %d pontos \n", resultado);
			printf("\n");	
		}
		else {
			printf("Errou, vamos iniciar a Pergunta bonus: \n");
			// Pergunta bonus
			printf("PERGUNTA BONUS \n");
			printf("\n");
			printf("O que � uma rede Wi-Fi? \n");
			printf("1) Um cabo para conectar dispositivos \n");
			printf("2) Uma rede sem fio para conectar dispositivos � internet \n");
			printf("3) Um programa para editar v�deos \n");
			printf("4) Um tipo de sistema operacional \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);

				if (questionario == 2) {
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
				}
				else {
					printf("Falhou a pergunta bonus. \n");
					printf("Finalizou com %d pontos\n", resultado);
					printf("\n");
					printf("Fim do jogo. Obrigado por jogar. \n");
					return 0;
				}		
			}
		}
	}
