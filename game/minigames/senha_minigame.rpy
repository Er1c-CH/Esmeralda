
init python:

    import re

    def analisar_senha(senha):

        criterios = {
            "tamanho": len(senha) >= 8,
            "minuscula": bool(re.search(r"[a-z]", senha)),
            "maiuscula": bool(re.search(r"[A-Z]", senha)),
            "numero": bool(re.search(r"[0-9]", senha)),
            "especial": bool(re.search(r"[^A-Za-z0-9]", senha))
        }

        pontos = sum(criterios.values())

        if pontos <= 2:
            nivel = "Fraca"
        elif pontos <= 4:
            nivel = "Média"
        else:
            nivel = "Forte"

        return criterios, pontos, nivel