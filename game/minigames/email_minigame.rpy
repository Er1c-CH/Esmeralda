label email1:

    scene bg quarto

    show esmeralda triste at centro

    e "Banco Central?"

    menu:

        "Clicar no link e seguir instruções":
            $ phishing_score += 1
            e "Isso parece sério... vou seguir o link."
            "O link era falso e capturava seus dados."

        "Analisar o remetente antes de clicar":
            e "Isso é suspeito."
            "Boa escolha. Era phishing."

    $ emails_analisados += 1

    jump inbox_phishing

label email2:

    scene bg quarto

    show esmeralda feliz at centro

    e "Um e-mail da escola..."

    menu:

        "Abrir o link normalmente":
            e "Parece seguro."
            "Email legítimo."

        "Desconfiar e ignorar":
            e "Talvez seja melhor checar depois."
            "Você foi cautelosa demais."

    $ emails_analisados += 1

    jump inbox_phishing

label email3:

    scene bg quarto

    show esmeralda feliz at centro

    e "Suporte SkyEmail..."

    menu:

        "Enviar dados de verificação":
            $ phishing_score += 1
            e "Vou enviar minhas informações."
            "Golpe de roubo de conta."

        "Ignorar e verificar manualmente":
            e "Melhor acessar pelo site oficial."
            "Boa prática."

    $ emails_analisados += 1

    jump inbox_phishing

label fase3_resultado:

    scene black with fade

    if phishing_score == 0:

        centered "EXCELENTE DETETIVE DIGITAL"
        centered "Você identificou todas as ameaças corretamente."

    elif phishing_score == 1:

        centered "BOM TRABALHO"
        centered "Você cometeu um pequeno erro."

    elif phishing_score == 2:

        centered "ATENÇÃO"
        centered "Você caiu em algumas armadilhas."

    else:

        centered "VULNERÁVEL"
        centered "Seus dados foram comprometidos."

    pause 2.0

    centered "JOGO CONCLUÍDO"

    return

screen email_inbox():

    modal True

    frame:

        xalign 0.5
        yalign 0.5
        padding (30, 20)

        has vbox
        spacing 15

        text "SkyEmail - Caixa de Entrada" size 32

        text "E-mails analisados: [emails_analisados]/3"

        textbutton "📧 Banco Central - Conta bloqueada":
            action Jump("email1")

        textbutton "📧 Escola - Atualização de notas":
            action Jump("email2")

        textbutton "📧 Suporte SkyEmail - Verificação de conta":
            action Jump("email3")

        if emails_analisados >= 3:

            textbutton "Finalizar análise":
                action Return()