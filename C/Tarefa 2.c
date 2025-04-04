#include <stdio.h>
#include <locale.h>

int menu(){
	printf("Bem vindos ao Quiz ADN \n");
	printf("=====================================\n");
    printf("            REGRAS DO QUIZ           \n");
    printf("=====================================\n");
    printf("1 - Responda a 10 perguntas! No fim de cada pergunta, se errar, irá ter uma questão bónus! \n");
    printf("2 - 4 opções em cada pergunta, apenas 1 está correta. \n");
    printf("3 - Cada pergunta vale 20 pontos. \n");
    printf("4 - Caso erre a pergunta, haverá uma questão bónus que vale 10 pontos. \n");
    printf("5 - Cada questao bónus vale 10 pontos. \n");
    printf("6 - Ao errar a pergunta + a questão bónus, o jogo termina e fica só com os pontos até aí acumulados. \n");
    printf("Pontuação máxima = 200 pontos || 10 perguntas = 20 pontos cada | 10 questões bónus = 10 pontos cada. \n");
}

int pergunta1() {
	printf("O que significa a sigla CPU? \n");
	printf("1) Central Processing Unit \n");
	printf("2) Computer Personal Unit \n");
	printf("3) Control Processing Unit \n");
	printf("4) Central Personal Unit \n");
	printf("A sua resposta: ");
}

int pergunta2() {
	printf("Qual é a função principal do sistema operacional? \n");
	printf("1) Proteger o computador de vírus \n");
	printf("2) Gerenciar os recursos do computador \n");
	printf("3) Criar documentos de texto \n");
	printf("4) Acelerar a conexão com a internet \n");
	printf("A sua resposta: ");
}

int pergunta3() {
	printf("Qual é a diferença entre hardware e software? \n");
	printf("1) Hardware é físico, software é lógico/programas \n");
	printf("2) Hardware é gratuito, software é pago \n");
	printf("3) Hardware é para jogos, software é para trabalho \n");
	printf("4) Hardware é interno, software é externo \n");
	printf("A sua resposta: ");
}

int pergunta4() {
	printf("O que é um vírus de computador? \n");
	printf("1) Um problema físico no disco rígido \n");
	printf("2) Um software malicioso que pode danificar o computador \n");
	printf("3) Um erro do sistema operacional \n");
	printf("4) Um programa para limpar arquivos \n");
	printf("A sua resposta: ");
}

int pergunta5() {
	printf("O que é uma impressora? \n");
	printf("1) Um dispositivo que digitaliza documentos \n");
	printf("2) Um dispositivo que imprime documentos físicos \n");
	printf("3) Um software para criar documentos \n");
	printf("4) Um componente interno do computador \n");
	printf("A sua resposta: ");
}

int pergunta6() {
	printf("O que é um backup? \n");
	printf("1) Um tipo de vírus \n");
	printf("2) Uma atualização do sistema operacional \n");
	printf("3) Uma cópia de segurança de arquivos \n");
	printf("4) Um dispositivo de entrada de dados \n");
	printf("A sua resposta: ");
}

int pergunta7() {
	printf("O que é armazenamento em nuvem? \n");
	printf("1) Armazenar dados em disquetes antigos \n");
	printf("2) Armazenar dados em servidores remotos acessíveis pela internet \n");
	printf("3) Um tipo de disco rígido especial \n");
	printf("4) Um programa para compactar arquivos \n");
	printf("A sua resposta: ");
}

int pergunta8() {
	printf("O que significa a sigla HTML? \n");
	printf("1) High Technical Modern Language \n");
	printf("2) Hyper Text Markup Language \n");
	printf("3) Hard Text Memory Link \n");
	printf("4) Hybrid Technical Machine Language \n");
	printf("A sua resposta: ");
}

int pergunta9() {
	printf("O que é um sistema binário? \n");
	printf("1) Um sistema que usa apenas os números 0 e 1 \n");
	printf("2) Um sistema com dois monitores conectados \n");
	printf("3) Um sistema operacional com duas versões \n");
	printf("4) Um computador com dois processadores \n");
	printf("A sua resposta: ");
}

int pergunta10() {
	printf("Qual é a função principal do teclado? \n");
	printf("1) Mostrar imagens na tela \n");
	printf("2) Processar informações \n");
	printf("3) Inserir dados no computador \n");
	printf("4) Armazenar arquivos importantes \n");
	printf("A sua resposta: ");
}

