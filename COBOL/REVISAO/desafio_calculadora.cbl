      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. EX_CALCULADORA.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 WS-OPCAO PIC 9 VALUE 9.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM UNTIL WS-OPCAO =0
                DISPLAY "###################"
                DISPLAY "1 - SOMA"
                DISPLAY "2 - SUBTRACAO"
                DISPLAY "3 - MULTIPLICACAO"
                DISPLAY "4 - DIVISAO"
                DISPLAY "0 - SAIR"
                DISPLAY "###################"
                DISPLAY "ESCOLHA UMA OPCAO"
                ACCEPT WS-OPCAO

                EVALUATE WS-OPCAO
                   WHEN 1
                       DISPLAY "Escolheu a soma "
                  WHEN 2
                       DISPLAY "Escolheu subtracao"
                   WHEN 0
                       DISPLAY "Adeus"

                END-EVALUATE

           END-PERFORM
            STOP RUN.
       END PROGRAM EX_CALCULADORA.
