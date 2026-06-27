default e2_remetente = False
default e2_link = False
default e2_assunto = False

screen email2_screen():

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

            text "Atualização das notas" style "sky_title"

            text "Escola Estadual" size 18 color "#555555"

            text "Para: esmeralda@skyemail.com" size 15 color "#777777"

            ##################################################
            ## REMETENTE
            ##################################################

            if e2_remetente:

                text "De: secretaria@escola.edu.br" size 16 color "#2E7D32"

            else:

                textbutton "De: secretaria@escola.edu.br":

                    background None

                    text_size 16
                    text_color "#1565C0"
                    text_hover_color "#0D47A1"

                    action SetVariable("e2_remetente", True)

            null height 15

            ##################################################
            ## CORPO
            ##################################################

            text "Olá Esmeralda," size 18

            text "As notas do segundo bimestre já estão disponíveis no portal da escola." size 18

            if e2_assunto:

                text "Não há qualquer caráter de urgência nesta mensagem." size 18 color "#2E7D32"

            else:

                textbutton "Não há qualquer caráter de urgência nesta mensagem.":

                    background None

                    text_size 18
                    text_color "#444444"
                    text_hover_color "#222222"

                    action SetVariable("e2_assunto", True)

            text "Você pode acessar utilizando o link abaixo." size 18

            ##################################################
            ## LINK
            ##################################################

            if e2_link:

                text "https://portal.escola.edu.br" size 18 color "#2E7D32"

            else:

                textbutton "https://portal.escola.edu.br":

                    background None

                    text_size 18
                    text_color "#1565C0"
                    text_hover_color "#0D47A1"

                    action SetVariable("e2_link", True)

            null height 15

            text "Atenciosamente," size 18

            text "Secretaria Escolar" size 18

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

            text "Análise realizada" style "sky_title"

            if not (e2_remetente or e2_link or e2_assunto):

                text "Clique nos elementos importantes para analisá-los."

            if e2_remetente:

                text "✔ O domínio pertence à escola (.edu.br)." color "#2E7D32"

            if e2_assunto:

                text "✔ A mensagem não tenta causar medo ou urgência." color "#2E7D32"

            if e2_link:

                text "✔ O link aponta para o portal oficial da escola." color "#2E7D32"

            ##################################################
            ## CLASSIFICAÇÃO
            ##################################################

            if e2_remetente and e2_link and e2_assunto:

                null height 20

                text "Como você classifica este e-mail?" size 20

                hbox:

                    spacing 20

                    textbutton "🚨 É PHISHING":

                        style "sky_button"
                        text_style "sky_button_text"

                        action [

                            SetVariable("phishing_score", phishing_score + 1),

                            SetVariable("email2_lido", True),

                            SetVariable("email_selecionado", 0)

                        ]

                    textbutton "✓ É SEGURO":

                        style "sky_button"
                        text_style "sky_button_text"

                        action [

                            SetVariable("email2_lido", True),

                            SetVariable("email_selecionado", 0)

                        ]