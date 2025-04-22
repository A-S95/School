******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: Programa para pedir um numero ao utilizador e mostra o numero no ecrã
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. EX7.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 OPCAO PIC S9(1) VALUES 1.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

           PERFORM UNTIL OPCAO = 0
            DISPLAY "Exemplo EVALUATE"
            DISPLAY "###############"
            DISPLAY "# 1 - Inserir #"
            DISPLAY "# 2 - Listar  #"
            DISPLAY "# 0 - Sair    #"
            DISPLAY "###############"
            DISPLAY "Insira a sua escolha : "
            ACCEPT OPCAO
            EVALUATE OPCAO
               WHEN 1
                  DISPLAY "Escolheu Inserir"
               WHEN 2
                  DISPLAY "Escolheu Listar"
               WHEN 0
                  DISPLAY "Adeus"
               WHEN OTHER
                  DISPLAY "Escolheu uma opcao invalida"
            END-EVALUATE
            END-PERFORM.
            STOP RUN.
       END PROGRAM EX7.
