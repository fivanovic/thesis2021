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

def pingup(gpio, level, tick):
    global t1
    print("echo up ")
    t1 = tick
    #t1 = c.request(NTP_SERVER)
def pingdown(gpio, level, tick):
    print("echo down ")
    t2 = tick
    #t2 = c.request(NTP_SERVER)
    #t2 = t2.tx_time
    durationmicro = t2-t1
    duration = durationmicro/1000000
    duration = t2 - t1
    distance = ss*duration
    print("duration is %f" % duration)
    #print("distance is %f" % distance)
    #send(str(t2))


cb1 = pi.callback(RECEIVE,pigpio.RISING_EDGE,pingup)
cb2 = pi.callback(RECEIVE,pigpio.FALLING_EDGE,pingdown)

while True:
    #resp = (client.recv(2048).decode(FORMAT))
    pi.gpio_trigger(TRIGGER,10,1)
