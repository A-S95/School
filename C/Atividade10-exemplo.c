#include <stdio.h>
#include <locale.h>
#include <stdbool.h>

int main() {
    setlocale(LC_ALL, "");
    
    int num;

    printf("App - Par ou impar\n\n");

        printf("Indique um número: "); 
        scanf("%d", &num);
        
        if (num % 2 == 1) 
            printf("Numero inserido é impar\n");
         else 
            printf("Numero inserido é par\n");
    }
