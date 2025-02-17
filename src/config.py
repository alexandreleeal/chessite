# Número de WhatsApp no formato internacional (exemplo: +55 para Brasil)
whatsapp_number = "+5511945717027"  # Substitua pelo número correto
# Mensagem pré-definida
message = "Olá, gostaria de agendar uma aula de xadrez com algum professor da academia."
# Criando o link do WhatsApp
whatsapp_link = f"https://wa.me/{whatsapp_number}?text={message.replace(' ', '%20')}"

page_title = "Academia de Xadrez"

page_icon = "../images/Chess_king.png"