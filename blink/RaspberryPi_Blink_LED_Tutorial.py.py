import RPi.GPIO as GPIO
from time import sleep
#Î”Î¹Î±ÎºÎ¿Ï€Î® Î£Ï†Î¬Î»Î¼Î±Ï„Î¿Ï‚
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
while True:
    GPIO.output(18,GPIO.HIGH)
    print ("To LED HIGH")
    sleep(1)
    GPIO.output(18,GPIO.LOW)
    print ("To LED LOW")
    sleep(1)
