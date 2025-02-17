import streamlit as st
#import qrcode
from io import BytesIO
#from pixqrcodegen import Payload

# Adicionando um favicon (ícone do navegador) com Streamlit
st.set_page_config(
    page_title="Academia de Xadrez",
    page_icon="🦄",
    #page_icon="../images/Chess_king.png"
    )

def home():
    st.title("Academia de Xadrez")
    st.write("Academia de Xadrez é um centro de estudos dedicado a jogadores iniciantes que desejam evoluir para níveis intermediários e avançados. Com uma metodologia estruturada, oferecemos aulas teóricas e práticas, abordando desde os fundamentos do jogo até estratégias avançadas, táticas e preparação para torneios. Nosso objetivo é desenvolver o pensamento crítico, a capacidade de cálculo e a visão estratégica dos alunos, proporcionando uma base sólida para que possam competir em alto nível. Seja você um entusiasta ou alguém que busca se tornar um mestre, a Academia de Xadrez é o lugar ideal para aprimorar suas habilidades e alcançar novos patamares no jogo. ♟️🔥")
    st.image("https://raw.githubusercontent.com/alexandreleeal/chessite/refs/heads/main/images/logo2.webp")
    st.write("""Domine o Jogo e Eleve Seu Nível no Xadrez! ♟️🔥

Seja você um iniciante ou alguém buscando aprimorar suas habilidades, a Academia de Xadrez é o lugar ideal para evoluir no jogo. Aqui, você aprenderá desde os fundamentos até estratégias avançadas, desenvolvendo sua visão tática, raciocínio lógico e capacidade de tomada de decisões. Aprimore seu jogo com ensinamentos exclusivos e junte-se a uma comunidade apaixonada por xadrez!

🔽 No próximo parágrafo, descubra como podemos transformar sua jornada no xadrez! 🚀

Acelere sua evolução no xadrez com um treinamento personalizado! Agora você pode ter aulas individuais com professores especializados, que irão focar no seu estilo de jogo e ajudar você a superar desafios específicos. Seja para dominar aberturas, melhorar sua visão tática ou se preparar para torneios, nossas aulas são feitas sob medida para você!
""")
    st.markdown("#### **Clique em [Professores] e solicite sua aula particular agora mesmo!** 🚀")

def aulas():
    st.title("Aulas de Xadrez da Academia")
    st.write("Aqui você encontra as aulas disponíveis da Academ-ia de Xadrez")
    st.markdown("""
            ##### 1. [Aprenda a jogar xadrez do zero](#aprenda-a-jogar-xadrez-do-zero)
            ##### 2. [Xeque-mate com os dois cavalos](#xeque-mate-com-os-dois-cavalos)
            ##### 3. [Rei afogado](#rei-afogado)
            ##### 4. [Oposição e final de rei e peão](#oposiçao-e-final-de-rei-e-peao)
            ##### 5. [Regra do quadrado](#regra-do-quadrado)
            ##### 6. [Dicas de como analisar o lance](#dicas-de-como-analisar-o-lance)
            """)
    
    
    st.markdown("#### Aprenda a jogar xadrez do zero")
    st.video("https://www.youtube.com/watch?v=mbnMeq0CeAQ")
    st.markdown("#### Xeque-mate com os dois cavalos?")
    st.video("https://www.youtube.com/watch?v=ojjNhJg7aGo")
    st.markdown("#### Rei afogado")
    st.video("https://www.youtube.com/watch?v=LpTPDERcHaw")
    st.markdown("#### Oposição e final de rei e peão")
    st.video("https://www.youtube.com/watch?v=W97vOpSkMS4")
    st.markdown("#### Regra do quadrado")
    st.video("https://www.youtube.com/watch?v=ZCO9oDqS5EU")
    st.markdown("#### Dicas de como analisar o lance")
    st.video("https://www.youtube.com/watch?v=KYi1Ni3ZXZI")
    
def dados():
    st.title("Dados")
    st.write("Aqui você encontra os dados disponíveis.")

def professores():
    st.title("Professores")
    st.write("Aqui você pode conhecer os professores da Academia de Xadrez.")
    st.markdown("### Prof. Alexandre Garcia Leal")
    st.image("../images/professor_alexandre.png")
    st.markdown("""Canal no Youtube: [Link](https://www.youtube.com/@agleal1)  
                Contato: [Link](https://www.instagram.com/alexandre_leal_2022/)  
                Aula particular online personalizada para o aluno levando em conta seu conhecimento sobre xadrez.""")
    
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




# def gerar_pix_qrcode(descricao=" "):
#     try:
#         nome_sobrenome="Alexandre Leal"
#         chave_pix = "485.216.978-05"
#         valor = "1.00"
#         cidade = "Sao Paulo"
#         payloadFormat = "000201"
#         merchantAccount = "26"
#         merchantCategCode = "520400"
#         transactionCurrency = "5303986"
#         transactionAmount = "54"
#         countryCode = "5802BR"
#         merchantName = "59"
#         merchantCity = "60"
#         addDataField = "62"
#         crc16 = "6304"
#         nome_tam = len(nome_sobrenome)
#         payload = Payload(nome_sobrenome, chave_pix, valor, cidade, descricao)
#         pix_code = payload.gerarPayload()
#         qr = qrcode.make(pix_code)
#         buffer = BytesIO()
#         qr.save(buffer, format="PNG")
#         return buffer.getvalue()
#     except Exception as e:
#         st.error(f"Erro ao gerar QR Code Pix: {str(e)}")
#         return None

# def comprar():
#     st.title("Pagamento via Pix")
#     st.write("O pagamento tem um valor fixo de R$1,00.")
#     # Entrada de dados
#     descricao = st.text_input("Descrição do pagamento", placeholder="Ex: Treinamento de Xadrez")
#     valor =1
#     # Botão para gerar QR Code
#     if st.button("Gerar QR Code Pix"):
#         if valor > 0:
#             qr_image = gerar_pix_qrcode(descricao)
#             if qr_image:
#                 st.image(qr_image, caption="Escaneie para pagar", use_column_width=False)
#         else:
#             st.warning("Por favor, insira um valor maior que zero.")
