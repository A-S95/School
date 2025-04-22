******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. ficheiros.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT FICHEIRO ASSIGN TO 'ficheiro.txt'
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
            PERFORM ESCRITA.
            PERFORM LEITURA.
            STOP RUN.

           ESCRITA.
      * Escrita do ficheiro
            DISPLAY "Escrita em Ficheiros"
            OPEN OUTPUT FICHEIRO
            MOVE 'Primeira Linha' TO LINHA-FICHEIRO
            WRITE LINHA-FICHEIRO
            MOVE 'Segunda Linha' TO LINHA-FICHEIRO
            WRITE LINHA-FICHEIRO
            CLOSE FICHEIRO.

           LEITURA.
      * Leitura do FICHEIRO
            MOVE 'N' TO EOF-FICHEIRO
            DISPLAY "Leitura em Ficheiros"
            OPEN INPUT FICHEIRO
            PERFORM UNTIL EOF-FICHEIRO = 'S'
               READ FICHEIRO
                   AT END MOVE 'S' TO EOF-FICHEIRO
                   NOT AT END DISPLAY LINHA-FICHEIRO
               END-READ
            END-PERFORM
            CLOSE FICHEIRO.

       END PROGRAM ficheiros.
