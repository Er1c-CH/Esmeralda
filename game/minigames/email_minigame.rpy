
label fase3_resultado:

    scene black with fade

    if phishing_score == 0:

        centered "EXCELENTE DETETIVE DIGITAL"
        centered "Você identificou todas as ameaças corretamente."

    elif phishing_score == 1:

        centered "BOM TRABALHO"
        centered "Você cometeu um pequeno erro."

    elif phishing_score == 2:

        centered "ATENÇÃO"
        centered "Você caiu em algumas armadilhas."

    else:

        centered "VULNERÁVEL"
        centered "Seus dados foram comprometidos."

    pause 2.0

    centered "JOGO CONCLUÍDO"

    return

############################################################
##
## SKYMAIL - CAIXA DE ENTRADA
##
############################################################

default email_selecionado = 0

default email1_lido = False
default email2_lido = False
default email3_lido = False

screen email_inbox():

    modal True

    use skymail_window(
    title="SkyMail - Caixa de Entrada",
    largura=980,
    altura=610
    ):

        hbox:

            spacing 0

            ####################################################
            ## MENU LATERAL
            ####################################################

            frame:

                background "#F7F7F7"

                xsize 220
                yfill True

                padding (15,20)

                vbox:

                    spacing 18

                    text "📨 SkyMail" style "sky_title"

                    null height 10

                    text "📥 Caixa de Entrada" style "sky_label"

                    text "⭐ Favoritos" style "sky_label"

                    text "📤 Enviados" style "sky_label"

                    text "🗑 Lixeira" style "sky_label"

                    text "🚫 Spam" style "sky_label"

            ####################################################
            ## LISTA DE EMAILS
            ####################################################

            frame:

                background "#FFFFFF"

                xsize 280
                yfill True

                padding (10,10)

                vbox:

                    spacing 5

                    text "Mensagens" style "sky_title"

                    null height 5

                    button:

                        xfill True

                        background If(email_selecionado == 1, "#EAF2FF", "#FFFFFF")


                        action SetVariable("email_selecionado",1)

                        vbox:

                            spacing 2

                            if email1_lido:
                                text "✔ Banco Central"
                            else:
                                text "● Banco Central"

                            text "Sua conta será bloqueada"

                    button:

                        xfill True

                        background If(email_selecionado == 2, "#EAF2FF", "#FFFFFF")


                        action SetVariable("email_selecionado",2)

                        vbox:

                            spacing 2
                            if email2_lido:
                                text "✔ Escola Estadual"
                            else:
                                text "● Escola Estadual"

                            text "Atualização das notas"

                    button:

                        xfill True

                        background If(email_selecionado == 3, "#EAF2FF", "#FFFFFF")

                        action SetVariable("email_selecionado",3)

                        vbox:

                            spacing 2
                            if email3_lido:
                                text "✔ SkyMail"
                            else:
                                text "● SkyMail"

                            text "Verificação da conta"

            ####################################################
            ## PAINEL DE LEITURA
            ####################################################

            frame:

                background "#FFFFFF"

                xfill True
                yfill True

                padding (25,20)

                if email_selecionado == 0:

                    vbox:

                        spacing 15

                        text "Bem-vinda ao SkyMail" style "sky_title"

                        text "Selecione uma mensagem para começar a análise."

                        if email1_lido and email2_lido and email3_lido:

                            null height 25

                            textbutton "Finalizar análise":

                                style "sky_button"

                                text_style "sky_button_text"

                                action Return()

                elif email_selecionado == 1:

                    use email1_screen

                elif email_selecionado == 2:

                    use email2_screen

                elif email_selecionado == 3:

                    use email3_screen
            