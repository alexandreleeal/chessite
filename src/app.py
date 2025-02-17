import streamlit as st
from io import BytesIO
from config import *

# Adicionando um favicon (ícone do navegador) com Streamlit
st.set_page_config(
    page_title=page_title,
    page_icon=page_icon
    )

def home():
    st.title("Academia de Xadrez")
    st.write("Academia de Xadrez é um centro de estudos dedicado a jogadores iniciantes que desejam evoluir para níveis intermediários e avançados. Com uma metodologia estruturada, oferecemos aulas teóricas e práticas, abordando desde os fundamentos do jogo até estratégias avançadas, táticas e preparação para torneios. Nosso objetivo é desenvolver o pensamento crítico, a capacidade de cálculo e a visão estratégica dos alunos, proporcionando uma base sólida para que possam competir em alto nível. Seja você um entusiasta ou alguém que busca se tornar um mestre, a Academia de Xadrez é o lugar ideal para aprimorar suas habilidades e alcançar novos patamares no jogo.")
    st.markdown("#### Domine o Jogo e Eleve Seu Nível no Xadrez! ♟️🔥")
    st.video("https://www.youtube.com/watch?v=19RoPcxs9bw")
    st.write("""
Seja você um iniciante ou alguém buscando aprimorar suas habilidades, a Academia de Xadrez é o lugar ideal para evoluir no jogo. Aqui, você aprenderá desde os fundamentos até estratégias avançadas, desenvolvendo sua visão tática, raciocínio lógico e capacidade de tomada de decisões. Aprimore seu jogo com ensinamentos exclusivos e junte-se a uma comunidade apaixonada por xadrez!

Acelere sua evolução no xadrez com um treinamento personalizado! Agora você pode ter aulas individuais com professores especializados, que irão focar no seu estilo de jogo e ajudar você a superar desafios específicos. Seja para dominar aberturas, melhorar sua visão tática ou se preparar para torneios, nossas aulas são feitas sob medida para você!
""")
    st.markdown("#### **Clique no botão abaixo e solicite sua aula particular!** 🚀")
    # Botão para abrir o WhatsApp
    if st.button("📲 **Solicite sua aula agora mesmo!**"):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={whatsapp_link}">', unsafe_allow_html=True)

