import RPi.GPIO as GPIO
from time import sleep

pin=18
count=30

def fade(pin, direction):
    max_iterations = 100

    if direction == "in":
        GPIO.output(pin,0)
        ident = 1
        iterations = 0
        while iterations < max_iterations:
            sleep((iterations/max_iterations)/max_iterations)
            GPIO.output(pin,0)

            sleep((1-iterations/max_iterations)/max_iterations)
            GPIO.output(pin,1)

            iterations += ident

    if direction == "out":
        GPIO.output(pin,1)
        ident = -1
        iterations = max_iterations
        while iterations > 0:
            sleep((iterations/max_iterations)/max_iterations)
            GPIO.output(pin,0)

            sleep((1-iterations/max_iterations)/max_iterations)
            GPIO.output(pin,1)

            iterations += ident


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)


while count > 0:
    fade(18, "in")
    print ("To LED HIGH")

    fade(18, "out")
    print ("To LED LOW")

    count=count-1

GPIO.output(pin,0)
GPIO.cleanup()
