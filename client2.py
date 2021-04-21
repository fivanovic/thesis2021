import socket
import time
import pigpio
import ntplib

TRIGGER = 17
RECEIVE = 27
a=0
t1 = 0
t2 = 0
duration = 0.0
durationmicro = 0
dist = 0.0
prevdist = 0
ss = 343
packet = ""

NTP_SERVER = 'dk.pool.ntp.org'
c = ntplib.NTPClient()

def pingup(gpio, level, tick):
    global t1
    print("echo up ")
    #t1 = tick
    #t1 = c.request(NTP_SERVER)
def pingdown(gpio, level, tick):
    print("echo down ")
    #t2 = tick
    t2 = c.request(NTP_SERVER)
    t2 = t2.tx_time
    #durationmicro = t2-t1
    #duration = durationmicro/1000000
    #duration = t2 - t1
    #distance = ss*duration
    #print("duration is %f" % durationmicro)
    #print("distance is %f" % distance)
    send(str(t2))

def checkup(gpio, level, tick):
    print("trig up")
def checkdown(gpio, level, tick):
    print("trig down ")


HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnected"
ip = "192.168.1.233"
port = 8080

pi = pigpio.pi()
pi.set_mode(TRIGGER, pigpio.OUTPUT)
pi.set_mode(RECEIVE, pigpio.INPUT)

cb1 = pi.callback(RECEIVE,pigpio.RISING_EDGE,pingup)
cb2 = pi.callback(RECEIVE,pigpio.FALLING_EDGE,pingdown)
#cb3 = pi.callback(TRIGGER,pigpio.RISING_EDGE,checkup)
#cb4 = pi.callback(TRIGGER,pigpio.FALLING_EDGE,checkdown)
pi.write(TRIGGER, 0)
print("Settling Sensor")
time.sleep(0.5)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

while True:
    resp = (client.recv(2048).decode(FORMAT))
    pi.gpio_trigger(TRIGGER,10,1)
    #a+=1
