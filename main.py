#main code base
import time
import pigpio

def pingup(gpio, level, tick):
    print("echo up")
    tick = t1
def pingdown(gpio, level, tick):
    print("echo down")
    tick = t2


try:

    pi = pigpio.pi()



    TRIGGER = 17
    RECEIVE1 = 27

    t1 = 0
    t2 = 0
    duration1 = 0
    duration2 = 0
    duration3 = 0
    duration4 = 0
    ss = 343

    pi.set_mode(TRIGGER, pigpio.OUTPUT)
    pi.set_mode(RECEIVE1, pigpio.INPUT)

    cb1 = pi.callback(RECEIVE1,RISING_EDGE,pingup)
    cb2 = pi.callback(RECEIVE1,FALLING_EDGE,pingdown)

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





except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
