#include <stdio.h>
#include <locale.h>

int main() {
    std::setlocale(LC_ALL, "");

    int A = 4, B = 4;
    
    if (A == B)
    {
        std::cout << "O resultado da minha condi��o � verdadeiro" << std::endl;
        std::cout << "A = " << A << std::endl << "B = " << B << std::endl;
    } 
    else
    {
        std::cout << "O resultado da minha condi��o � falso" << std::endl;
        std::cout << "A = " << A << std::endl << "B = " << B << std::endl;
    }
}
