default e1_remetente = False
default e1_link = False
default e1_urgencia = False

screen email1_screen():

    viewport:

        mousewheel True
        draggable True

        xfill True
        yfill True

        vbox:

            spacing 12

            ##################################################
            ## CABEÇALHO
            ##################################################

            text "Sua conta será bloqueada" style "sky_title"

            text "Banco Central" size 18 color "#555555"

            text "Para: esmeralda@skyemail.com" size 15 color "#777777"

            ###############################################

            if e1_remetente:

                text "De: banco@banco-central-login.xyz" size 16 color "#2E7D32"

            else:

                textbutton "De: banco@banco-central-login.xyz":

                    background None

                    text_size 16
                    text_color "#1565C0"
                    text_hover_color "#0D47A1"

                    action SetVariable("e1_remetente", True)

            null height 15

            ##################################################
            ## CORPO
            ##################################################

            text "Olá Esmeralda," size 18

            text "Detectamos uma atividade suspeita em sua conta." size 18

            if e1_urgencia:

                text "Sua conta será BLOQUEADA em menos de 24 horas." size 18 color "#2E7D32"

            else:

                textbutton "Sua conta será BLOQUEADA em menos de 24 horas.":

                    background None

                    text_size 18
                    text_color "#C62828"
                    text_hover_color "#8E0000"

                    action SetVariable("e1_urgencia", True)

            text "Para evitar o bloqueio clique no link abaixo." size 18

            if e1_link:

                text "https://banco-central-login.xyz" size 18 color "#2E7D32"

            else:

                textbutton "https://banco-central-login.xyz":

                    background None

                    text_size 18
                    text_color "#1565C0"
                    text_hover_color "#0D47A1"

                    action SetVariable("e1_link", True)

            null height 15

            text "Atenciosamente," size 18

            text "Equipe Banco Central" size 18

            ##################################################
            ## DIVISÓRIA
            ##################################################

            null height 15

            frame:

                xfill True

                background "#EAEAEA"

                ysize 2

            ##################################################
            ## PISTAS
            ##################################################

            text "Pistas encontradas" style "sky_title"

            if not (e1_remetente or e1_link or e1_urgencia):

                text "Clique nos elementos suspeitos do e-mail."

            if e1_remetente:

                text "✔ O domínio do remetente não pertence ao Banco Central." color "#2E7D32"

            if e1_urgencia:

                text "✔ Linguagem de urgência é comum em golpes." color "#2E7D32"

            if e1_link:

                text "✔ O link leva para um domínio diferente do oficial." color "#2E7D32"

            ##################################################
            ## CLASSIFICAÇÃO
            ##################################################

            if e1_remetente and e1_link and e1_urgencia:

                null height 20

                text "Como você classifica este e-mail?" size 20

                hbox:

                    spacing 20

                    textbutton "🚨 É PHISHING":

                        style "sky_button"
                        text_style "sky_button_text"

                        action [

                            SetVariable("email1_lido", True),
                            SetVariable("email_selecionado", 0)

                        ]

                    textbutton "✓ É SEGURO":

                        style "sky_button"
                        text_style "sky_button_text"

                        action [

                            SetVariable("phishing_score", phishing_score + 1),
                            SetVariable("email1_lido", True),
                            SetVariable("email_selecionado", 0)

                        ]