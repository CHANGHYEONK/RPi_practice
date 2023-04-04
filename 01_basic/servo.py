import RPi.GPIO as GPIO
import time

SERVO_PIN = 14

GPIO.setmode(GPIO.BCM)

GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)


try:
    while True:
        angle = float(input("input angle: "))
        duty = (10 / 180) * angle + 2.5
        servo.ChangeDutyCycle(duty)
        # time.sleep(1)
        # servo.ChangeDutyCycle(12.5)
        # time.sleep(1)
        # servo.ChangeDutyCycle(2.5)
        # time.sleep(1)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()