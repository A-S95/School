******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. ex_perform_vaying.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01  N     PIC 9(2).
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
       DISPLAY "Exemplo: Contagem de 1 a 10 utilizando  PERFORM VARYING".
         PERFORM VARYING N FROM 1 BY 3 UNTIL N >10
            DISPLAY "Numero: " N
         END-PERFORM.
        STOP RUN.
       END PROGRAM ex_perform_vaying.
