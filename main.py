#main code base
import time
import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BOARD)

    TRIGGER = 11
    RECEIVE1 = 13
    RECEIVE2 = 12
    RECEIVE3 = 13
    RECEIVE4 = 15
    t1 = 0
    t2 = 0
    duration1 = 0
    duration2 = 0
    duration3 = 0
    duration4 = 0
    ss = 343

    GPIO.setup(TRIGGER, GPIO.OUT)
    GPIO.setup(RECEIVE1, GPIO.IN)
    GPIO.setup(RECEIVE2, GPIO.IN)

    GPIO.output(TRIGGER, GPIO.LOW)
    print("Settling Sensor")
    time.sleep(2)
    while(True):
        print("Firing")
        GPIO.output(TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIGGER, GPIO.LOW)

        #time.sleep(0.01)
        #print(GPIO.input(RECEIVE))

        while GPIO.input(RECEIVE1)==0:
            t1 = time.time()
        while GPIO.input(RECEIVE1)==1:
            t2 = time.time()

        duration1 = t2 - t1
        print("%f" % duration1)
        dist1 = duration1*ss
        print("%f" % dist1)
        time.sleep(0.5)

        GPIO.output(TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIGGER, GPIO.LOW)



        if(duration1 >= 0.038):
            print("CLEAR STATION 1")
        else:
            print("PING STATION 1 at %.2f" % dist1)





except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
