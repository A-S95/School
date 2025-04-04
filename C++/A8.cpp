#include <stdio.h>
#include <locale.h>

int main() {
    std::setlocale(LC_ALL, "");
    
    int A, B;
    
    std::cout << "Insira o valor a (A B): ";  // passo 1
    std::cin >> A >> B;  // passo 2
    
    // Estrutura condicional
    if (A == B)
        std::cout << "Os valores são iguais" << std::endl;  // passo 3
    else 
        std::cout << "Os valores são diferentes" << std::endl;  // passo 3
    
    std::cout << "Fim";  // passo 4
}
