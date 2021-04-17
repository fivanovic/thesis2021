import socket
import time
import math
import numpy as np
import sympy as sym
import localization as lx
import matplotlib.pyplot as plt
import pickle
import pigpio
import os

TRIGGER = 14

Station1 = np.array((100,100))
Station2 = np.array((100,0))
Station3 = np.array((0,0))
Station4 = np.array((0,100))
sendtime = 0
HEADER = 64

StationNumber = 1
statnum = 1

ss = 343

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
port = 8080

S1DIST = "0"
S2DIST = "0"
S3DIST = "0"
S4DIST = "0"

pi = pigpio.pi()
pi.set_mode(TRIGGER, pigpio.OUTPUT)
pi.write(TRIGGER, 0)
print("Settling Sensor")
time.sleep(2)

#start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))

server.listen(1)
(conn,addr) = server.accept()
print("Connected")

while True:
    FLASH = "1"
    print("Firing")
    pi.gpio_trigger(TRIGGER,10,1)
    conn.send(FLASH.encode(FORMAT))
    msg = conn.recv(2048).decode(FORMAT)

    print(msg)

    time.sleep(1)
    





f
