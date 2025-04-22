#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main() {
    setlocale(LC_ALL, "");

    int i;
    int a=1;

    for(i=0; i<=100; i++)
    {
        printf("");
    }
    printf("\nApp - Tabuada\n");
    for(i=0; i<=100; i++)
    {
        printf("");
    }
//    tabuada
    printf("\n Tabuada do 1 ao 10\n");
    for(i=1; i<=10; i++){
        for(a=1; a<=10; a++){
            printf("%d X %d = %d\n", i, a, i*a);
        }
        printf("Prima Enter para continuar\n");
        getchar();

    }
}
