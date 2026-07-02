init python:

    def calcular_boletim():

        # -----------------------------
        # FASE 1 - SENHAS
        # -----------------------------

        if senha_fraca:
            nota_senha = 1.0
        else:
            nota_senha = 2.0


        # -----------------------------
        # FASE 2 - ENGENHARIA SOCIAL
        # -----------------------------

        nota_social = max(1.0, 4.0 - vulnerabilidade)


        # -----------------------------
        # FASE 3 - PHISHING
        # -----------------------------

        nota_phishing = max(1.0, 4.0 - phishing_score)


        nota_final = nota_senha + nota_social + nota_phishing


        if nota_final >= 9:

            nivel = "Excelente"

        elif nota_final >= 7:

            nivel = "Bom"

        elif nota_final >= 5:

            nivel = "Regular"

        else:

            nivel = "Necessita Reforço"


        return (
            nota_final,
            nivel,
            nota_senha,
            nota_social,
            nota_phishing
        )


screen boletim_digital():

    modal True

    $ nota, nivel, nota_senha, nota_social, nota_phishing = calcular_boletim()

    frame:

        xalign 0.5
        yalign 0.5

        xsize 920
        ysize 620

        padding (20,20)

        vbox:

            spacing 10

            text "📊 Boletim Digital - SkyMail Academy" style "sky_title"

            viewport:

                draggable True
                mousewheel True
                scrollbars "vertical"

                xsize 880
                ysize 540

                vbox:

                    spacing 20

                    ##################################################
                    ## CABEÇALHO
                    ##################################################

                    frame:

                        background "#F5F7FA"

                        padding (20,20)

                        vbox:

                            spacing 6

                            text "Aluno: Esmeralda" size 22

                            text "Professor: Segurança Digital"

                            text "Avaliação: Prova Prática SkyMail"

                            text "Pontuação Máxima: 10 pontos"

                    ##################################################
                    ## NOTA FINAL
                    ##################################################

                    frame:

                        background "#EAF2FF"

                        padding (20,20)

                        vbox:

                            spacing 8

                            text "Nota Final" size 24

                            text "[nota] / 10" size 48 color "#1565C0"

                            text "Classificação: [nivel]" size 20

                    ##################################################
                    ## COMPETÊNCIAS
                    ##################################################

                    frame:

                        background "#F7F7F7"

                        padding (20,20)

                        vbox:

                            spacing 12

                            text "Desempenho por Competência" size 22

                            text "🔐 Criação de Senhas ................ [nota_senha] / 2"

                            bar:
                                value StaticValue(nota_senha)
                                range 2
                                xmaximum 650

                            text "🧠 Engenharia Social ............. [nota_social] / 4"

                            bar:
                                value StaticValue(nota_social)
                                range 4
                                xmaximum 650

                            text "📧 Identificação de Phishing ..... [nota_phishing] / 4"

                            bar:
                                value StaticValue(nota_phishing)
                                range 4
                                xmaximum 650

                    ##################################################
                    ## COMPETÊNCIAS DESENVOLVIDAS
                    ##################################################

                    frame:

                        background "#FFFFFF"

                        padding (20,20)

                        vbox:

                            spacing 8

                            text "Competências Desenvolvidas" size 22

                            text "✔ Criar senhas fortes"

                            text "✔ Reconhecer tentativas de engenharia social"

                            text "✔ Identificar sinais de phishing"

                            text "✔ Tomar decisões seguras na internet"

                    ##################################################
                    ## FEEDBACK
                    ##################################################

                    frame:

                        background "#FFFFFF"

                        padding (20,20)

                        vbox:

                            spacing 10

                            text "Comentários do Professor" size 22

                            ########################################

                            if senha_fraca:

                                text "• Você precisou revisar sua senha antes de atender aos requisitos de segurança."

                            else:

                                text "• Excelente! Sua senha atendeu aos critérios logo na primeira tentativa."

                            ########################################

                            if vulnerabilidade == 0:

                                text "• Você identificou corretamente todas as tentativas de engenharia social."

                            elif vulnerabilidade == 1:

                                text "• Você caiu em apenas uma tentativa de manipulação."

                            elif vulnerabilidade == 2:

                                text "• Algumas situações de engenharia social ainda geraram dúvidas."

                            else:

                                text "• É importante praticar mais a identificação de tentativas de engenharia social."

                            ########################################

                            if phishing_score == 0:

                                text "• Todos os e-mails foram classificados corretamente."

                            elif phishing_score == 1:

                                text "• Apenas um e-mail foi classificado incorretamente."

                            elif phishing_score == 2:

                                text "• Alguns sinais de phishing passaram despercebidos."

                            else:

                                text "• Recomenda-se revisar os principais indícios de phishing."

                    ##################################################
                    ## OBSERVAÇÃO FINAL
                    ##################################################

                    frame:

                        background "#FFF3E0"

                        padding (20,20)

                        vbox:

                            spacing 8

                            text "Observação Final" size 22

                            text "Seu desempenho demonstra sua capacidade de aplicar conhecimentos de segurança digital em situações semelhantes às encontradas no uso cotidiano da internet."

                            text "Continue observando cuidadosamente mensagens, pessoas e solicitações antes de compartilhar informações pessoais."

                    ##################################################
                    ## BOTÃO
                    ##################################################

                    null height 15

                    textbutton "Finalizar Avaliação":

                        xalign 0.5

                        style "sky_button"

                        text_style "sky_button_text"

                        action Return()

                    null height 20

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