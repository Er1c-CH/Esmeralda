label tutorial:

    # ==================================================
    # CENA 1 - O DESPERTAR
    # ==================================================

    scene bg quarto

    show esmeralda feliz at centro

    e "Mais um dia começando..."

    e "Hoje parece que vai ser diferente. O professor comentou que teríamos uma aula especial sobre segurança digital."

    e "Melhor eu me arrumar logo para não perder o ônibus."

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

    e "Bom dia! Sobre o que vocês estavam falando?"

    a2 "Você viu a mensagem que circulou no grupo da turma ontem?"

    a1 "Pois é. Tinha um link prometendo ingressos grátis para um show."

    e "E alguém clicou?"

    a1 "Algumas pessoas sim. Depois descobriram que era falso."

    a2 "Hoje em dia é difícil saber o que é confiável na internet."

    e "Ainda bem que a aula de hoje vai falar justamente sobre isso."

    "O sinal toca."

    a1 "Vamos para a sala!"

    a2 "Antes que o professor reclame do atraso."

    hide npc1
    hide npc2
    hide esmeralda feliz

    # ==================================================
    # CENA 3 - A AULA
    # ==================================================

    scene bg sala_aula

    show professor feliz at esquerda
    show esmeralda feliz at direita

    p "Bom dia, turma!"

    "Turma" "Bom dia!"

    p "Hoje vamos aprender algo muito importante: como proteger nossos dados e nossa identidade digital."

    p "Todos vocês usam celulares, redes sociais, aplicativos e e-mails diariamente."

    p "Mas será que sabem reconhecer os riscos que existem na internet?"

    "Os alunos ficam atentos."

    # --------------------------
    # DESAFIO 1
    # --------------------------

    p "Nosso primeiro desafio será sobre senhas."

    p "Muitas pessoas ainda utilizam senhas simples como datas de aniversário, nomes de familiares ou sequências numéricas."

    p "Essas senhas podem ser descobertas facilmente."

    p "Vocês precisarão aprender a criar senhas fortes utilizando letras maiúsculas, minúsculas, números e símbolos."

    p "Quanto mais difícil for adivinhar a senha, maior será a proteção das suas contas."

    show esmeralda triste at direita

    e "Acho que vou precisar revisar algumas das minhas senhas..."

    # --------------------------
    # DESAFIO 2
    # --------------------------

    show esmeralda feliz at direita

    p "O segundo desafio será sobre engenharia social."

    a1 "O que é isso, professor?"

    p "É quando alguém tenta manipular você para obter informações pessoais."

    p "Nem todo ataque acontece através de computadores."

    p "Muitas vezes o golpista tenta ganhar sua confiança primeiro."

    p "Vocês precisarão observar comportamentos, analisar situações e decidir em quem confiar."

    p "Uma decisão errada pode expor informações importantes."

    e "Então nem todo perigo vem de programas maliciosos..."

    # --------------------------
    # DESAFIO 3
    # --------------------------

    p "O terceiro desafio será sobre phishing."

    a2 "Já ouvi esse nome antes."

    p "Phishing é uma tentativa de enganar usuários através de mensagens falsas."

    p "Essas mensagens geralmente imitam bancos, lojas, empresas ou serviços conhecidos."

    p "Vocês precisarão analisar e-mails, links e mensagens para identificar possíveis fraudes."

    p "Nem tudo o que parece verdadeiro realmente é."

    p "Antes de clicar em qualquer link, é importante observar os detalhes."

    show esmeralda triste at direita

    e "Parece mais complicado do que eu imaginava."

    # --------------------------
    # FIM DA AULA
    # --------------------------

    show professor feliz at esquerda

    "O sinal toca anunciando o fim da aula."

    p "Por hoje é só."

    p "Nas próximas atividades vocês colocarão esse conhecimento em prática."

    p "Lembrem-se: proteger seus dados é proteger vocês mesmos."

    "Turma" "Até logo, professor!"

    hide professor feliz
    hide esmeralda triste

    # ==================================================
    # CENA 4 - VOLTA PARA CASA
    # ==================================================

    scene bg sala_casa

    show esmeralda feliz at centro

    "Esmeralda chega em casa e coloca sua mochila sobre a mesa."

    e "Aprendi bastante coisa hoje."

    e "Nunca tinha parado para pensar que uma senha fraca poderia causar tantos problemas."

    e "Também preciso prestar mais atenção nas pessoas e nas mensagens que recebo."

    e "A internet pode ser muito útil, mas também exige cuidado."

    "Ela liga o computador."

    e "Hora de colocar esse conhecimento em prática."

    hide esmeralda feliz

    scene black with fade

    centered "TUTORIAL CONCLUÍDO"

    pause 2.0

    centered "Próxima Etapa"

    pause 1.5

    centered "FASE 1 - CONSTRUINDO SENHAS FORTES"

    pause 2.0

    $ fase1_liberada = True

    jump chapter_menu