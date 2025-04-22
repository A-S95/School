******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. EX_UNTIL.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01  N   PIC 99 VALUE 0.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
         DISPLAY "Exemplo: mostra numeros de 1 a 10  PERFORM UNTIL".
         MOVE 1 TO N
         PERFORM UNTIL N > 10
            DISPLAY "Numero :" N
         ADD 1 TO N
         END-PERFORM.

       END PROGRAM EX_UNTIL.
