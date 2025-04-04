#include <stdio.h>
#include <locale.h>

int main() {
	
	setlocale(LC_ALL, "");
	int menu;
	
	printf("App - Menu\n");
	//goto
	menu:
		printf("Escolha a opcao (1(sair) || 2 || 3): ");
		scanf("%d", &menu);
		
		if(menu == 1){
			printf("Opcao A \n");
		} else if (menu == 2) {
			printf("Opcao B \n");
			goto menu;
		} else if ( menu == 3) {
			printf("Opcao C \n");
			goto menu;
		} else if (menu > 3) {
			printf("Opcao nao existente \n");
			goto menu;
		}
		
		printf("App - Menu a sair.");
}