def aulas():
    st.title("Aulas da Academia de Xadrez")
    st.write("""Bem-vindo à Academia de Xadrez! Aqui você encontra aulas didáticas e acessíveis para aprimorar suas habilidades no jogo, desde conceitos básicos até técnicas avançadas. Nossos conteúdos são elaborados para ajudar jogadores de todos os níveis a entenderem melhor as estratégias do xadrez, tornando cada partida mais envolvente e competitiva. Com vídeos explicativos e exemplos práticos, você poderá aprender e aperfeiçoar suas jogadas com facilidade.

Nesta seção, você encontrará lições essenciais para desenvolver seu raciocínio estratégico e dominar os princípios fundamentais do jogo. Desde aprender as regras básicas até técnicas avançadas como xeque-mate com dois cavalos, oposição em finais e a regra do quadrado, cada aula foi pensada para maximizar seu aprendizado. Explore o conteúdo e eleve seu nível no xadrez com a Academia!""")
    st.markdown("""
            ### Aulas
            ##### 1. [Aprenda a jogar xadrez do zero](#aprenda-a-jogar-xadrez-do-zero)
            ##### 2. [Xeque-mate com os dois cavalos](#xeque-mate-com-os-dois-cavalos)
            ##### 3. [Rei afogado](#rei-afogado)
            ##### 4. [Oposição e final de rei e peão](#oposiçao-e-final-de-rei-e-peao)
            ##### 5. [Regra do quadrado](#regra-do-quadrado)
            ##### 6. [Dicas de como analisar o lance](#dicas-de-como-analisar-o-lance)
            ###
            """)
    
    
    st.markdown("#### Aprenda a jogar xadrez do zero")
    st.video("https://www.youtube.com/watch?v=mbnMeq0CeAQ")
    st.markdown("""O vídeo apresenta uma introdução ao xadrez, explicando as regras básicas do jogo, o tabuleiro e a movimentação das peças. O tabuleiro é composto por 64 casas alternadas entre brancas e pretas, e cada jogador começa com 16 peças: oito peões, duas torres, dois cavalos, dois bispos, uma dama e um rei. A movimentação das peças é explicada de forma clara, destacando o cavalo como a única peça que pode saltar sobre outras.

Além das regras, o vídeo aborda conceitos essenciais como o objetivo do jogo, que é dar xeque-mate no rei adversário, impedindo qualquer movimento seguro. São apresentados exemplos práticos de xeque e xeque-mate para ilustrar as situações mais comuns. Também se explica a importância do desenvolvimento das peças no início do jogo e como evitar erros frequentes de iniciantes.

Por fim, são discutidas algumas estratégias básicas para iniciantes, como o controle do centro do tabuleiro, a importância da segurança do rei e a troca de peças vantajosa. O vídeo reforça a necessidade de prática e estudo para o aprimoramento, recomendando que os jogadores analisem partidas famosas e treinem regularmente para evoluir.

###
""")

    st.markdown("#### Xeque-mate com os dois cavalos?")
    st.video("https://www.youtube.com/watch?v=ojjNhJg7aGo")
    st.markdown("""O vídeo analisa a possibilidade de dar xeque-mate apenas com dois cavalos e um rei contra um rei solitário. Diferente de outras combinações de peças, os dois cavalos não conseguem forçar um xeque-mate sozinhos, pois o rei adversário pode escapar continuamente. O Prof. Alexandre explica que, sem a cooperação de outro fator, o xeque-mate não pode ser forçado.

No entanto, existe uma exceção: se o oponente ainda tiver um peão em jogo, ele pode ser usado para restringir as casas disponíveis para o rei adversário. O vídeo demonstra como essa situação pode ocorrer e como aproveitar esse detalhe para criar um xeque-mate eficiente. São mostradas sequências práticas em que o mate pode ser conduzido com precisão.

Por fim, o vídeo destaca a importância de conhecer essa limitação e como ela influencia finais de partida. Em competições, é essencial saber quando um mate é possível e quando é melhor tentar outro plano. O estudo de finais como esse aprimora a compreensão da movimentação dos cavalos e a necessidade de coordenação entre as peças para alcançar a vitória.

###
""")
    
    st.markdown("#### Rei afogado")
    st.video("https://www.youtube.com/watch?v=LpTPDERcHaw")
    st.markdown("""O conceito de "rei afogado" é explicado como uma situação em que o jogador fica sem movimentos legais, mas sem estar em xeque, resultando em empate. O vídeo apresenta exemplos práticos desse cenário, destacando como isso pode ocorrer tanto de forma acidental quanto intencional, dependendo da estratégia do jogador.

São mostradas algumas posições comuns onde o afogamento acontece, especialmente em finais de partida, quando o jogador em desvantagem tenta escapar de uma derrota certa. Um exemplo clássico é quando o rei adversário está cercado por suas próprias peças e não pode se mover sem entrar em xeque. O vídeo também aborda como evitar cair nessa armadilha ao tentar finalizar um jogo ganho.

Por fim, o Prof. Alexandre enfatiza que entender o rei afogado é essencial para jogadores de todos os níveis. Para quem está em uma posição perdedora, forçar o afogamento pode ser uma maneira de salvar meio ponto no jogo. Já para quem está ganhando, é fundamental calcular corretamente os lances finais para evitar deixar o adversário sem movimentos legais e perder a vitória.

###
""")
    
    
    st.markdown("#### Oposição e final de rei e peão")
    st.video("https://www.youtube.com/watch?v=W97vOpSkMS4")
    st.markdown("""O vídeo ensina a importância da "oposição" nos finais de rei e peão, um conceito fundamental para garantir a vitória em finais simplificados. Oposição ocorre quando os reis estão frente a frente, e aquele que não tem a vez de jogar tem a vantagem. Esse conceito é crucial para controlar espaços no tabuleiro e impedir o avanço do rei adversário.

São demonstradas diversas situações onde a oposição faz a diferença entre ganhar ou empatar uma partida. Se o jogador souber utilizar corretamente esse princípio, poderá conduzir o próprio rei até uma posição ideal para promover um peão e vencer. O vídeo destaca a importância de entender a regra dos tempos e como manter a oposição ao longo dos lances.

No final, o Prof. Alexandre reforça que aprender sobre a oposição melhora a compreensão dos finais de jogo e a tomada de decisões estratégicas. Muitas partidas de torneios são decididas com poucos peões e reis no tabuleiro, tornando esse conhecimento essencial para jogadores competitivos. O estudo de finais ajuda a antecipar jogadas e tomar as melhores decisões quando o tempo está curto.

###
""")
    
    st.markdown("#### Regra do quadrado")
    st.video("https://www.youtube.com/watch?v=ZCO9oDqS5EU")
    st.markdown("""O vídeo explica a "regra do quadrado", um conceito simples que ajuda a determinar se um rei pode capturar um peão antes que ele promova a dama. Essa regra consiste em imaginar um quadrado traçado a partir da posição do peão até a última casa do tabuleiro, formando uma área de casas possíveis para o rei se deslocar.

São apresentados exemplos práticos para entender como essa regra funciona. Se o rei estiver dentro do quadrado, ele pode alcançar o peão e impedir a promoção. Se estiver fora, não conseguirá alcançar a tempo. O vídeo destaca a importância de aplicar essa técnica rapidamente durante uma partida, sem precisar calcular vários lances.

No final, o Prof. Alexandre enfatiza que dominar a regra do quadrado ajuda a tomar decisões rápidas em finais de jogo. Esse conceito permite avaliar rapidamente se vale a pena avançar um peão ou se é necessário proteger a posição do rei. Conhecer essa técnica melhora o jogo de finais e aumenta as chances de vitória em partidas equilibradas.

###
""")
    
    st.markdown("#### Dicas de como analisar o lance")
    st.video("https://www.youtube.com/watch?v=KYi1Ni3ZXZI")
    st.markdown("""O vídeo apresenta estratégias para analisar um lance antes de jogá-lo, ajudando a evitar erros comuns e aprimorar a tomada de decisões. O primeiro passo é verificar todas as ameaças do adversário, como peças desprotegidas, possíveis táticas e ataques iminentes. A análise cuidadosa evita jogadas impulsivas que podem resultar em perdas desnecessárias.

Outro ponto fundamental é considerar as respostas do oponente antes de executar um lance. O vídeo explica como visualizar a posição futura do tabuleiro e calcular variantes. Jogadores iniciantes costumam focar apenas no próprio ataque, sem avaliar os riscos. O Prof. Alexandre destaca a importância da paciência e da observação para melhorar a qualidade das jogadas.

Por fim, são mencionadas técnicas como a "checagem tripla", em que o jogador revisa sua jogada pelo menos três vezes antes de movê-la. Também são sugeridos exercícios para treinar a análise, como resolver posições táticas e revisar partidas jogadas. Com a prática constante, o jogador desenvolve uma visão estratégica mais refinada e toma decisões mais seguras.

###
""")
    
