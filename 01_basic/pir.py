import RPi.GPIO as GPIO
import time

led_Y = 16
led_B = 21
sensor = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_Y, GPIO.OUT)
GPIO.setup(led_B, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)
print ("PIR Ready . . . . ")
time.sleep(5)

try:
    while True:
        if GPIO.input(sensor) == 1:
            GPIO.output(led_B, 1)
            GPIO.output(led_Y, 0)
            print("Motion Detected !")
            time.sleep(0.2)

        if GPIO.input(sensor) == 0:
            GPIO.output(led_Y, 1)
            GPIO.output(led_B, 0)
            time.sleep(0.2) 

except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup()