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
import gpiozero
import pigpio
import os


try:
    factory = PiGPIOFactory(host='192.168.1.230')
    sens = DistanceSensor(echo=27, trigger=17,pin_factory=factory,max_distance=10)
    GPIO.setmode(GPIO.BOARD)
    TRIGGER = 8
    GPIO.setup(TRIGGER, GPIO.OUT)

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

    #start server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))

    server.listen(1)
    (conn,addr) = server.accept()
    print("Connected")

    while True:
        FLASH = "1"
        GPIO.output(TRIGGER, GPIO.HIGH)
        print(sensor.distance)
        print(time.time())
        sendtime = time.time()
        time.sleep(0.00001)
        GPIO.output(TRIGGER, GPIO.LOW)
        conn.send(FLASH.encode(FORMAT))
        FLASH = '0'
        msg = conn.recv(2048).decode(FORMAT)
        rectime = time.time()
        duration = rectime - sendtime
        print("duration is %f" % duration )
        dist = duration*ss
        print("distance is %f" % dist)
        #print("%f time taken" % duration)
        time.sleep(1)
        #print("%f distance" % dist)



except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
