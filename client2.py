import socket
import time
import RPi.GPIO as GPIO
from Bluetin_Echo import Echo
from hcrs04sensor import sensor

try:
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
            x=sensor.Measurement

            result = x.basic_distance(TRIGGER,RECEIVE)

            dist = result*2
            print("%f distance" % dist)
            packet = "s1 " + str(dist)
            send(packet)
            prevdist = dist

            resp = 0

        time.sleep(0.00001)

except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
