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
       01 NUM1 PIC S9(2).
       01 NUM2 PIC S9(2) .
       01 SOMA PIC S9(3).
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
            DISPLAY "Hoje esta um fantastico dia para aprender a "
     -     "programar na linguagem cobol"
            DISPLAY "Insira um numero 1"
            ACCEPT NUM1
            DISPLAY "Insira um numero 2"
            ACCEPT NUM2
            COMPUTE SOMA=NUM1+NUM2
            DISPLAY "SOMA : " SOMA

            STOP RUN.
       END PROGRAM EX0.
