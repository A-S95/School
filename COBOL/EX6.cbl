******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. EX_PERFORM_TIMES.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01  N     PIC 99 VALUE 1.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
        PERFORM 5 TIMES
            DISPLAY "Numero: " N
            ADD 1 TO N
        END-PERFORM.
            STOP RUN.
       END PROGRAM EX_PERFORM_TIMES.
