label fase2:

    $ vulnerabilidade = 0

    scene bg patio_escola

    show esmeralda feliz at esquerda
    show npc1 at direita

    a1 "Oi, Esmeralda!"

    e "Oi!"

    a1 "Estou criando uma conta nova."

    a1 "Qual era mesmo o nome do seu primeiro animal de estimação?"

    a1 "Preciso de ideias para responder minha pergunta secreta."

    menu:

        "Responder a pergunta":
            $ vulnerabilidade += 1

            e "Meu primeiro animal se chamava Pipoca."

            a1 "Interessante..."

            "Você compartilhou uma informação pessoal que poderia ser usada para recuperar contas."

        "Recusar responder":

            e "Prefiro não compartilhar esse tipo de informação."

            a1 "Tudo bem."

            "Boa escolha."
    
    scene bg patio_escola

    show npc2 at direita
    show esmeralda feliz at esquerda

    a2 "Esmeralda, preciso da sua ajuda."

    a2 "Recebi um código por mensagem."

    a2 "Pode me dizer qual foi o código que chegou para você?"

    a2 "Acho que usei seu número sem querer."

    menu:

        "Informar o código":
            $ vulnerabilidade += 1

            e "Tudo bem."

            "Códigos de verificação nunca devem ser compartilhados."

        "Recusar":

            e "Não posso compartilhar códigos de autenticação."

            a2 "Entendi."

            "Boa decisão."
    
    scene bg sala_aula

    show professor feliz at direita
    show esmeralda feliz at esquerda

    p "Bom trabalho hoje, turma."

    p "Antes de terminar, preciso confirmar sua matrícula."

    p "Você pode me informar seu número de matrícula?"

    menu:

        "Informar matrícula":

            e "Claro."

            p "Perfeito."

            "O professor é uma fonte legítima nesta situação."

        "Recusar":

            e "Prefiro não informar."

            p "Tudo bem, mas essa era uma solicitação oficial da escola."

            "Nem toda solicitação é uma tentativa de golpe."

    hide professor feliz
    hide esmeralda feliz

    scene bg sala_casa

    show esmeralda feliz at centro

    e "Hoje percebi que nem sempre é fácil saber em quem confiar."

    e "Algumas pessoas podem tentar conseguir informações importantes de forma sutil."

    e "Preciso analisar cada situação com atenção."

    hide esmeralda feliz

    scene black with fade

    if vulnerabilidade == 0:

        centered "RESULTADO: EXCELENTE"

        centered "Você identificou corretamente todas as tentativas de engenharia social."

    elif vulnerabilidade == 1:

        centered "RESULTADO: BOM"

        centered "Você cometeu apenas um pequeno erro."

    elif vulnerabilidade == 2:

        centered "RESULTADO: ATENÇÃO"

        centered "Algumas informações foram compartilhadas sem necessidade."

    else:

        centered "RESULTADO: VULNERÁVEL"

        centered "Golpistas poderiam explorar as informações fornecidas."
    
    pause 2.0

    centered "FASE 2 CONCLUÍDA"

    pause 2.0

    centered "Próxima Etapa"

    pause 1.0

    centered "ANÁLISE DE PHISHING"

    pause 2.0

    $ fase3_liberada = True

    jump chapter_menu