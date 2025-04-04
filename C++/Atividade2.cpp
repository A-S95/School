#include <iostream>  // Biblioteca para manipulação de entrada/saída (cout, etc)

int main() {
    int numA = 20;
    int numB = 30;

    std::cout << "Os valores de A: " << numA << " e B: " << numB << std::endl;

    // Trocar valores de A e B
    
    // numC = numA;
    // numA = numB;
    // numB = numC;
    
    // Maneira mais eficiente (sem variável temporária)
    numA = numA + numB;
    numB = numA - numB;
    numA = numA - numB;

    std::cout << "Os valores de A: " << numA << " e B: " << numB << std::endl;
}

