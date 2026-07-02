# ==================================================
# PERSONAGENS
# ==================================================

define e = Character("Esmeralda", color="#66CC66")
define p = Character("Prof. Gustavo", color="#4A90E2")
define a1 = Character("Gabriel", color="#FFB347")
define a2 = Character("Júlia", color="#FF69B4")

define narrador = Character(None)


# ==================================================
# ESPERMALDA
# ==================================================

image esmeralda feliz = Transform(
    "images/protagonista feliz.png",
    zoom=0.35
)

image esmeralda triste = Transform(
    "images/protagonista triste.png",
    zoom=0.35
)

image esmeralda raiva = Transform(
    "images/protagonista raiva.png",
    zoom=0.35
)


# ==================================================
# PROFESSOR
# ==================================================

image professor feliz = Transform(
    "images/professor feliz.png",
    zoom=0.45
)

image professor triste = Transform(
    "images/professor triste.png",
    zoom=0.45
)

image professor raiva = Transform(
    "images/professor raiva.png",
    zoom=0.45
)


# ==================================================
# NPCs
# ==================================================

image npc1 = Transform(
    "images/npc 2.png",
    zoom=0.35
)

image npc2 = Transform(
    "images/npc 1.png",
    zoom=0.35
)