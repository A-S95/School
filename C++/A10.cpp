#include <iostream>
#include <locale>

int main() {
    std::locale::global(std::locale(""));
    
    int num;

    std::cout << "App - Par ou impar\n\n";

    std::cout << "Indique um número: ";
    std::cin >> num;
    
    if (num % 2 == 1) 
        std::cout << "Numero inserido é impar\n";
    else 
        std::cout << "Numero inserido é par\n";

    return 0;
}
