default senha_login = ""
default tentativas_login = 3
default login_falhou = False
default login_ok = False

init python:

    def verificar_login(senha_digitada, senha_correta):
        return senha_digitada == senha_correta

label fase3_login:

    $ senha_login = ""
    $ login_falhou = False
    $ login_ok = False

    while tentativas_login > 0 and not login_ok:

        call screen login_skyemail

        if _return == "login":

            if senha_login.strip() == senha_cadastrada.strip():

                $ login_ok = True

            else:

                $ tentativas_login -= 1
                $ login_falhou = True
                $ senha_login = ""

    if not login_ok:

        $ tentativas_login = 3

        scene black

        centered "ACESSO BLOQUEADO"

        return

    jump fase3_email