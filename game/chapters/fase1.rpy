label fase1:

    scene bg quarto

    show esmeralda feliz at centro

    e "A aula de hoje foi interessante."

    e "Nunca tinha parado para pensar em como uma senha ruim pode colocar minhas informações em risco."

    e "Vou criar uma conta no SkyMail para praticar."

    hide esmeralda feliz

    scene bg tela_computador with fade

    $ senha_digitada = ""
    $ mostrar_dicas = False

    call screen skymail_cadastro

    scene bg quarto

    show esmeralda feliz at centro

    e "Consegui!"

    e "Uma senha forte ajuda a proteger minhas informações."

    e "Agora entendo melhor o que o professor explicou."

    hide esmeralda feliz

    scene black with fade

    centered "FASE 1 CONCLUÍDA"

    pause 2.0

    centered "Próxima Etapa"

    pause 1.0

    centered "ENGENHARIA SOCIAL"

    pause 2.0

    $ fase2_liberada = True
    $ senha_cadastrada = senha_digitada

    jump chapter_menu


screen skymail_cadastro():

    modal True

    $ criterios, pontos, nivel = analisar_senha(senha_digitada)

    frame:

        background "#FFFFFF"

        xalign 0.5
        yalign 0.4

        xsize 800
        ysize 620

        padding (0,0)

        has vbox

        ########################################
        ## Barra do navegador
        ########################################

        frame:

            background "#D9D9D9"

            xfill True
            ysize 38

            hbox:

                xfill True
                yalign 0.5
                spacing 10

                null width 15

                text "SkyMail - Criar Conta" color "#333333" size 22

                null width 12

                text "●" color "#ff5f57" size 18
                text "●" color "#ffbd2f" size 18
                text "●" color "#28c840" size 18



        ########################################
        ## Barra de endereço
        ########################################

        frame:

            background "#EFEFEF"

            xfill True
            ysize 45

            hbox:

                spacing 12

                null width 12

                text "←"

                text "→"

                text "⟳"

                frame:

                    background "#FFFFFF"

                    xfill True

                    padding (8,5)

                    text "https://www.skymail.com/cadastro" color "#666666"

        ########################################
        ## Conteúdo
        ########################################

        frame:

            background "#FFFFFF"

            xfill True
            yfill True

            padding (25,20)

            vbox:

                spacing 15

                ################################

                hbox:

                    spacing 10

                    add Transform(
                        "images/icons/email.png",
                        size=(40,40)
                    )

                    text "SkyMail" size 34 color "#222"

                ################################

                text "E-mail"

                frame:

                    background "#F5F5F5"

                    xfill True

                    padding (10,10)

                    text "esmeralda@skymail.com"

                ################################

                text "Senha"

                frame:

                    background "#F5F5F5"

                    xfill True

                    padding (10,10)

                    input:
                        value VariableInputValue("senha_digitada")
                        length 32
                        mask "*"

                ################################

                textbutton "Criar Conta":

                    xalign 0.5

                    action If(
                        pontos == 5,
                        Return(True),
                        SetVariable("mostrar_dicas", True)
                    )

                ################################

                if mostrar_dicas:

                    $ senha_fraca = True

                    null height 5

                    frame:

                        background "#ECECEC"

                        xfill True

                        padding (10, 10)

                        vbox:

                            spacing 12

                            text "⚠ Sua senha ainda não atende aos requisitos mínimos de segurança." color "#AA0000"

                            grid 2 3:

                                spacing 5

                                if criterios["tamanho"]:
                                    text "✓ 8 caracteres"
                                else:
                                    text "✗ 8 caracteres"

                                if criterios["numero"]:
                                    text "✓ Número"
                                else:
                                    text "✗ Número"

                                if criterios["maiuscula"]:
                                    text "✓ Letra maiúscula"
                                else:
                                    text "✗ Letra maiúscula"

                                if criterios["especial"]:
                                    text "✓ Caractere especial"
                                else:
                                    text "✗ Caractere especial"

                                if criterios["minuscula"]:
                                    text "✓ Letra minúscula"
                                else:
                                    text "✗ Letra minúscula"

                                null