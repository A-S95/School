      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. EX_PROCEDIMENTO.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
          01 NUM1       PIC 9(4) VALUE 10.
          01 NUM2       PIC 9(4) VALUE 20.
          01 RESULTADO  PIC 9(5).
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
            PERFORM MOSTRA_BARRAS.
            PERFORM MOSTRA_TITULO.
            PERFORM MOSTRA_BARRAS.
            PERFORM CALCULA-SOMA.
            DISPLAY "insira n1 : "
            ACCEPT NUM1
            DISPLAY "insira n~2 : "
            ACCEPT NUM2
            PERFORM VERIFICA_MAIOR.

            STOP RUN.


       CALCULA-SOMA.
          COMPUTE RESULTADO = NUM1 + NUM2.
          DISPLAY "Resultado da soma: " RESULTADO.
       MOSTRA_TITULO.
           DISPLAY "Exemplo procedimento".
       MOSTRA_BARRAS.
           DISPLAY "####################".
       VERIFICA_MAIOR.
           IF NUM1 > NUM2
               DISPLAY "Maior :", NUM1
           ELSE IF NUM2>NUM1
               DISPLAY "Maior :", NUM2
           ELSE
               DISPLAY "numeros iguais".

       END PROGRAM EX_PROCEDIMENTO.
