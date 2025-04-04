// biblioteca para manipulação de strings (printf,etc)
#include <stdio.h>

int main() {

    int numA = 20;
    int numB = 30;
//  int numC;

    printf("os valores de A: %d e B: %d\n",numA ,numB);

// Trocar valores de A e B
//correto mas nao o mais eficiente
    // numC = numA;
    // numA = numB;
    // numB = numC;

    // maneira mais eficiente
    numA = numA + numB;
    numB = numA - numB;
    numA = numA - numB;

    // \n é uma quebra de linha
    printf("os valores de A: %d e B: %d\n",numA ,numB);
}
