import socket
import time
import threading

HEADER = 64
global FLASH
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnected"
CHECKER = "PING"
ip = "192.168.1.233"
#start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, 8080))

def trigger():
    global FLASH
    FLASH = "1"
    time.sleep(1)
    FLASH = "0"
    time.sleep(1)

x = threading.Thread(target=trigger, args=())


def handle_client(conn, addr):
    print(f"New Connection {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                connected = False
            print(f"{addr} {msg}")

            if msg == CHECKER:
                conn.send(FLASH.encode(FORMAT))
        time.sleep(1)
        #conn.send("test".encode(FORMAT))


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections] {threading.activeCount() -2}")
print(f"SERVER: started on {ip}")

start()
x.start()
