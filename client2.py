import socket
import time
import pigpio

TRIGGER = 17
RECEIVE = 27

t1 = 0
t2 = 0
duration = 0.0
durationmicro = 0
dist = 0.0
prevdist = 0
ss = 343
packet = ""

def pingup(gpio, level, tick):
    global t1
    print("echo up ")
    t1 = tick
def pingdown(gpio, level, tick):
    print("echo down ")
    t2 = tick
    durationmicro = t2-t1
    duration = durationmicro/1000000
    distance = ss*duration
    print("duration is %f" % durationmicro)
    print("distance is %f" % distance)
    send(str(distance))

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnected"
ip = "192.168.1.233"
port = 8080

pi = pigpio.pi('localhost',8080)
pi.set_mode(TRIGGER, pigpio.OUTPUT)
pi.set_mode(RECEIVE, pigpio.INPUT)

#cb1 = pi.callback(RECEIVE,pigpio.RISING_EDGE,pingup)
#cb2 = pi.callback(RECEIVE,pigpio.FALLING_EDGE,pingdown)
pi.write(TRIGGER, 0)
print("Settling Sensor")
time.sleep(0.5)

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect((ip,port))

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

while True:
    #resp = (client.recv(2048).decode(FORMAT))
    #pi.gpio_trigger(TRIGGER,10,1)

    time.sleep(0.000001)
