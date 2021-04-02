import socket
import time
import threading

HEADER = 64

FLASH = "0"
THREADS = []
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnected"
CHECKER = "PING"
CONCHECK = 0
CONF = "CONF"
ip = "192.168.1.233"

S1DIST = "0"
S2DIST = "0"
S3DIST = "0"
S4DIST = "0"
#start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, 8080))

#this will be the function that controls the triggering of the sent signal
def trig(conn, addr):
    global FLASH
    while True:
        FLASH = "0"
        #print(f"{FLASH}")
        time.sleep(1)
        FLASH = "1"
        conn.send(FLASH.encode(FORMAT))
        #print(f"{FLASH}")
        time.sleep(1)



#this function will handle each receiver pi or the central receiver pi depending on architecture
def handle_client(conn, addr):
    global FLASH
    global S1DIST
    global S2DIST
    global S3DIST
    global S4DIST
    global thread
    print(f"New Connection {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            print(thread.name)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            if thread.name == "Thread-1":
                S1DIST = msg
            elif thread.name == "Thread-2":
                S2DIST = msg
            elif thread.name == "Thread-3":
                S3DIST = msg
            elif thread.name == "Thread-4":
                S4DIST = msg
            print(f"{addr} {msg}")

            print(f"Station 1 distance is {S1DIST}")



        time.sleep(0.01)
        #conn.send("test".encode(FORMAT))


def start():
    global thread
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        x = threading.Thread(target=trig, args=(conn, addr))
        x.start()
        thread.start()
        
        print(f"[Active Connections] {threading.activeCount() -2}")

print(f"SERVER: started on {ip}")


start()
