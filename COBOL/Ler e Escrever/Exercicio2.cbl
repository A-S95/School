******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. Exercicio2.
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
            PERFORM LEITURA.
            STOP RUN.

           LEITURA.
      * Leitura do FICHEIRO
            MOVE 'N' TO EOF-FICHEIRO
            DISPLAY "Leitura em Ficheiros"
            DISPLAY "--------------------"
            OPEN INPUT FICHEIRO
            PERFORM UNTIL EOF-FICHEIRO = 'S'
               READ FICHEIRO
                   AT END MOVE 'S' TO EOF-FICHEIRO
                   NOT AT END DISPLAY LINHA-FICHEIRO
               END-READ
            END-PERFORM
            CLOSE FICHEIRO.

       END PROGRAM Exercicio2.
