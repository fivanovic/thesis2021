import socket
import time

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnected"
ip = "192.168.1.233"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,8080))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

#send("Hello!")
#send("Hello world!")
while True:
    resp = (client.recv(2048).decode(FORMAT))
    print(resp)

    if resp == "1":
        send("50")
        resp = 0
    #if PING == 1:
        #print("Starting count...")
        #PING = 0
    time.sleep(0.001)
