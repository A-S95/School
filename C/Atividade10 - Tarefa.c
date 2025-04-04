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
		
	printf("\n");
	printf("Que comece o jogo \n");
	printf("\n");
					
	//Primeira pergunta : O que significa a sigla CPU?
	printf("O que significa a sigla CPU? \n");
	//Opcoes
	printf("1) Central Processing Unit \n");
	printf("2) Computer Personal Unit \n");
	printf("3) Control Processing Unit \n");
	printf("4) Central Personal Unit \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 1) {
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
	
	//Segunda pergunta :
	printf("Qual � a fun��o principal do sistema operacional? \n");
	//Opcoes
	printf("1) Proteger o computador de v�rus \n");
	printf("2) Gerenciar os recursos do computador \n");
	printf("3) Criar documentos de texto \n");
	printf("4) Acelerar a conex�o com a internet \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 2) {
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
		printf("O que � um software? \n");
		printf("1) Um componente f�sico do computador\n");
		printf("2) Uma pe�a de metal dentro do computador \n");
		printf("3) Um programa ou aplicativo de computador \n");
		printf("4) Um tipo de cabo para conectar dispositivos \n");
		printf("A sua resposta: ");
		scanf("%d", &questionario);

			if (questionario == 3) {
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
	
	
	//Terceira pergunta : 
	printf("Qual � a diferen�a entre hardware e software? \n");
	//Opcoes
	printf("1) Hardware � f�sico, software � l�gico/programas \n");
	printf("2) Hardware � gratuito, software � pago \n");
	printf("3) Hardware � para jogos, software � para trabalho \n");
	printf("4) Hardware � interno, software � externo \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 1) {
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
		printf("O que � um arquivo PDF? \n");
		printf("1) Um tipo de v�rus de computador \n");
		printf("2) Um formato de arquivo para documentos digitais \n");
		printf("3) Um programa para editar fotos \n");
		printf("4) Um tipo de hardware para impress�o \n");
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
	
	//Quarta pergunta :
	printf("O que � um v�rus de computador? \n");
	//Opcoes
	printf("1) Um problema f�sico no disco r�gido \n");
	printf("2) Um software malicioso que pode danificar o computador \n");
	printf("3) Um erro do sistema operacional \n");
	printf("4) Um programa para limpar arquivos \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 2) {
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
		printf("Qual � a fun��o do mouse? \n");
		printf("1) Digitalizar documentos \n");
		printf("2) Processar dados \n");
		printf("3) Apontar e selecionar elementos na tela \n");
		printf("4) Armazenar informa��es \n");
		printf("A sua resposta: ");
		scanf("%d", &questionario);

			if (questionario == 3) {
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
	
	//Quinta pergunta :
	printf("O que � uma impressora? \n");
	//Opcoes
	printf("1) Um dispositivo que digitaliza documentos \n");
	printf("2) Um dispositivo que imprime documentos f�sicos \n");
	printf("3) Um software para criar documentos \n");
	printf("4) Um componente interno do computador \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 2) {
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
		printf("O que � um pendrive? \n");
		printf("1) Um dispositivo de armazenamento port�til \n");
		printf("2) Um tipo de processador \n");
		printf("3) Um software de seguran�a \n");
		printf("4) Um cabo para conectar monitores \n");
		printf("A sua resposta: ");
		scanf("%d", &questionario);

			if (questionario == 1) {
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
	
	//Sexta pergunta :
	printf("O que � um backup? \n");
	//Opcoes
	printf("1) Um tipo de v�rus \n");
	printf("2) Uma atualiza��o do sistema operacional \n");
	printf("3) Uma c�pia de seguran�a de arquivos \n");
	printf("4) Um dispositivo de entrada de dados \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 3) {
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
		printf("O que � um e-mail? \n");
		printf("1) Um tipo de v�rus \n");
		printf("2) Um servi�o de correio eletr�nico \n");
		printf("3) Um programa de edi��o de imagens \n");
		printf("4) Um dispositivo de armazenamento \n");
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

	//Setima pergunta :
	printf("O que � armazenamento em nuvem? \n");
	//Opcoes
	printf("1) Armazenar dados em disquetes antigos \n");
	printf("2) Armazenar dados em servidores remotos acess�veis pela internet \n");
	printf("3) Um tipo de disco r�gido especial \n");
	printf("4) Um programa para compactar arquivos \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 2) {
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
		printf(" O que � um smartphone? \n");
		printf("1) Um telemovel com fun��es avan�adas semelhantes �s de um computador \n");
		printf("2) Um tipo especial de mouse \n");
		printf("3) Um programa para fazer liga��es pelo computador \n");
		printf("4) Um dispositivo apenas para jogos \n");
		printf("A sua resposta: ");
		scanf("%d", &questionario);

			if (questionario == 1) {
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
	
	//Oitava pergunta : 
	printf("O que significa a sigla HTML? \n");
	//Opcoes
	printf("1) High Technical Modern Language \n");
	printf("2) Hyper Text Markup Language \n");
	printf("3) Hard Text Memory Link \n");
	printf("4) Hybrid Technical Machine Language \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 2) {
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
		printf(" O que � uma Motherboard? \n");
		printf("1) Um dispositivo de armazenamento externo \n");
		printf("2) Um software para controle do computador \n");
		printf("3) A placa principal onde os componentes do computador s�o conectados \n");
		printf("4) Um tipo de monitor de computador \n");
		printf("A sua resposta: ");
		scanf("%d", &questionario);

			if (questionario == 3) {
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
	
	//Nona pergunta :
	printf("O que � um sistema bin�rio? \n");
	//Opcoes
	printf("1) Um sistema que usa apenas os n�meros 0 e 1 \n");
	printf("2) Um sistema com dois monitores conectados \n");
	printf("3) Um sistema operacional com duas vers�es \n");
	printf("4) Um computador com dois processadores \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 1) {
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
		printf("O que significa a sigla USB? \n");
		printf("1) Universal Serial Bus \n");
		printf("2) United System Basic \n");
		printf("3) Universal Storage Battery \n");
		printf("4) Unified Serial Bandwidth \n");
		printf("A sua resposta: ");
		scanf("%d", &questionario);

			if (questionario == 1) {
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
		
	//Decima pergunta :
	printf("Qual � a fun��o principal do teclado? \n");
	//Opcoes
	printf("1) Mostrar imagens na tela \n");
	printf("2) Processar informa��es \n");
	printf("3) Inserir dados no computador \n");
	printf("4) Armazenar arquivos importantes \n");
	printf("A sua resposta: ");
	scanf("%d", &questionario);
	
	if (questionario == 3) {
		printf("Acertou!!! \n");
		resultado = resultado + pontuacao;
		printf("Tem %d pontos \n", resultado);
		printf("\n");
	} 
	else {
		printf("Errou, vamos iniciar a Pergunta Bonus: \n");
		// Pergunta bonus
		printf("PERGUNTA BONUS \n");
		printf("\n");
		printf(" O que � um programa antiv�rus? \n");
		printf("1) Um dispositivo para melhorar a conex�o com a internet \n");
		printf("2) Um software que protege o computador contra virus \n");
		printf("3) Um tipo de sistema operacional \n");
		printf("4) Um hardware para aumentar a velocidade do computador \n");
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

	printf("Finalizou o jogo. Muitos parabens. \n");
	printf("O seu resultado e: %d pontos \n", resultado);
	printf("Fim. Obrigado por jogar.");	
}
