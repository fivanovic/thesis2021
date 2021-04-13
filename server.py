import socket
import time
import threading

HEADER = 64

StationNumber = 2 
statnum = 1

FLASH = "0"
STATIONS = []
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
        for i in STATIONS:
            i.send(FLASH.encode(FORMAT))
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
            if msg[:2] == "s1":
                S1DIST = msg[3:]
                print(f"Station 1 distance is {S1DIST}")
            elif msg[:2] == "s2":
                S2DIST = msg[3:]
                print(f"Station 2 distance is {S2DIST}")
            elif thread.name == "Thread-3":
                S3DIST = msg
            elif thread.name == "Thread-4":
                S4DIST = msg
            #print(f"{addr} {msg}")

            #print(f"Station 1 distance is {S1DIST}")



        time.sleep(0.01)
        #conn.send("test".encode(FORMAT))


def start():
    global thread
    global statnum
    server.listen()
    while True:
        if (threading.activeCount() -1) == StationNumber:
            x = threading.Thread(target=trig, args=(conn, addr))
            x.start()
        else:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.name = "Station" + str(statnum)
            statnum+=1
            print(f"next station will be {statnum}")
            STATIONS.append(conn)
            #print(thread.name)
            thread.start()

        print(f"[Active Connections] {threading.activeCount() -1}")

print(f"SERVER: started on {ip}")


start()
