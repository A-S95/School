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
       01 AUX PIC 9(2).
       01 SOMA  PIC 9(5) VALUE 0.
       01 MEDIA PIC 9(5).
       01 MINIMO PIC 9(5).
       01 MAXIMO PIC 9(5).
       01 WS-OPCAO PIC 9 VALUE 9.

       01 MEU-ARRAY.
         05 ELEMENTO PIC 9(3) OCCURS 5 TIMES.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
        PERFORM UNTIL WS-OPCAO = 0
                DISPLAY "###################"
                DISPLAY "1 - SOMA"
                DISPLAY "2 - MAXIMO"
                DISPLAY "3 - MINIMO"
                DISPLAY "4 - MEDIA"
                DISPLAY "5 - CRIAR ARRAY"
                DISPLAY "6 - MOSTRAR ARRAY"
                DISPLAY "0 - SAIR"
                DISPLAY "###################"
                DISPLAY "ESCOLHA UMA OPCAO"
                ACCEPT WS-OPCAO

                EVALUATE WS-OPCAO
                   WHEN 1
                       DISPLAY "Escolheu a soma "
                       PERFORM CALCULA-SOMA
                   WHEN 2
                       DISPLAY "Escolheu o valor maximo "
                       PERFORM CALCULA-MAXIMO
                   WHEN 3
                       DISPLAY "Escolheu o valor minimo "
                       PERFORM CALCULA-MINIMO
                   WHEN 4
                       DISPLAY "Escolheu a media "
                       PERFORM CALCULA-MEDIA
                   WHEN 5
                       DISPLAY "CRIAR ARRAY "
                       PERFORM CONSTRUIR-ARRAY
                   WHEN 6
                       DISPLAY "Escolheu mostrar o Array "
                       PERFORM MOSTRAR-ARRAY
                   WHEN 0
                       DISPLAY "ADEUS "

                   END-EVALUATE

           END-PERFORM.
       STOP RUN.

       CONSTRUIR-ARRAY.
        PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
           DISPLAY "Insira um numero para a pos " I
           accept ELEMENTO(I)
        END-PERFORM.

       MOSTRAR-ARRAY.
        PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
           DISPLAY ELEMENTO(I)
        END-PERFORM.


       CALCULA-SOMA.
        PERFORM VARYING AUX FROM 1 BY 1 UNTIL AUX > 5
           COMPUTE SOMA = SOMA + ELEMENTO(AUX)
        END-PERFORM.
           DISPLAY SOMA.

       CALCULA-MEDIA.
        PERFORM VARYING AUX FROM 1 BY 1 UNTIL AUX > 5
           COMPUTE SOMA = SOMA + ELEMENTO(AUX)
        END-PERFORM.
         COMPUTE MEDIA = SOMA / 5
         DISPLAY "Resultado da media: " MEDIA.

       CALCULA-MAXIMO.
           COMPUTE MAXIMO = ELEMENTO(1)
        PERFORM VARYING I FROM 2 BY 1 UNTIL I > 5
           IF ELEMENTO(I) > MAXIMO
               COMPUTE MAXIMO = ELEMENTO(I)
           END-IF
        END-PERFORM.
           DISPLAY "Resultado da media: " MAXIMO.

       CALCULA-MINIMO.
           COMPUTE MINIMO = ELEMENTO(1)
        PERFORM VARYING I FROM 2 BY 1 UNTIL I > 5
           IF ELEMENTO(I) < MINIMO
               COMPUTE MINIMO = ELEMENTO(I)
           END-IF
        END-PERFORM.

           DISPLAY "O valor minimo e: " MINIMO.

       END PROGRAM array1.
