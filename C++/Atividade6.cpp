#include <iostream>
#include <iomanip>

int main() {
    float valorHora;
    int horaTrabalho;
    float valorTotal;
    float valAlimentacao;

    std::cout << "Indique o valor hora: ";
    std::cin >> valorHora;
    std::cout << "Indique o numero total de horas: ";
    std::cin >> horaTrabalho;
    std::cout << "Indique o valor do alimentacao (por dia): ";
    std::cin >> valAlimentacao;

    valorTotal = (valorHora + (valAlimentacao / 8)) * horaTrabalho;

    std::cout << "Resumo:" << std::endl;
    std::cout << "Valor hora: " << std::fixed << std::setprecision(2) << valorHora << " euros" << std::endl;
    std::cout << "Total de Horas: " << horaTrabalho << std::endl;
    std::cout << "Custo do projeto: " << std::fixed << std::setprecision(2) << valorTotal << std::endl;

}
