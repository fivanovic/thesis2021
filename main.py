#main code base
import time
import pigpio

t1 = 0
t2 = 0
duration1 = 0.0
duration1micro = 0
distance = 0.0
duration2 = 0
duration3 = 0
duration4 = 0
ss = 343

def pingup(gpio, level, tick):
    global t1
    print("echo up ")
    t1 = tick
def pingdown(gpio, level, tick):
    print("echo down ")
    t2 = tick
    duration1micro = t2-t1
    duration1 = duration1micro/1000000
    distance = ss*duration1
    print("duration is %f" % duration1micro)
    #print("distance is %f" % distance)





pi = pigpio.pi()



TRIGGER = 17
RECEIVE1 = 27


pi.set_mode(TRIGGER, pigpio.OUTPUT)
pi.set_mode(RECEIVE1, pigpio.INPUT)

cb1 = pi.callback(RECEIVE1,pigpio.RISING_EDGE,pingup)
cb2 = pi.callback(RECEIVE1,pigpio.FALLING_EDGE,pingdown)

pi.write(TRIGGER, 0)
print("Settling Sensor")
time.sleep(2)
while(True):
    print("Firing")
    pi.gpio_trigger(TRIGGER,10,1)



    #duration1 = t2 - t1
    #print("%f" % duration1)
    #dist1 = duration1*ss
    #print("%f" % dist1)
    time.sleep(0.5)





    #if(duration1 >= 0.038):
        #print("CLEAR STATION 1")
    #else:
        #print("PING STATION 1 at %.2f" % dist1)
