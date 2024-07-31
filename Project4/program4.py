# IMPORTANT!!! IMPORTANTE!!!
# Para funcionar corretamente utilize as bibliotecas flet
# to work correctly uses the flet library
# pip install flet


# Talkchat
# botao de iniciar chat / start button
# popup para entrar no chat/ popup to join on chat
# quando entrar no chat: (aparece para todo mundo)/ when joined on chat: (visible for everyone)
    # a mensagem que você entrou no chat/ the message that you joined on chat
    # o campo e o botão de enviar mensagem/ the field and button to send message
# a cada mensagem que você envia (aparece para todo mundo)/ for every message you send (visible for everyone)
    # Nome: Texto da Mensagem/ name: message text

import flet as ft

def main(pagina):
    texto = ft.Text("Talkchat")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome / type your name")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat / to add a message on chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
                                         size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})
        # limpar o campo de mensagem / clear the field of message
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        # adicionar o chat / to add the chat
        pagina.add(chat)
        # fechar o popup / close popup
        popup.open = False
        # remover o botao iniciar chat/ remove the button of start chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar o campo de mensagem do usuario / create the field user message
        # criar o botao de enviar mensagem do usuario/ create the button to send user message
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem vindo ao Talkchat / Welcome to Talkchat"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar/ join", on_click=entrar_popup)],
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat/ Start chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

# deploy