def dados():
    st.title("Dados")
    st.write("Aqui você encontra os dados disponíveis.")

def professores():
    st.title("Professores")
    st.write("Aqui você pode conhecer os professores da Academia de Xadrez.")
    st.markdown("### Prof. Alexandre Garcia Leal")
    st.image("https://yt3.googleusercontent.com/wCBFLwj_6qLRf4DhqZXGNB-uq3MhJokHp_yIq34Jsj_qlDAUC52Sa59pXkC1QN0D1zC2WA9h=w2560-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj")
    st.markdown("""Canal no Youtube: [Link](https://www.youtube.com/@agleal1)  
                Contato: [Link](https://www.instagram.com/alexandre_leal_2022/)  
                Aula particular online personalizada para o aluno levando em conta seu conhecimento sobre xadrez.""")
    # Botão para abrir o WhatsApp
    if st.button("📲 **Solicite sua aula agora mesmo!**"):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={whatsapp_link}">', unsafe_allow_html=True)
    
def puzzles():
    st.title("Quebra-cabeças")
    st.markdown("""
            ##### 1. [♟️ Aberturas](https://lichess.org/pt/training/opening)
            ##### 2. [🏁 Finais](https://lichess.org/pt/training/endgame)
            ##### 3. [♝ Finais de bispo](https://lichess.org/pt/training/bishopEndgame)
            ##### 4. [♞ Finais de cavalo](https://lichess.org/pt/training/knightEndgame)
            ##### 5. [♙ Finais de peao](https://lichess.org/pt/training/pawnEndgame)
            ##### 6. [♜ Finais de torres](https://lichess.org/pt/training/rookEndgame)
            ##### 7. [♛ Finais de dama](https://lichess.org/pt/training/queenEndgame)
            ##### 8. [♛♜ Finais de dama e torre](https://lichess.org/pt/training/queenRookEndgame)
            ##### 9. [⚔️ Meio-jogo](https://lichess.org/pt/training/middlegame)
            """)

# Dicionário de páginas
pages = {
    "Home": home,
    "Aulas": aulas,
    "Professores": professores,
    "Quebra-cabeças": puzzles,
    #"Comprar":comprar,
}

# Criando a barra lateral para navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio("Escolha uma página:", list(pages.keys()))

# Executando a página selecionada
pages[page]()