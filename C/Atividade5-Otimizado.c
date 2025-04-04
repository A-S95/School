#include <stdio.h>

int main(){

//  int numUm, numDois, numRes, numSom, numMul, numSub, numDiv;
//  int numUm, numDois, numRes;
  int numUm, numDois;

//  printf("Insira o primeiro o valor: ");
//  scanf("%d", &numUm);
//  printf("Insira o segundo valor: ");
//  scanf("%d", &numDois);
  printf("Insira dois valores:");
  scanf("%d %d", &numUm, &numDois);

  // Operadores aritm�ticos + / - * %
//  numRes = numUm % numDois;
//  numSom = numUm + numDois;
//  numMul = numUm * numDois;
//  numSub = numUm - numDois;
//  numDiv = numUm / numDois;

//  numRes = numUm % numDois;
  printf("O resultado do resto da divisao: %d\n", numUm % numDois);
//  numRes = numUm + numDois;
  printf("O resultado da soma: %d\n", numUm + numDois);
//  numRes = numUm * numDois;
  printf("O resultado da multiplicacao: %d\n", numUm * numDois);
//  numRes = numUm - numDois;
  printf("O resultado da subtracao: %d\n", numUm - numDois);
//  numRes = numUm / numDois;
  printf("O resultado da divisao: %d\n", numUm / numDois);
}


