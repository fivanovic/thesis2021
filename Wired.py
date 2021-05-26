import time
import threading
import math
import numpy as np
import sympy as sym
import localization as lx
import matplotlib.pyplot as plt
import pickle
import pigpio
import os
import ntplib

Station1 = np.array((0,0))
Station2 = np.array((3,0))
Station3 = np.array((0,3))
Station4 = np.array((3,3))

t1 = 0
t2 = 0

S1DIST = 0
S2DIST = 0
S3DIST = 0
S4DIST = 0

s1flip = 0
s2flip = 0
s3flip = 0
s4flip = 0
ss = 343

pi = pigpio.pi()
TRIGGER = 17
RECEIVE1 = 27
RECEIVE2 = 22
RECEIVE3 = 18
RECEIVE4 = 23

pi.set_mode(TRIGGER, pigpio.OUTPUT)
pi.set_mode(RECEIVE1, pigpio.INPUT)
pi.set_mode(RECEIVE2, pigpio.INPUT)
pi.set_mode(RECEIVE3, pigpio.INPUT)
pi.set_mode(RECEIVE4, pigpio.INPUT)

def pingup1(gpio, level, tick):
    global t11
    t11 = tick
def pingdown1(gpio, level, tick):
    global S1DIST
    global s1flip
    t12 = tick
    durationmicro1 = t12-t11
    duration1 = durationmicro1/1000000
    S1DIST = ss*duration1
    s1flip = 1
    print("Ping at 1")
    print("1 distance is %f" % S1DIST)

def pingup2(gpio, level, tick):
    global t21
    t21 = tick
def pingdown2(gpio, level, tick):
    global S2DIST
    global s2flip
    t22 = tick
    durationmicro2 = t22-t21
    duration2= durationmicro2/1000000
    S2DIST = ss*duration2
    s2flip = 1
    print("Ping at 2")
    print(" 2 distance is %f" % S2DIST)

def pingup3(gpio, level, tick):
    global t31
    t31 = tick
def pingdown3(gpio, level, tick):
    global S3DIST
    global s3flip
    t32 = tick
    durationmicro3 = t32-t31
    duration3= durationmicro3/1000000
    S3DIST = ss*duration3
    s3flip = 1
    print("Ping at 3")
    print("3 distance is %f" % S3DIST)

def pingup4(gpio, level, tick):
    global t41
    t41 = tick
def pingdown4(gpio, level, tick):
    global S4DIST
    global s4flip
    t42 = tick
    durationmicro4 = t42-t41
    duration4= durationmicro4/1000000
    S4DIST = ss*duration4
    s4flip = 1
    print("Ping at 4")
    print("4 distance is %f" % S4DIST)


cb1up = pi.callback(RECEIVE1,pigpio.RISING_EDGE,pingup1)
cb1down = pi.callback(RECEIVE1,pigpio.FALLING_EDGE,pingdown1)

cb2up = pi.callback(RECEIVE2,pigpio.RISING_EDGE,pingup2)
cb2down = pi.callback(RECEIVE2,pigpio.FALLING_EDGE,pingdown2)

cb3up = pi.callback(RECEIVE3,pigpio.RISING_EDGE,pingup3)
cb3down = pi.callback(RECEIVE3,pigpio.FALLING_EDGE,pingdown3)

cb4up = pi.callback(RECEIVE4,pigpio.RISING_EDGE,pingup4)
cb4down = pi.callback(RECEIVE4,pigpio.FALLING_EDGE,pingdown4)

while True:
    print("Pinging")
    pi.gpio_trigger(TRIGGER,10,1)
    time.sleep(1)
    P=lx.Project(mode='2D',solver='LSE')
    P.add_anchor('Station1',(Station1[0],Station1[1]))
    P.add_anchor('Station2',(Station2[0],Station2[1]))
    P.add_anchor('Station3',(Station3[0],Station3[1]))
    P.add_anchor('Station4',(Station4[0],Station4[1]))
    device,label=P.add_target()
    if s1flip == 1:
        device.add_measure('Station1',S1DIST)
        s1flip = 0
    if s2flip == 1:
        device.add_measure('Station2',S2DIST)
        s2flip = 0
    if s3flip == 1:
        device.add_measure('Station3',S3DIST)
        s3flip = 0
    if s4flip == 1:
        device.add_measure('Station4',S4DIST)
        s4flip = 0
    P.solve()
    finalloc = device.loc
    xp = round(finalloc.x,2)
    yp = round(finalloc.y,2)
    print("Device is at",xp,",",yp)
    coords = [xp,yp]
    file = open("plotvals.txt","wb")
    pickle.dump(coords,file)
    file.close()
    time.sleep(3)
