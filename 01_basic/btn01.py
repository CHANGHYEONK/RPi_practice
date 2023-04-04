import RPi.GPIO as GPIO
import time

button_pin = 26
count = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while (1):
        if (GPIO.input(button_pin) == GPIO.LOW):
            count += 1
            print(count, "Button pushed!")
        time.sleep(0.1)
finally:
    GPIO.cleanup()