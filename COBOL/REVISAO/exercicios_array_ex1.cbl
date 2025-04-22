      ******************************************************************
      * Author:
      * Date:
      * Purpose:Exercício1  arrays
      * Elabore um programa em cobol que tenha um array
      * de numeros inteiros com 7 notas
      *
      * Solicite as notas ao utilizador e guarde-as no array
      * Mostre as notas no ecrã
      *
      * Mostre a nota mais alta
      * Mostre a nota mais baixa
      * Mostre quantas notas são positivas >=10
      * Mostre quantas notas são negativas <10

      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. ARRAY_EX1.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 N PIC 9(1).
       01 WS-LISTA-NOTAS.
         05 WS-NOTAS PIC 9(2) OCCURS 7 TIMES.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
            DISPLAY "Exercicio 1 Arrays"
            PERFORM VARYING N FROM 1 BY 1 UNTIL N >7
                DISPLAY "INSIRA A NOTA PARA A POSICAO : " N
                ACCEPT WS-NOTAS(N)
            END-PERFORM

            DISPLAY "LISTA NOTAS"
            PERFORM VARYING N FROM 1 BY 1 UNTIL N >7
               DISPLAY "POS : " N " : "  WS-NOTAS(N)
           END-PERFORM

            STOP RUN.
       END PROGRAM ARRAY_EX1.
