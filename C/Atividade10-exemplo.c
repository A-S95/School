#include <stdio.h>
#include <locale.h>
#include <stdbool.h>

int main() {
    setlocale(LC_ALL, "");
    
    int num;

    printf("App - Par ou impar\n\n");

        printf("Indique um n�mero: "); 
        scanf("%d", &num);
        
        if (num % 2 == 1) 
            printf("Numero inserido � impar\n");
         else 
            printf("Numero inserido � par\n");
    }
