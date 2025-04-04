#include <iostream>  // Biblioteca para manipula��o de entrada/sa�da (cout, etc)

int main() {
    int numA = 20;
    int numB = 30;

    std::cout << "Os valores de A: " << numA << " e B: " << numB << std::endl;

    // Trocar valores de A e B
    
    // numC = numA;
    // numA = numB;
    // numB = numC;
    
    // Maneira mais eficiente (sem vari�vel tempor�ria)
    numA = numA + numB;
    numB = numA - numB;
    numA = numA - numB;

    std::cout << "Os valores de A: " << numA << " e B: " << numB << std::endl;
}

