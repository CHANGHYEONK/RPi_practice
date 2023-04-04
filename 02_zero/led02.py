from gpiozero import LED
from signal import pause
from time import sleep

led = LED(16)

led.blink()

# pause()
sleep(3)

led.blink(on_time=0.5, off_time=0.5)
sleep(5)

led.blink(on_time=0.2, off_time=1)
sleep(5)