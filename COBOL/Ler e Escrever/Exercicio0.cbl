      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. Exercicio0.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT FICHEIRO ASSIGN TO 'ficheiro0.txt'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD FICHEIRO.
       01 LINHA-FICHEIRO PIC X(80).

       WORKING-STORAGE SECTION.
       01 NOME-UTILIZADOR     PIC X(20).
       01 EOF-FICHEIRO        PIC X VALUE 'N'.
       01 CONTADOR-LINHAS     PIC 9(2) VALUE ZEROS.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM ESCREVER-NOMES.
           PERFORM LER-FICHEIRO.
           DISPLAY "Número de linhas no ficheiro: " CONTADOR-LINHAS
           STOP RUN.

       ESCREVER-NOMES.
           DISPLAY "Inserir nomes (Digite 'FIM' para terminar):"
           OPEN OUTPUT FICHEIRO

           PERFORM UNTIL NOME-UTILIZADOR = "FIM" OR
           NOME-UTILIZADOR = "fim"
               DISPLAY "Nome: " WITH NO ADVANCING
               ACCEPT NOME-UTILIZADOR
               IF NOME-UTILIZADOR NOT = "FIM" AND
                   NOME-UTILIZADOR NOT = "fim"

                   MOVE NOME-UTILIZADOR TO LINHA-FICHEIRO
                   WRITE LINHA-FICHEIRO
               END-IF
           END-PERFORM

           CLOSE FICHEIRO.

       LER-FICHEIRO.
           MOVE 'N' TO EOF-FICHEIRO
           DISPLAY "Conteúdo do ficheiro:"
           OPEN INPUT FICHEIRO

           PERFORM UNTIL EOF-FICHEIRO = 'S'
               READ FICHEIRO
                   AT END
                       MOVE 'S' TO EOF-FICHEIRO
                   NOT AT END
                       DISPLAY LINHA-FICHEIRO
                       ADD 1 TO CONTADOR-LINHAS
               END-READ
           END-PERFORM

           CLOSE FICHEIRO.
       END PROGRAM Exercicio0.
