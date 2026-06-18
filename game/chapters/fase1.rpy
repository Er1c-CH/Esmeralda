label fase1:

    scene bg quarto

    show esmeralda feliz at centro

    e "A aula de hoje foi interessante."

    e "Nunca tinha parado para pensar em como uma senha ruim pode colocar minhas informações em risco."

    e "Vou criar uma conta no SkyMail para praticar."

    hide esmeralda feliz

    "SkyMail - Criar Conta"

    $ senha_digitada = ""
    $ senha_concluida = False

    $ resultado = renpy.call_screen("senha_minigame")

    if resultado:

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

        jump chapter_menu