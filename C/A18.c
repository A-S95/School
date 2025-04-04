#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	int num, i=1;
	char opc;
	
	printf("App - \"Tabuada\" \n\a");
	inicio:
		
	i= 1;
	printf("Introduza um numero para a tabuada:");
	scanf("%d", &num);
	
	tabuada:
	printf("%d x %d\t = %d\n", num, i, num*i);
	
	i++;
	if (i <= 10)
	goto tabuada;
	
	printf("Deseja realizar uma nova tabuada: ");
	fflush(stdin);
	scanf("%c", &opc);
	if (opc == 's')
	goto inicio;
}
