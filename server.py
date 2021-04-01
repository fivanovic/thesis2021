import socket
import time
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnected"
ip = socket.gethostbyname(socket.gethostname())
#start server
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, 8080))

def handle_client(conn, addr):
    print(f"New Connection {addr} connected")
    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
        print(f"{addr} {msg}")


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections] {threading.activeCount() -1}")
print(f"SERVER: started on {ip}")
start()
