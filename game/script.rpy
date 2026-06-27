
label start:

    play music "music/ost1.ogg" fadein 2.0

    jump chapter_menu

label chapter_menu:

    call screen chapter_select

    return

screen chapter_select():

    tag menu

    add Solid("#fff3ff")

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 35
            xalign 0.5

            text "Selecione um Capítulo" size 48 xalign 0.5

            hbox:
                spacing 60
                xalign 0.5

                #################################
                # TUTORIAL
                #################################

                vbox:
                    spacing 10
                    xalign 0.5

                    imagebutton:
                        idle Transform("images/menu/tutorial_icone.png", size=(200,200))
                        hover Transform("images/menu/tutorial_icone.png", size=(200,200))
                        action Jump("tutorial")

                    text "Tutorial" xalign 0.5

                #################################
                # FASE 1
                #################################

                vbox:
                    spacing 10
                    xalign 0.5

                    fixed:
                        xsize 200
                        ysize 200

                        if fase1_liberada:

                            imagebutton:
                                idle Transform("images/menu/fase1_icone.png", size=(200,200))
                                hover Transform("images/menu/fase1_icone.png", size=(200,200))
                                action Jump("fase1")

                        else:

                            imagebutton:
                                idle Transform(
                                    "images/menu/fase1_icone.png",
                                    size=(200,200),
                                    alpha=0.45
                                )
                                hover Transform(
                                    "images/menu/fase1_icone.png",
                                    size=(200,200),
                                    alpha=0.45
                                )
                                action NullAction()

                            add Transform(
                                "images/menu/lock.png",
                                size=(64,64),
                                xpos=68,
                                ypos=68
                            )

                    text "Fase 1" xalign 0.5

                #################################
                # FASE 2
                #################################

                vbox:
                    spacing 10
                    xalign 0.5

                    fixed:
                        xsize 200
                        ysize 200

                        if fase2_liberada:

                            imagebutton:
                                idle Transform("images/menu/fase2_icone.png", size=(200,200))
                                hover Transform("images/menu/fase2_icone.png", size=(200,200))
                                action Jump("fase2")

                        else:

                            imagebutton:
                                idle Transform(
                                    "images/menu/fase2_icone.png",
                                    size=(200,200),
                                    alpha=0.45
                                )
                                hover Transform(
                                    "images/menu/fase2_icone.png",
                                    size=(200,200),
                                    alpha=0.45
                                )
                                action NullAction()

                            add Transform(
                                "images/menu/lock.png",
                                size=(64,64),
                                xpos=68,
                                ypos=68
                            )

                    text "Fase 2" xalign 0.5

                #################################
                # FASE 3
                #################################

                vbox:
                    spacing 10
                    xalign 0.5

                    fixed:
                        xsize 200
                        ysize 200

                        if fase3_liberada:

                            imagebutton:
                                idle Transform("images/menu/fase3_icone.png", size=(200,200))
                                hover Transform("images/menu/fase3_icone.png", size=(200,200))
                                action Jump("fase3")

                        else:

                            imagebutton:
                                idle Transform(
                                    "images/menu/fase3_icone.png",
                                    size=(200,200),
                                    alpha=0.45
                                )
                                hover Transform(
                                    "images/menu/fase3_icone.png",
                                    size=(200,200),
                                    alpha=0.45
                                )
                                action NullAction()

                            add Transform(
                                "images/menu/lock.png",
                                size=(64,64),
                                xpos=68,
                                ypos=68
                            )

                    text "Fase 3" xalign 0.5

            null height 15

            textbutton "Voltar":
                xalign 0.5
                action Return()