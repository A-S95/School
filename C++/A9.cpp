#include <iostream>
#include <locale>
using namespace std;

int main() {
    setlocale(LC_ALL, "");

    float classificacao = 5;

    cout << "App de avaliacao: " << endl;
    cout << " 0 a 7 - Reprovado " << endl;
    cout << " 8 a 9 - Exame " << endl;
    cout << " 10 a 20 - Aprovado " << endl;

    cout << "A classificacao do aluno e: ";
    cout << fixed << setprecision(2) << classificacao << endl;

    if (classificacao < 8)
        cout << "Aluno Reprovado" << endl; // verdadeiro 1
    else if (classificacao >= 10)
        cout << "Aluno Aprovado" << endl; // verdadeiro 2
    else
        cout << "Aluno vai a Exame" << endl; // falso

    return 0;
}

