label fase3_login:

    scene bg tela_computador with fade

    $ senha_login = ""
    $ login_falhou = False
    $ login_ok = False
    $ tentativas_login = 3

    while tentativas_login > 0 and not login_ok:

        $ resultado = renpy.call_screen("login_skyemail")

        if resultado == "login":

            if senha_login.strip() == senha_cadastrada.strip():

                $ login_ok = True

            else:

                $ tentativas_login -= 1
                $ login_falhou = True
                $ senha_login = ""

    if login_ok:

        scene bg tela_computador with fade

        centered "Login realizado com sucesso."

        pause 1

        jump fase3_email

    scene black with fade

    centered "Conta bloqueada temporariamente."

    pause 2

    jump chapter_menu

############################################################
##
## LOGIN SKYMAIL
##
############################################################

default senha_login = ""
default login_falhou = False
default tentativas_login = 3
default login_ok = False

screen login_skyemail():

    modal True
    zorder 100

    use skymail_window("SkyMail - Login"):

        vbox:

            xfill True
            spacing 18

            ##################################################
            ## Logo
            ##################################################

            hbox:

                spacing 15
                xalign 0.5

                add Transform(
                    "images/icons/email.png",
                    size=(52,52)
                )

                text "SkyMail" style "sky_title"

            text "Entre com sua conta para acessar sua caixa de entrada." style "sky_text" xalign 0.5

            null height 15

            ##################################################
            ## Email
            ##################################################

            text "E-mail" style "sky_label"

            frame:

                background "#F5F5F5"

                xfill True

                padding (12,10)

                text "esmeralda@skyemail.com" style "sky_text"

            ##################################################
            ## Senha
            ##################################################

            text "Senha" style "sky_label"

            frame:

                background "#F5F5F5"

                xfill True

                padding (12,8)

                input:

                    value VariableInputValue("senha_login")

                    length 32

                    mask "*"

                    color "#000000"

                    size 24

                    xfill True

            ##################################################
            ## Mensagem de erro
            ##################################################

            if login_falhou:

                frame:

                    background "#FDECEC"

                    xfill True

                    padding (12,12)

                    text "Senha incorreta. Tente novamente." style "sky_error"

            ##################################################
            ## Tentativas
            ##################################################

            text "Tentativas restantes: [tentativas_login]" style "sky_label"

            ##################################################
            ## Botão
            ##################################################

            textbutton "Entrar":

                style "sky_button"

                text_style "sky_button_text"

                xalign 0.5

                action Return("login")
