#main code base
import time
import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BOARD)

    TRIGGER = 7
    RECEIVE = 11
    t1 = 0
    t2 = 0
    duration = 0
    ss = 343
        
    GPIO.setup(TRIGGER, GPIO.OUT)
    GPIO.setup(RECEIVE, GPIO.IN)
        
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
            
        while GPIO.input(RECEIVE)==0:
            t1 = time.time()
        while GPIO.input(RECEIVE)==1:
            t2 = time.time()
            
        duration = t2 - t1
        print("%f" % duration)
        dist = duration*ss
        print("%f" % dist)
        if(duration >= 0.038):
            print("CLEAR")
        else:
            print("PING")
        time.sleep(2)
        
        
    
except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
