******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. Exercicio1.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT FICHEIRO ASSIGN TO 'ficheiro1.txt'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD FICHEIRO.
       01 LINHA-FICHEIRO PIC X(80).

       WORKING-STORAGE SECTION.
       01 EOF-FICHEIRO PIC X VALUE 'N'.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
            PERFORM ESCRITA.
            STOP RUN.

           ESCRITA.
      * Escrita do ficheiro
            DISPLAY "Escrita em Ficheiros"
            DISPLAY "--------------------"
            DISPLAY "PRONTO!"
            OPEN OUTPUT FICHEIRO
            MOVE 'Primeira Linha' TO LINHA-FICHEIRO
            WRITE LINHA-FICHEIRO
            MOVE 'Segunda Linha' TO LINHA-FICHEIRO
            WRITE LINHA-FICHEIRO
            MOVE 'Terceira Linha' TO LINHA-FICHEIRO
            WRITE LINHA-FICHEIRO
            CLOSE FICHEIRO.

       END PROGRAM Exercicio1.
