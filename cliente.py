from threading import Thread
import websocket

def on_message(ws, message):
    print(message)

ws = websocket.WebSocketApp("ws://localhost:8000/", on_message=on_message)

paralelo = Thread(target=ws.run_forever)
paralelo.start()

while 1:
    a = input()
    ws.send(a)
