#include <iostream>
#include <locale>

int main() {
    std::locale::global(std::locale(""));
    
    // variáveis
    int ano;
 
    // inputs / outputs
    std::cout << "App - Ano bissexto\n";
    std::cout << "Descubra se o ano é Bissexto\n";
    std::cout << "Introduza o ano que pretende saber: ";
    std::cin >> ano;
 
    // Estrutura Condicional
    if (ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0)
        std::cout << "O ano " << ano << " é bissexto.\n";
    else
        std::cout << "O ano " << ano << " não é bissexto.\n";

    return 0;
}
