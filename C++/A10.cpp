#include <iostream>
#include <locale>

int main() {
    std::locale::global(std::locale(""));
    
    int num;

    std::cout << "App - Par ou impar\n\n";

    std::cout << "Indique um n�mero: ";
    std::cin >> num;
    
    if (num % 2 == 1) 
        std::cout << "Numero inserido � impar\n";
    else 
        std::cout << "Numero inserido � par\n";

    return 0;
}
