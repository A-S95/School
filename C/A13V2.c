#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "");
    int mes;
    char* nome_mes;
    
    printf("App - Dias do Mes \n");
    printf("Introduza o mes (1 a 12): \n");
    scanf("%d", &mes);
    
    if (mes == 1)
        nome_mes = "Janeiro";
    else if (mes == 2)
        nome_mes = "Fevereiro";
    else if (mes == 3)
        nome_mes = "Marco";
    else if (mes == 4)
        nome_mes = "Abril";
    else if (mes == 5)
        nome_mes = "Maio";
    else if (mes == 6)
        nome_mes = "Junho";
    else if (mes == 7)
        nome_mes = "Julho";
    else if (mes == 8)
        nome_mes = "Agosto";
    else if (mes == 9)
        nome_mes = "Setembro";
    else if (mes == 10)
        nome_mes = "Outubro";
    else if (mes == 11)
        nome_mes = "Novembro";
    else if (mes == 12)
        nome_mes = "Dezembro";
    else
        nome_mes = "invalido";
    
    switch (mes) {    
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            printf("O mes %s tem 31 dias\n", nome_mes);
            break;
        case 2:
            printf("O mes %s tem 28/29 dias\n", nome_mes);
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            printf("O mes %s tem 30 dias\n", nome_mes);
            break;
        default:
            printf("Mes invalido. Valores entre 1 e 12\n");
    }
    
    printf("Fim da app.");
}
