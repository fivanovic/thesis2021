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

Station1 = np.array((100,100))
Station2 = np.array((100,0))
Station3 = np.array((0,0))
Station4 = np.array((0,100))

t1 = 0
t2 = 0

S1DIST = 0
S2DIST = 0
S3DIST = 0
S4DIST = 0
ss = 343

pi = pigpio.pi()
TRIGGER = 17
trig2 = 21
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
    #print("echo up ")
    t11 = tick
def pingdown1(gpio, level, tick):
    global S1DIST
    #print("echo down ")
    t12 = tick
    durationmicro1 = t12-t11
    duration1 = durationmicro1/1000000
    S1DIST = ss*duration1
    print(" 1 duration is %f" % duration1)
    print("1 distance is %f" % S1DIST)

def pingup2(gpio, level, tick):
    global t21
    #print("echo up ")
    t21 = tick
def pingdown2(gpio, level, tick):
    global S2DIST
    #print("echo down ")
    t22 = tick
    durationmicro2 = t22-t21
    duration2= durationmicro2/1000000
    S2DIST = ss*duration2
    print(" 2 duration is %f" % duration2)
    print(" 2 distance is %f" % S2DIST)

def pingup3(gpio, level, tick):
    global t31
    #print("echo up ")
    t31 = tick
def pingdown3(gpio, level, tick):
    global S3DIST
    #print("echo down ")
    t32 = tick
    durationmicro3 = t32-t31
    duration3= durationmicro3/1000000
    S3DIST = ss*duration3
    print("3 duration is %f" % duration3)
    print("3 distance is %f" % S3DIST)

def pingup4(gpio, level, tick):
    global t41
    #print("echo up ")
    t41 = tick
def pingdown4(gpio, level, tick):
    global S4DIST
    #print("echo down ")
    t42 = tick
    durationmicro4 = t42-t41
    duration4= durationmicro4/1000000
    S4DIST = ss*duration4
    print("4 duration is %f" % duration4)
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
    pi.gpio_trigger(trig2,10,1)
    time.sleep(1)
