from gpiozero import AngularServo
from time import sleep
from signal import pause

servo = AngularServo(18, 
min_angle=0, max_angle=180, 
min_pulse_width=0.00054, max_pulse_width=0.0024)

servo.angle = 90
pause()

# while True:
#     servo.angle = -90
#     sleep(2)
#     servo.angle = 0
#     sleep(2)
#     servo.angle = 90
#     sleep(2)
#     servo.angle = 0
#     sleep(2)