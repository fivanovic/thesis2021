import socket
import time
import threading
import math
import numpy as np
import sympy as sym
import localization as lx
import matplotlib.pyplot as plt
import pickle
import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BOARD)
    TRIGGER = 8
    GPIO.setup(TRIGGER, GPIO.OUT)

    Station1 = np.array((100,100))
    Station2 = np.array((100,0))
    Station3 = np.array((0,0))
    Station4 = np.array((0,100))

    HEADER = 64

    StationNumber = 1
    statnum = 1


    xp = 0
    yp = 0
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
    threadLock = threading.Lock()
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
        global xp
        global yp
        while True:
            #threadLock.acquire()
            #Hits the trigger
            FLASH = "1"

            #Sends out the signal to each client
            #for i in STATIONS:
                #i.send(FLASH.encode(FORMAT))
            STATIONS[0].send(FLASH.encode(FORMAT))

            GPIO.output(TRIGGER, GPIO.HIGH)
            STATIONS[0].send(FLASH.encode(FORMAT))
            time.sleep(0.00001)
            GPIO.output(TRIGGER, GPIO.LOW)
            #threadLock.release()
            #print(f"{FLASH}")
            time.sleep(1)

            FLASH = "0"

            print(S1DIST)

            #Multilateration from each received distance

            #P=lx.Project(mode='2D',solver='LSE')

            #P.add_anchor('Station1',(Station1[0],Station1[1]))
            #P.add_anchor('Station2',(Station2[0],Station2[1]))
            #P.add_anchor('Station3',(Station3[0],Station3[1]))
            #P.add_anchor('Station4',(Station4[0],Station4[1]))

            #device,label=P.add_target()

            #device.add_measure('Station1',S1DIST)
            #device.add_measure('Station2',S2DIST)
            #device.add_measure('Station3',S3DIST)
            #device.add_measure('Station4',S4DIST)
            #P.solve()
            #finalloc = device.loc
            #print(finalloc)
            #xp = finalloc.x
            #yp = finalloc.y
            #zp = finalloc.z
            #print(xp)
            #print(yp)
            #print(zp)
            #coords = [xp,yp]
            #file = open("plotvals.txt","wb")
            #pickle.dump(coords,file)
            #file.close()
            #time.sleep(5)




    #this function will handle each receiver pi, collecting received information and assigning it to the correct station
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

    #this is the main function, starting all necessary threads and listening for connections
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

except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
