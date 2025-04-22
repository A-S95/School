      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. array1.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 I PIC 9(2).
       01 num pic 9(1).
       01 MEU-ARRAY.
         05 ELEMENTO PIC 9(3) OCCURS 5 TIMES.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
        DISPLAY "Ex array"

        PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
           DISPLAY "Insira um numero para a pos ", I
           accept ELEMENTO(I)
        END-PERFORM.

        PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
            DISPLAY ELEMENTO(I)
        END-PERFORM.

        STOP RUN.
       END PROGRAM array1.
