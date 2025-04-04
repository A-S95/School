#include <iostream>
#include <locale>

int main() {
    std::locale::global(std::locale(""));
    
    int numProdutos;
    float valorCompra;
    const float descontoMax = 2.0f;
    const float valorDescontoMax = 0.5f;
    const float descontoMin = 0.60f;
    const float valorDesconto = 0.4f;
    float resultado;

    std::cout << "APP - Bazar do digital\n";
    std::cout << "As nossas promoções de Primavera\n";
    std::cout << "Na compra de 3 ou mais produtos recebe um desconto de 40%\n";
    std::cout << "Numa compra de valor superior a 100 euros recebe um desconto de 40%\n";
    std::cout << "Numa compra de 3 ou mais produtos e num total de superior a 100€ recebe desconto de 50%\n\n";

    std::cout << "Insira o número de produtos escolhidos: \n";
    std::cin >> numProdutos;
    std::cout << "Valor da compra total: \n";
    std::cin >> valorCompra;

    std::cout << std::fixed << std::setprecision(2);

    if (numProdutos >= 3 && valorCompra > 100) {
        std::cout << "O desconto será de 50% \n";
        resultado = valorCompra / descontoMax;
        float valorDescontadoMax = valorCompra * valorDescontoMax;
        std::cout << "O valor da compra com desconto é: " << resultado << " euros\n";
        std::cout << "O valor descontado foi de: " << valorDescontadoMax << " euros\n";
    } else if (numProdutos >= 3 || valorCompra > 100) {
        std::cout << "O desconto será de 40%\n";
        resultado = valorCompra * descontoMin;
        float valorDescontado = valorCompra * valorDesconto;
        std::cout << "O valor da compra com desconto é: " << resultado << " euros\n";
        std::cout << "O valor descontado foi de: " << valorDescontado << " euros\n";
    } else {
        std::cout << "Sem desconto: " << valorCompra << " euros\n";
    }

    return 0;
}
