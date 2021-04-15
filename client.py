import socket
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

TRIGGER = 8
RECEIVE = 7

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(RECEIVE, GPIO.IN)

t1 = 0
t2 = 0
duration = 0
dist = 0
prevdist = 0
ss = 343
packet = ""

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

##send("Hello world!")
while True:
    resp = (client.recv(2048).decode(FORMAT))
    print(resp)

    if resp == "1":
        while GPIO.input(RECEIVE)==0:
            t1 = time.time()
        while GPIO.input(RECEIVE)==1:
            t2 = time.time()

        duration = t2 - t1
        #print("%f" % duration1)

        #print("%f" % dist1)
        if(duration >= 0.038):
            dist = prevdist
            packet = "s1 " + str(dist)
            send(packet)
        else:
            dist = duration*ss
            packet = "s1 " + str(dist)
            send(packet)
            prevdist = dist

        resp = 0

    time.sleep(0.00001)
