init python:

    def calcular_nota(phishing_score):

        # 0 erros = nota máxima
        if phishing_score == 0:
            return 10, "Excelente"

        # 1 erro
        elif phishing_score == 1:
            return 8.5, "Bom"

        # 2 erros
        elif phishing_score == 2:
            return 6.5, "Atenção"

        # 3 erros
        else:
            return 4.0, "Crítico"


screen boletim_digital():

    modal True

    $ nota, nivel = calcular_nota(phishing_score)

    frame:

        xalign 0.5
        yalign 0.5

        xsize 900
        ysize 600

        padding (20, 20)

        vbox:
            spacing 10

            text "📊 Boletim Digital - SkyMail Academy" style "sky_title"

            viewport:

                draggable True
                mousewheel True
                scrollbars "vertical"

                xsize 860
                ysize 520

                vbox:

                    spacing 18

                    ##################################################
                    ## INFO ALUNO
                    ##################################################

                    frame:
                        background "#F5F7FA"
                        padding (15,15)

                        vbox:
                            spacing 5

                            text "Aluno: Esmeralda" size 20
                            text "Avaliação: Segurança Digital" size 18
                            text "Sistema: Prova Prática SkyMail"

                    ##################################################
                    ## NOTA
                    ##################################################

                    frame:
                        background "#EAF2FF"
                        padding (20,20)

                        vbox:
                            spacing 10

                            text "Nota Final" size 22
                            text "[nota] / 10" size 42 color "#1565C0"
                            text "Classificação: [nivel]" size 18

                    ##################################################
                    ## HABILIDADES
                    ##################################################

                    frame:
                        background "#F7F7F7"
                        padding (15,15)

                        vbox:
                            spacing 8

                            text "Habilidades Avaliadas:" size 18

                            text "🔐 Senhas seguras: OK"
                            text "🧠 Engenharia social: OK"
                            text "📧 Phishing: " + ("Excelente" if phishing_score == 0 else "Parcial")

                    ##################################################
                    ## FEEDBACK DETALHADO
                    ##################################################

                    frame:
                        background "#FFFFFF"
                        padding (15,15)

                        vbox:
                            spacing 8

                            if phishing_score == 0:

                                text "✔ Excelente percepção de riscos digitais."
                                text "✔ Identificação precisa de tentativas de phishing."
                                text "✔ Nenhuma falha crítica detectada."

                            elif phishing_score == 1:

                                text "✔ Bom desempenho geral."
                                text "⚠ Pequenos erros em análise de mensagens."

                            elif phishing_score == 2:

                                text "⚠ Atenção necessária."
                                text "⚠ Alguns sinais de phishing não foram percebidos."

                            else:

                                text "⚠ Risco elevado."
                                text "⚠ Necessita reforço em segurança digital."

                    ##################################################
                    ## OBSERVAÇÃO FINAL
                    ##################################################

                    frame:
                        background "#FFF3E0"
                        padding (15,15)

                        vbox:
                            spacing 5

                            text "Observação do Professor:" size 18

                            text "O desempenho reflete sua capacidade de identificar ameaças reais em ambientes digitais."

                    ##################################################
                    ## BOTÃO FINAL
                    ##################################################

                    textbutton "Finalizar Avaliação":

                        xalign 0.5

                        style "sky_button"
                        text_style "sky_button_text"

                        action Return()

label avaliacao_professor:

    scene bg sala_aula

    show professor feliz at esquerda
    show esmeralda feliz at direita

    p "Bom dia, Esmeralda."

    p "Sua avaliação digital já foi processada pelo sistema."

    hide professor feliz
    hide esmeralda feliz

    call screen boletim_digital

    scene black with fade

    centered "FIM DA AVALIAÇÃO"
    pause 2.0

    return