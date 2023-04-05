# Jittering 방지 코드
# 터미널에 sudo pigpiod 치고

from gpiozero import AngularServo
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host = "localhost")

servo = AngularServo(18, 
                    min_angle=0, max_angle=180, 
                    min_pulse_width=0.00054, max_pulse_width=0.0024,
                    pin_factory = factory)

servo.angle = 90

pause()