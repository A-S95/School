#include <stdio.h>

int main() {
  
  //int numUm, numDois, numRes, numSom, numMul, numSub, numDiv;
  //int numDois;
  int numUm, numDois;
  
//  printf("Insira o primeiro valor: ");
//  scanf("%d", &numUm);
//  printf("Insira o segundo valor: ");
//  scanf("%d", &numDois);

////////// otimizado ////////////////
	printf("Insira dois valores: \n");
	scanf("%d %d", &numUm, &numDois);
	
  //Operadores Aritmeticos + - / * %
//  numRes = numUm % numDois; // resto
//  numSom = numUm + numDois; // soma
//  numMul = numUm * numDois; // multiplicacao
//  numSub = numUm - numDois; // subtracao
//  numDiv = numUm / numDois; // divisao
  
  
  // Otimizado //
  printf("O Resultado do resto da divisao e: %d\n", numUm % numDois);
  printf("O Resultado da soma e: %d\n", numUm + numDois);
  printf("O Resultado da multiplicacao e: %d\n",numUm * numDois);
  printf("O Resultado da subtracao e: %d\n", numUm - numDois);
  printf("O Resultado da divisao e: %d\n", numUm / numDois);
}
