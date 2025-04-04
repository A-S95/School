#include <stdio.h>
#include <locale.h>

int main() {
//#include <locale.h>     Ambas para aceitar linguagem PT ( UTF-8 )
//setlocale(LC_ALL,"");

//	Operadores relacionais
//	 == A == B (A igual a B?)
//    != A != B (A diferente de B?)
//    >  A > B (A e maior que B?)
//    >= A >= B (A e maior ou igual que B?)
//    <  A < B (A e menor que B?)
//    <= A <= B (A e menor ou igual que B?)

//	Estrutura Condicional
//	if(condicao)
//	verdadeiro
//	else
//	falso
//	
//	Estrutura Condicional
//	if(condicao) 
//	{ verdadeiro }
//	else 
//	{ falso	}

setlocale(LC_ALL,"");

	int A=4, B=4;
	
	if (A == B)
	{
	
		printf("O resultado da minha condicao é verdadeiro\n");
		printf("A = %d\nB = %d\n", A, B);
	} 
	else
	{
		printf("O resultado da minha condicao é falso\n");
		printf("A = %d\nB = %d\n", A, B);
	}
}
