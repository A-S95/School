      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: Programa para pedir um numero ao utilizador e mostra o numero no ecrã
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. EX0.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 NUM1 PIC 9(2).

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
            DISPLAY "Hoje esta um fantastico dia para aprender a "
     -     "programar na linguagem cobol"
            DISPLAY "Insira um numero"
            ACCEPT NUM1

            DISPLAY "Numero 1 : " NUM1

            STOP RUN.

       END PROGRAM EX0.