int main() {
	setlocale(LC_ALL, "");
	
	// Variaveis
	int questionario;
	int pontuacao = 20;
	int bonus = 10;
	int resultado = 0;
	int game_over = 0;  // Variável para controlar o jogo
		
	menu();
	printf("\n");
	printf("Que comece o jogo \n");
	printf("\n");
					
	pergunta1();				
	scanf("%d", &questionario);
	
	
	if (questionario > 4 || questionario < 0)  
		printf("Resposta invalida.");
	else {
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
			printf("O que é uma rede Wi-Fi? \n");
			printf("1) Um cabo para conectar dispositivos \n");
			printf("2) Uma rede sem fio para conectar dispositivos à internet \n");
			printf("3) Um programa para editar vídeos \n");
			printf("4) Um tipo de sistema operacional \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);
	
			switch (questionario) {
				case 2:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;
				case 1:
				case 3:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
					break;
				default:
					printf("Numero que inseriu é inválido.");
		}
	}
	
	 if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; // Encerra o programa
    }
	
		pergunta2();				
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
			printf("O que é um software? \n");
			printf("1) Um componente físico do computador\n");
			printf("2) Uma peça de metal dentro do computador \n");
			printf("3) Um programa ou aplicativo de computador \n");
			printf("4) Um tipo de cabo para conectar dispositivos \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);
	
			switch (questionario) {
				case 3:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;
				case 1:
				case 2:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
					break;
				default:
					printf("Numero que inseriu é inválido.");
			}		
		}	
	
	 if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; // Encerra o programa
    }
	
		pergunta3();
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
			printf("O que é um arquivo PDF? \n");
			printf("1) Um tipo de vírus de computador \n");
			printf("2) Um formato de arquivo para documentos digitais \n");
			printf("3) Um programa para editar fotos \n");
			printf("4) Um tipo de hardware para impressão \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);
			
			switch (questionario) {
				case 2:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;		
				case 1:
				case 3:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
				default:
					printf("Numero que inseriu é inválido.");
			}		
		}		
	
	 if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; // Encerra o programa
    }
	
		pergunta4();
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
			printf("Qual é a função do mouse? \n");
			printf("1) Digitalizar documentos \n");
			printf("2) Processar dados \n");
			printf("3) Apontar e selecionar elementos na tela \n");
			printf("4) Armazenar informações \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);
	
			switch (questionario) {
				case 3:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;
				case 1:
				case 2:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
				default:
					printf("Numero que inseriu é inválido.");
			}		
		}		
	
	 if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; // Encerra o programa
    }
	
	pergunta5();
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
			printf("O que é um pendrive? \n");
			printf("1) Um dispositivo de armazenamento portátil \n");
			printf("2) Um tipo de processador \n");
			printf("3) Um software de segurança \n");
			printf("4) Um cabo para conectar monitores \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);
	
			switch (questionario) {
				case 1:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;
				case 2:
				case 3:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
				default:
					printf("Numero que inseriu é inválido.");
			}		
		}			
	
	 if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; // Encerra o programa
    }
	
		pergunta6();
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
			printf("O que é um e-mail? \n");
			printf("1) Um tipo de vírus \n");
			printf("2) Um serviço de correio eletrônico \n");
			printf("3) Um programa de edição de imagens \n");
			printf("4) Um dispositivo de armazenamento \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);
	
	
			switch (questionario) {
				case 2:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;
				case 1:
				case 3:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
				default:
					printf("Numero que inseriu é inválido.");				
			}		
		}	
	
	 if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; // Encerra o programa
    }
	
		pergunta7();
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
			printf(" O que é um smartphone? \n");
			printf("1) Um telemovel com funções avançadas semelhantes às de um computador \n");
			printf("2) Um tipo especial de mouse \n");
			printf("3) Um programa para fazer ligações pelo computador \n");
			printf("4) Um dispositivo apenas para jogos \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);
	
	
			switch (questionario) {
				case 1:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;
				case 2:
				case 3:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
				default:
					printf("Numero que inseriu é inválido.");
			}		
		}
	
	 if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; // Encerra o programa
    }
	
		pergunta8();
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
			printf(" O que é uma Motherboard? \n");
			printf("1) Um dispositivo de armazenamento externo \n");
			printf("2) Um software para controle do computador \n");
			printf("3) A placa principal onde os componentes do computador são conectados \n");
			printf("4) Um tipo de monitor de computador \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);
	
			switch (questionario) {
				case 3:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;
				case 1:
				case 2:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
				default:
					printf("Numero que inseriu é inválido.");
			}		
		}	
	
	 if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; // Encerra o programa
    }
	
		pergunta9();
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
	
			switch (questionario) {
				case 1:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;
				case 2:
				case 3:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
				default:
					printf("Numero que inseriu é inválido.");				
			}		
		}		
		
		if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; // Encerra o programa
    	}
		
		pergunta10();	
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
			printf(" O que é um programa antivírus? \n");
			printf("1) Um dispositivo para melhorar a conexão com a internet \n");
			printf("2) Um software que protege o computador contra virus \n");
			printf("3) Um tipo de sistema operacional \n");
			printf("4) Um hardware para aumentar a velocidade do computador \n");
			printf("A sua resposta: ");
			scanf("%d", &questionario);
	
			switch (questionario) {
				case 2:
					printf("Acertou!!! \n");
					resultado = resultado + bonus;
					printf("Pontuacao: ");
					printf("Tem %d pontos \n", resultado);
					printf("\n");
					break;
				case 1:
				case 3:
				case 4:
					printf("Falhou a pergunta bonus. \n");
					game_over = 1; // O jogo termina
					printf("\n");
				default:
					printf("Numero que inseriu é inválido.");	
			}		
		}	
		
		if (game_over) {
        printf("O jogo terminou. Sua pontuação final é: %d pontos.\n", resultado);
        printf("Fim. Obrigado por jogar.\n");
        return 0; 
    }	
	
		printf("Finalizou o jogo. Muitos parabens. \n");
		printf("O seu resultado e: %d pontos \n", resultado);
		printf("Fim. Obrigado por jogar.");	
}
}
