******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: Programa para pedir um numero ao utilizador e mostra o numero no ecrã
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. EX2.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 NUM1 PIC S9(2).

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
            DISPLAY "Hoje esta um fantastico dia para aprender a "
     -     "programar na linguagem cobol"
            DISPLAY "Insira um numero 1"
            ACCEPT NUM1
            IF NUM1 >=0 THEN
               IF NUM1=0 THEN
                   DISPLAY "Numero ZERO"
               ELSE
                   DISPLAY "Numero positivo"
            ELSE
               DISPLAY "Numero negativo"
            END-IF.

            STOP RUN.
       END PROGRAM EX2.
