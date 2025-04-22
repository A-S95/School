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
         05 ELEMENTO PIC 9(3) OCCURS 10 TIMES.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
        DISPLAY "Ex array"

        MOVE 33  TO ELEMENTO(1)
        MOVE 44  TO ELEMENTO(2)
        MOVE 55  TO ELEMENTO(3)
        MOVE 66  TO ELEMENTO(4)
        MOVE 77  TO ELEMENTO(5)

        PERFORM VARYING I FROM 1 BY 1 UNTIL I >10
           DISPLAY "Insira um numero para a pos ", I
           accept ELEMENTO(I)
        END-PERFORM.


        PERFORM VARYING I FROM 1 BY 1 UNTIL I > 10
            DISPLAY ELEMENTO(I)
        END-PERFORM.

        STOP RUN.
       END PROGRAM array1.
