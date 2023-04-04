import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 20
ECHO = 21

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2)

try:
    while True: 
        GPIO.output(TRIG, True) # Triger 핀에 펄스신호를 만들기 위해 1 출력
        time.sleep(0.00001) # 10µs 딜레이
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            start = time.time() # Echo 핀 상승 시간
        while GPIO.input(ECHO)==1:
            stop= time.time() # Echo 핀 하강 시간

        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm" % distance)
        time.sleep(0.4) # 0.4초 간격으로 센서 측정

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()