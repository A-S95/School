#include <stdio.h>
// 1 Experimentar usar o resto da divis�o com uma vari�vel do tipo float e verificar o resultado.
// 2 Pesquisar e verificar a forma de coo o scanf funciona na linguagem C.
// 3 Passar a aplica��o A4 e A5 para C++.
// 4 Comparar os m�todos de input do C++.

#include <math.h>

// 1 
int main() {
   
   float numUm = 17.0;
   float numDois = 3.0;
   
 //  printf("O resultado do resto e: %f", numUm % numDois); // Erro, nao ha resto em Float numbers, sem ser usado o fmod() + biblioteca math.h. https://www.w3schools.com/c/ref_math_fmod.php
   printf("O resultado do resto e: %f", fmod(numUm, numDois));  
}
