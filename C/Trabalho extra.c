#include <stdio.h>
#include <locale.h>


int pergunta1(){
	printf("\n1. Quantos planetas fazem do Sistema Solar (Plutão está fora)\n");
  	printf("a) 3\n");
  	printf("b) 5\n");
  	printf("c) 12\n");
  	printf("d) 8\n");
  	printf("Sua resposta: ");
}

int main() {
	setlocale(LC_ALL, "");
	
  int pontuacao = 0;
  int oportunidades = 3; // Número de oportunidades para errar
  char resposta; // Guarda a resposta do jogador

  printf("Bem-vindo ao Quiz de Múltipla Escolha com Oportunidades!\n");
  
  printf("QUADRO DE JOGO:\n");
  printf("Responda até 6 perguntas\n");
  printf("Tem 3 oportunidades de errar\n");
  printf("Se errar 3 vezes, perde o jogo\n");
  
	// primeira pergunta:
  pergunta1();
  scanf(" %c", &resposta);

// verifica a resposta do utilizador
	switch (resposta) {
		case 'd':
			printf("Correto!\n");
    		pontuacao++;
    		printf("Oportunidades restantes: %d\n", oportunidades);
    	case 'a':
    	case 'b':
    	case 'c':
    		printf("Incorreto. A resposta correta é d) Oito planetas.\n");
    		oportunidades--;
			printf("Oportunidades restantes: %d\n", oportunidades);
		}


// Verifica se ainda há oportunidades
  if (oportunidades > 0) { 
    printf("\n2. Qual o maior planeta do Sistema Solar?\n");
    printf("a) Terra\n");
    printf("b) Júpiter\n");
    printf("c) Marte\n");
    printf("d) Vênus\n");
    printf("Sua resposta: ");
    scanf(" %c", &resposta);

  if (resposta == 'b' | resposta == 'B') {
      printf("Correto!\n");
      pontuacao++;
      printf("Oportunidades restantes: %d\n", oportunidades);
    } else {
      printf("Incorreto. A resposta correta é b) Júpiter.\n");
      oportunidades--;
      printf("Oportunidades restantes: %d\n", oportunidades);
    }
  }

  if (oportunidades > 0) { // Verifica se ainda há oportunidades
      printf("\n3. Qual é o nome da nossa Galáxia?\n");
      printf("a) Monte Real\n");
      printf("b) Láctea\n");
      printf("c) Plutão Fora\n");
      printf("d) Donatello\n");
      printf("Sua resposta: ");
      scanf(" %c", &resposta);

      if (resposta == 'b' | resposta == 'B') {
          printf("Correto!\n");
          pontuacao++;
          printf("Oportunidades restantes: %d\n", oportunidades);
      } else {
          printf("Incorreto. A resposta correta é b) Via Láctea.\n");
          oportunidades--;
          printf("Oportunidades restantes: %d\n", oportunidades);
      }
  }

  if (oportunidades > 0) { // Verifica se ainda há oportunidades
      printf("\n4. Qual é o objeto mais denso?\n");
      printf("a) Estrela\n");
      printf("b) Planeta \n");
      printf("c) Aneis de Saturno\n");
      printf("d) Buraco negro\n");
      printf("Sua resposta: ");
      scanf(" %c", &resposta);

      if (resposta == 'd' | resposta == 'D') {
          printf("Correto!\n");
          pontuacao++;
          printf("Oportunidades restantes: %d\n", oportunidades);
      } else {
          printf("Incorreto. A resposta correta é d) Buraco Negro.\n");
          oportunidades--;
          printf("Oportunidades restantes: %d\n", oportunidades);
      }
  }

  if (oportunidades > 0) { // Verifica se ainda há oportunidades
      printf("\n5. Quantas luas tem o planeta Terra?\n");
      printf("a) Duas\n");
      printf("b) Cinco\n");
      printf("c) Uma\n");
      printf("d) Nenhuma\n");
      printf("Sua resposta: ");
      scanf(" %c", &resposta);

      if (resposta == 'c' | resposta == 'C') {
          printf("Correto!\n");
          pontuacao++;
          printf("Oportunidades restantes: %d\n", oportunidades);
      } else {
          printf("Incorreto. A resposta correta é c) Uma Lua.\n");
          oportunidades--;
          printf("Oportunidades restantes: %d\n", oportunidades);
      }
  }

 if (oportunidades > 0) { // Verifica se ainda há oportunidades
      printf("\n6. Na categoria de estrela, o Sol é considerado uma estrela: ______ ?\n");
      printf("a) Grande\n");
      printf("b) Pequena\n");
      printf("Sua resposta: ");
      scanf(" %c", &resposta);

      if (resposta == 'b' | resposta == 'B') {
          printf("Correto!\n");
          pontuacao++;
          printf("Oportunidades restantes: %d\n", oportunidades);
      } else {
          printf("Incorreto. A resposta correta é b) Pequena.\n");
          oportunidades--;
    	  printf("Oportunidades restantes: %d\n", oportunidades);
      }
  }

  printf("\nSua pontuação final: %d de 6\n", pontuacao);
  printf("Oportunidades restantes: %d\n", oportunidades);
  printf("Perdeu o jogo. Obrigado por jogar \n");

  if(oportunidades == 0){
     // printf("Você perdeu todas as oportunidades.\n");
  }

  return 0;
}
