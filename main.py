#main code base
import time
import RPi.GPIO as GPIO
try:
    GPIO.setmode(GPIO.BOARD)

    TRIGGER = 7
    RECEIVE = 11
    
    GPIO.setup(TRIGGER, GPIO.OUT)
    GPIO.setup(RECEIVE, GPIO.IN)

    GPIO.output(TRIGGER, GPIO.LOW)
    print("Settling Sensor")
    time.sleep(2)

    print("Firing")
    GPIO.output(TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, GPIO.LOW)
    
    print(GPIO.input(RECEIVE))
    
    if GPIO.input(RECEIVE)==1:
        print(GPIO.input(RECEIVE))
        print("Success!")

finally:
    GPIO.cleanup()
