import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

count=30
while count > 0:
    GPIO.output(18,GPIO.HIGH)
    print ("To LED HIGH")
    sleep(1)
    GPIO.output(18,GPIO.LOW)
    print ("To LED LOW")
    sleep(1)
    count=count-1

GPIO.output(pin,0)
GPIO.cleanup()
