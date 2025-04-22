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
       01 MINIMO PIC 9(5).
       01 MAXIMO PIC 9(5).
       01 WS-OPCAO PIC 9(2) VALUE 10.

       01 ESCOLHA PIC 9(2).
       01 VALOR PIC 9(2).

       01 MEU-ARRAY.
         05 ELEMENTO PIC 9(3) OCCURS 10 TIMES.

       01 WS-LINHA PIC X(50) VALUE ALL "-".
       01 WS-LINHA-DUPLA PIC X(50) VALUE ALL "=".

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
        PERFORM UNTIL WS-OPCAO = 0
                DISPLAY WS-LINHA-DUPLA
                DISPLAY "TRABALHO DE COBOL - IEFP 2025"
                DISPLAY WS-LINHA-DUPLA
                DISPLAY "1 - INSERIR"
                DISPLAY "2 - LISTAR"
                DISPLAY "3 - APAGAR"
                DISPLAY "4 - EDITAR"
                DISPLAY "5 - MAIOR"
                DISPLAY "6 - MENOR"
                DISPLAY "0 - SAIR"
                DISPLAY WS-LINHA
                DISPLAY "ESCOLHA UMA OPCAO: "
                ACCEPT WS-OPCAO

                EVALUATE WS-OPCAO
                   WHEN 1
                       DISPLAY "Escolheu o inserir dados "
                       PERFORM INSERIR-VALORES
                   WHEN 2
                       DISPLAY "Escolheu o listar dados "
                       PERFORM LISTAR-VALORES
                   WHEN 3
                       DISPLAY "Escolheu o apagar dados "
                       PERFORM APAGAR-VALORES
                   WHEN 4
                       DISPLAY "Escolheu o editar dados "
                       PERFORM EDITAR-VALORES
                   WHEN 5
                       DISPLAY "Escolheu o maior "
                       PERFORM CALCULA-MAXIMO
                   WHEN 6
                       DISPLAY "Escolheu o menor "
                       PERFORM CALCULA-MINIMO
                   WHEN 0
                       DISPLAY "Obrigado. "
                       DISPLAY "Fim do programa "
                   END-EVALUATE
               DISPLAY WS-LINHA
           END-PERFORM.
       STOP RUN.

       INSERIR-VALORES.
        PERFORM VARYING I FROM 1 BY 1 UNTIL I > 10
           DISPLAY "Insira um numero para a posicao " I
           accept ELEMENTO(I)
        END-PERFORM.

       LISTAR-VALORES.
        PERFORM VARYING I FROM 1 BY 1 UNTIL I > 10
           DISPLAY ELEMENTO(I)
        END-PERFORM.

       APAGAR-VALORES.
           DISPLAY "Escolha a posicao que quer apagar"
           ACCEPT ESCOLHA
           DISPLAY "O valor da posicao " ESCOLHA, "foi alterado para "
           " zero"
           MOVE 0 TO ELEMENTO(ESCOLHA).

       EDITAR-VALORES.
           DISPLAY "Qual a posicao que pretende alterar? "
           ACCEPT ESCOLHA

           DISPLAY "Insira o valor pretendido: "
           ACCEPT VALOR
           MOVE VALOR TO ELEMENTO(ESCOLHA).

       CALCULA-MAXIMO.
           COMPUTE MAXIMO = ELEMENTO(1)
        PERFORM VARYING I FROM 2 BY 1 UNTIL I > 5
           IF ELEMENTO(I) > MAXIMO
               COMPUTE MAXIMO = ELEMENTO(I)
           END-IF
        END-PERFORM.
           DISPLAY WS-LINHA-DUPLA
           DISPLAY "O valor maximo guardado e: " MAXIMO.

       CALCULA-MINIMO.
           COMPUTE MINIMO = ELEMENTO(1)
        PERFORM VARYING I FROM 2 BY 1 UNTIL I > 5
           IF ELEMENTO(I) < MINIMO
               COMPUTE MINIMO = ELEMENTO(I)
           END-IF
        END-PERFORM.
           DISPLAY WS-LINHA-DUPLA
           DISPLAY "O valor minimo guardado e: " MINIMO.

       END PROGRAM array1.
