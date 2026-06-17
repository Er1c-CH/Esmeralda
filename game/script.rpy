default fase1_liberada = False
default fase2_liberada = False
default fase3_liberada = False

label start:

    jump chapter_menu

label chapter_menu:

    call screen chapter_select
    return