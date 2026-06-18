default phishing_score = 0
default emails_analisados = 0

label fase3_phishing:

    $ phishing_score = 0
    $ emails_analisados = 0

    scene bg quarto

    show esmeralda feliz at centro

    e "Finalmente estou dentro da minha conta de e-mail..."

    e "Mas por que tem tantas mensagens urgentes?"

    e "Preciso ter cuidado... isso pode ser perigoso."

    hide esmeralda feliz

    jump inbox_phishing

label inbox_phishing:

    while emails_analisados < 3:

        call screen email_inbox

    jump fase3_resultado