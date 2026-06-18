screen login_skyemail():

    modal True
    zorder 100

    frame:

        xalign 0.5
        yalign 0.5
        padding (40, 30)

        has vbox
        spacing 15

        text "SkyEmail - Login" size 32

        text "E-mail: esmeralda@skyemail.com"

        if senha_login == "":
            text "Digite sua senha" color "#888888"

        input:
            value VariableInputValue("senha_login")
            length 32
            color "#000000"

        if login_falhou:
            text "Senha incorreta!" color "#ff4444"

        text "Tentativas restantes: [tentativas_login]"

        if tentativas_login > 0:

            textbutton "Entrar":
                action Return("login")

        else:

            text "Conta bloqueada temporariamente." color "#ff4444"