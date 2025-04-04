#include <iostream>
#include <locale>

int main() {
    setlocale(LC_ALL, "");

    float classificacao;
    std::cout << "Insira a classificacao do Aluno \n";
    std::cin >> classificacao;  // Aceita valor feito pelo Utilizador

    std::cout << "App de avaliacao: \n";
    std::cout << " 0 a 7 - Reprovado \n";
    std::cout << " 8 a 9 - Exame \n";
    std::cout << " 10 a 20 - Aprovado \n";

    std::cout << "A classificacao do aluno e: ";
    std::cout << classificacao << "\n";

    if (classificacao >= 10)
        std::cout << "Aluno Aprovado";  // verdadeiro 1
    else if (classificacao >= 8)
        // else if (classificacao > 8 && classificacao < 10) // comparativo entre(&& ||) condicoes
        std::cout << "Aluno vai a Exame";  // verdadeiro 2
    else
        std::cout << "Aluno Reprovado";  // falso

    return 0;
}

