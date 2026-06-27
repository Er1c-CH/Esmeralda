label tutorial:

    # ==================================================
    # CENA 1 - O DESPERTAR
    # ==================================================

    scene bg quarto

    show esmeralda feliz at centro

    e "Mais um dia começando..."

    e "Hoje vai ser diferente. O professor comentou que teremos uma avaliação prática sobre segurança digital."

    e "Uma prova... mas não no papel. Na internet."

    e "Melhor eu me preparar."

    e "Uso meu celular, computador e redes sociais todos os dias..."

    e "Mas será que eu realmente sei me proteger na internet?"

    hide esmeralda feliz

    scene bg frente_casa

    "Esmeralda termina de se preparar e sai de casa."

    # ==================================================
    # CENA 2 - CHEGADA À ESCOLA
    # ==================================================

    scene bg patio_escola

    show npc1 at esquerda
    show npc2 at direita
    show esmeralda feliz at centro

    a1 "Bom dia, Esmeralda!"

    e "Bom dia! Prova hoje, né?"

    a2 "Sim... disseram que vai ser uma prova diferente. Mais prática."

    a1 "Sobre internet, senhas e essas coisas."

    e "Então não é só teoria..."

    a2 "Parece que vamos ser testados de verdade."

    "O sinal toca."

    a1 "Vamos logo, antes que o professor comece."

    hide npc1
    hide npc2
    hide esmeralda feliz

    # ==================================================
    # CENA 3 - A AVALIAÇÃO DO PROFESSOR
    # ==================================================

    scene bg sala_aula

    show professor feliz at esquerda
    show esmeralda feliz at direita

    p "Bom dia, turma!"

    "Turma" "Bom dia!"

    p "Hoje não teremos uma aula comum."

    p "Vocês serão avaliados em uma prova prática de segurança digital."

    p "Essa prova será dividida em três desafios."

    p "E cada um deles simula situações reais da internet."

    # --------------------------
    # DESAFIO 1 - SENHAS
    # --------------------------

    p "Desafio 1: Senhas seguras."

    p "Vocês deverão criar uma senha forte para uma conta fictícia chamada SkyMail."

    p "Senhas fracas são facilmente descobertas e colocam seus dados em risco."

    p "Uma senha segura deve conter letras maiúsculas, minúsculas, números e símbolos."

    show esmeralda triste at direita

    e "Então minha senha vai ser testada..."

    hide esmeralda triste
    show esmeralda feliz at direita

    # --------------------------
    # DESAFIO 2 - ENGENHARIA SOCIAL
    # --------------------------

    p "Desafio 2: Engenharia social."

    a1 "Isso é o quê mesmo?"

    p "É quando alguém tenta enganar você para obter informações confidenciais."

    p "Não é um ataque direto ao sistema, mas à confiança da pessoa."

    p "Durante a prova, vocês vão encontrar pessoas tentando obter dados de vocês."

    p "Nem todo risco vem de computadores — alguns vêm de conversas."

    e "Então preciso desconfiar até de quem parece confiável..."

    # --------------------------
    # DESAFIO 3 - PHISHING
    # --------------------------

    p "Desafio 3: Phishing."

    a2 "Já ouvi falar disso..."

    p "Phishing são mensagens falsas que imitam empresas, bancos ou serviços reais."

    p "O objetivo é enganar vocês para clicar em links ou fornecer dados."

    p "Vocês deverão analisar e-mails e identificar sinais de fraude."

    p "Nem tudo o que parece oficial realmente é."

    p "A atenção aos detalhes será essencial."

    show esmeralda triste at direita

    e "Isso parece o mais difícil de todos..."

    # --------------------------
    # FIM DA AVALIAÇÃO
    # --------------------------

    show professor feliz at esquerda

    "O sinal toca."

    p "A prova começa agora."

    p "Lembrem-se: vocês serão avaliados pela capacidade de identificar riscos digitais."

    p "Boa sorte."

    "Turma" "Obrigado, professor!"

    hide professor feliz
    hide esmeralda triste

    # ==================================================
    # CENA 4 - PREPARAÇÃO FINAL
    # ==================================================

    scene bg sala_casa

    show esmeralda feliz at centro

    e "Então é isso... uma prova de verdade."

    e "Não é só sobre decorar, mas sobre entender o que é seguro ou não."

    e "Senhas, pessoas, mensagens..."

    e "Tudo pode ser uma armadilha se eu não prestar atenção."

    "Ela liga o computador."

    e "Hora de começar a avaliação."

    hide esmeralda feliz

    scene black with fade

    centered "AVALIAÇÃO INICIADA"

    pause 2.0

    centered "DESAFIO 1 - SENHAS SEGURAS"

    pause 2.0

    $ fase1_liberada = True

    jump chapter_menu