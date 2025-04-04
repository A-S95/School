#include <iostream>
#include <iomanip>
#include <locale>

int main() {
    std::locale::global(std::locale(""));
    
    float classificacao;
    std::cout << "Insira a classificacao do Aluno: ";
    std::cin >> classificacao;
    
    std::cout << "App de avaliacao:\n";
    std::cout << " 0 a 7 - Reprovado\n";
    std::cout << " 8 a 9 - Exame\n";
    std::cout << " 10 a 18 - Aprovado\n";
    std::cout << "19 a 20 - Excelente\n";
    
    std::cout << "A classificacao do aluno e: ";
    std::cout << std::fixed << std::setprecision(2) << classificacao << std::endl;
    
    if (classificacao > 18)
        std::cout << "Aluno Excelente";
    else if (classificacao >= 10)
        std::cout << "Aluno Aprovado";
    else if (classificacao < 8)
        std::cout << "Aluno Reprovado";
    else
        std::cout << "Aluno vai a Exame";
    
    return 0;
}
