******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. Exercicio3.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT FICHEIRO ASSIGN TO 'ficheiro3.txt'
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
      * Escrita no ficheiro sem apagar o conteúdo
            DISPLAY "Escrita em Ficheiros (sem apagar)"
            DISPLAY "--------------------"
            DISPLAY "PRONTO!"
            OPEN EXTEND FICHEIRO
            MOVE 'Primeira Linha' TO LINHA-FICHEIRO
            WRITE LINHA-FICHEIRO
            MOVE 'Segunda Linha' TO LINHA-FICHEIRO
            WRITE LINHA-FICHEIRO
            MOVE 'Terceira Linha' TO LINHA-FICHEIRO
            WRITE LINHA-FICHEIRO
            CLOSE FICHEIRO.


       END PROGRAM Exercicio3.
