#include <stdio.h>
#include <locale.h>
#include <stdbool.h>

int main() {
    setlocale(LC_ALL, "");
    
    int num;
    bool is_odd = true; 
    
    printf("App - Par ou impar\n");
    printf("Acaba quando encontrar um numero par.\n\n");
    
    while (is_odd) {
        printf("Indique um número: ");
        scanf("%d", &num);
        
        if (num % 2 == 0) {
            printf("Numero inserido é par\n\n");
            is_odd = false;  // Sai do loop
        } else {
            printf("Numero inserido é impar\n\n");
        }
    }
    
    printf("Inseriu um numero par.\n");
    
    return 0;
}
