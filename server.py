import socket
import time
import threading
import math
import numpy as np
import sympy as sym

Station1 = np.array((100,100))
Station2 = np.array((100,0))
Station3 = np.array((0,0))
Station4 = np.array((0,100))

HEADER = 64

StationNumber = 4
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
    global S1DIST
    global S2DIST
    global S3DIST
    global S4DIST
    global Station1
    global Station2
    global Station3
    global Station4
    while True:
        FLASH = "1"
        for i in STATIONS:
            i.send(FLASH.encode(FORMAT))
        #print(f"{FLASH}")
        time.sleep(1)

        FLASH = "0"
        
        radsq1 = float(S1DIST)**2
        radsq2 = float(S2DIST)**2
        radsq3 = float(S3DIST)**2
        radsq4 = float(S4DIST)**2
        
        
        finrad1 = radsq1 - Station1[0]**2 - Station1[1]**2
        finrad2 = radsq2 - Station2[0]**2 - Station2[1]**2
        finrad3 = radsq3 - Station3[0]**2 - Station3[1]**2
        finrad4 = radsq4 - Station4[0]**2 - Station4[1]**2
        print(finrad1)
        print(finrad2)
        print(finrad3)
        print(finrad4)
        
        x,y = sym.symbols('x,y')
        eq1 = sym.Eq(x**2+y**2-(2*Station1[0])*x-(2*Station1[1])*y,finrad1)
        print(eq1)
        eq2 = sym.Eq(x**2+y**2-(2*Station2[0])*x-(2*Station2[1])*y,finrad2)
        eq3 = sym.Eq(x**2+y**2-(2*Station3[0])*x-(2*Station3[1])*y,finrad3)
        eq4 = sym.Eq(x**2+y**2-(2*Station4[0])*x-(2*Station4[1])*y,finrad4)
        loc = sym.solve([eq1,eq2,eq3,eq4],(x,y))
        print(loc)
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
            #print(thread.name)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            if msg[:2] == "s1":
                S1DIST = msg[3:]
                #print(f"Station 1 distance is {S1DIST}")
            elif msg[:2] == "s2":
                S2DIST = msg[3:]
                #print(f"Station 2 distance is {S2DIST}")
            elif msg[:2] == "s3":
                S3DIST = msg[3:]
            elif msg[:2] == "s4":
                S4DIST = msg[3:]
            #print(f"{addr} {msg}")

            #print(f"Station 1 distance is {S1DIST}")



        time.sleep(0.01)
        #conn.send("test".encode(FORMAT))


def start():
    global thread
    global statnum
    global S1DIST
    global S2DIST
    global S3DIST
    global S4DIST
    server.listen()
    while True:
        if (threading.activeCount() -1) == StationNumber:
            x = threading.Thread(target=trig, args=(conn, addr))
            x.start()
            
        else:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            #thread.name = "Station" + str(statnum)
            #statnum+=1
            #print(f"next station will be {statnum}")
            STATIONS.append(conn)
            #print(thread.name)
            thread.start()

        print(f"[Active Connections] {threading.activeCount() -1}")

print(f"SERVER: started on {ip}")


start()
