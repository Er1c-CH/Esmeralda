default e3_remetente = False
default e3_link = False
default e3_urgencia = False
default e3_botao = False

screen email3_screen():

    viewport:

        mousewheel True
        draggable True

        xfill True
        yfill True

        vbox:

            spacing 12

            ##################################################
            ## CABEÇALHO (FALSO SKYMAIL)
            ##################################################

            text "Confirme sua conta imediatamente" style "sky_title"

            text "SkyMail Suporte" size 18 color "#555555"

            text "Para: esmeralda@skyemail.com" size 15 color "#777777"

            ##################################################
            ## REMETENTE SUSPEITO
            ##################################################

            if e3_remetente:

                text "De: suporte@skymail-seguro.com" size 16 color "#2E7D32"

            else:

                textbutton "De: suporte@skymail-seguro.com":

                    background None

                    text_size 16
                    text_color "#1565C0"
                    text_hover_color "#0D47A1"

                    action SetVariable("e3_remetente", True)

            null height 15

            ##################################################
            ## CORPO DO EMAIL
            ##################################################

            text "Olá Esmeralda," size 18

            text "Detectamos atividade incomum em sua conta SkyMail." size 18

            text "Para evitar o encerramento, confirme seus dados imediatamente." size 18

            ##################################################
            ## URGÊNCIA
            ##################################################

            if e3_urgencia:

                text "Sua conta será encerrada em menos de 12 horas." size 18 color "#2E7D32"

            else:

                textbutton "Sua conta será encerrada em menos de 12 horas.":

                    background None

                    text_size 18
                    text_color "#C62828"
                    text_hover_color "#8E0000"

                    action SetVariable("e3_urgencia", True)

            null height 10

            ##################################################
            ## BOTÃO FALSO (GRANDE ARMADILHA)
            ##################################################

            if e3_botao:

                text "🔐 Verificar Conta Agora" size 20 color "#2E7D32"

            else:

                textbutton "🔐 Verificar Conta Agora":

                    background "#E0E0E0"
                    padding (10,10)

                    text_size 20
                    text_color "#1565C0"
                    text_hover_color "#0D47A1"

                    action SetVariable("e3_botao", True)

            null height 10

            text "Se não reconhecer esta atividade, ignore este e-mail." size 16

            text "Equipe SkyMail Security" size 16

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

            text "Análise de segurança" style "sky_title"

            if not (e3_remetente or e3_link or e3_urgencia or e3_botao):

                text "Analise cuidadosamente os elementos suspeitos."

            if e3_remetente:

                text "✔ O domínio contém 'skymail-seguro.com (não oficial)'." color "#2E7D32"

            if e3_urgencia:

                text "✔ Ameaça de encerramento cria pressão psicológica." color "#2E7D32"

            if e3_botao:

                text "✔ Botões de ação são comuns em golpes de phishing." color "#2E7D32"

            ##################################################
            ## CLASSIFICAÇÃO FINAL
            ##################################################

            if e3_remetente and e3_urgencia and e3_botao:

                null height 20

                text "Qual sua decisão?" size 20

                hbox:

                    spacing 20

                    textbutton "🚨 É PHISHING":

                        style "sky_button"
                        text_style "sky_button_text"

                        action [

                            SetVariable("phishing_score", phishing_score + 1),
                            SetVariable("email3_lido", True),
                            SetVariable("email_selecionado", 0)

                        ]

                    textbutton "✓ É SEGURO":

                        style "sky_button"
                        text_style "sky_button_text"

                        action [

                            SetVariable("email3_lido", True),
                            SetVariable("email_selecionado", 0)

                        ]