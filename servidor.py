from threading import Thread
from simple_websocket_server import WebSocketServer, WebSocket

usuarios = []

class Chat(WebSocket):
    def handle(self):
        mensagem = str(self.address[0]) + " diz: " + self.data
        global usuarios
        
        for usuario in usuarios:
            if usuario.address != self.address:
                usuario.send_message(mensagem)

        print(mensagem)

    def connected(self):
        mensagem = str(self.address[0]) + " entrou"
        global usuarios
        usuario = self        
        usuarios.append(usuario)

        for usuario in usuarios:
            if usuario.address != self.address:
                usuario.send_message(mensagem)

        print(mensagem)

    def handle_close(self):
        mensagem = str(self.address[0]) + " saiu"
        global usuarios
        for usuario in usuarios:
            if usuario.address == self.address:
                usuarios.remove(usuario)
            
            if usuario.address != self.address:
                usuario.send_message(mensagem)

        print(mensagem)

servidor = WebSocketServer("", 8000, Chat)

paralelo = Thread(target=servidor.serve_forever)
paralelo.start()

while 1:
    a = input()
    for usuario in usuarios:
        usuario.send_message("servidor diz: "+ a)