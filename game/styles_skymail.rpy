############################################################
##
## SkyMail UI
## Jornada Digital de Esmeralda
##
############################################################

##############################
## CORES
##############################

define SKY_BG = "#F4F6F9"

define SKY_WINDOW = "#FFFFFF"

define SKY_HEADER = "#E7EAF0"

define SKY_ADDRESS = "#F8F8F8"

define SKY_BORDER = "#CFCFCF"

define SKY_BUTTON = "#2D7FF9"

define SKY_BUTTON_HOVER = "#4D95FF"

define SKY_TEXT = "#222222"

define SKY_SUBTEXT = "#666666"

define SKY_SUCCESS = "#1E8E3E"

define SKY_ERROR = "#D93025"

define SKY_WARNING = "#F9AB00"

############################################################
## ESTILOS
############################################################

style sky_title:
    color SKY_TEXT
    size 25
    bold True

style sky_text:
    color SKY_TEXT
    size 17

style sky_label:
    color SKY_SUBTEXT
    size 13
    bold True

style sky_address:
    color "#555555"
    size 13

style sky_error:
    color SKY_ERROR
    size 15
    bold True

style sky_success:
    color SKY_SUCCESS
    size 15
    bold True

style sky_button_text:

    color "#FFFFFF"

    hover_color "#FFFFFF"

    bold True

    size 19

############################################################
## BOTÃO PADRÃO
############################################################

style sky_button is default:

    background Solid(SKY_BUTTON)

    hover_background Solid(SKY_BUTTON_HOVER)

    xpadding 22

    ypadding 12

############################################################
## TRANSFORMS
############################################################

transform skymail_shadow:

    alpha 0.15

transform skymail_window:

    xalign 0.5

    yalign 0.5

############################################################
## COMPONENTE
############################################################

screen skymail_window(title="SkyMail", largura=780, altura=590):

    modal True

    #########################################
    ## SOMBRA
    #########################################

    frame:

        background "#00000040"

        xpos 255
        ypos 60

        xsize largura + 10
        ysize altura + 10

    #########################################
    ## JANELA
    #########################################

    frame:

        background SKY_WINDOW

        xpos 250
        ypos 55

        xsize largura
        ysize altura

        padding (0,0)

        has vbox

        ####################################################
        ## BARRA DO NAVEGADOR
        ####################################################

        frame:

            background SKY_HEADER

            xfill True

            ysize 38

            hbox:

                spacing 10

                xalign 0.0

                yalign 0.5

                null width 10

                text "●" color "#ff5f57" size 18

                text "●" color "#febc2e" size 18

                text "●" color "#28c840" size 18

                null width 12

                text "[title]" style "sky_title"

        ####################################################
        ## BARRA DE ENDEREÇO
        ####################################################

        frame:

            background SKY_ADDRESS

            xfill True

            ysize 46

            hbox:

                spacing 14

                yalign 0.5

                null width 12

                text "←"

                text "→"

                text "⟳"

                frame:

                    background "#FFFFFF"

                    xfill True

                    yalign 0.5

                    padding (10,6)

                    text "https://www.skymail.com" style "sky_address"

        ####################################################
        ## CONTEÚDO
        ####################################################

        frame:

            background SKY_WINDOW

            xfill True

            yfill True

            padding (28,22)

            transclude