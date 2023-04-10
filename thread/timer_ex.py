import threading
from time import sleep

def do_something():
    print('time out!')

timer = threading.Timer(2, do_something)
timer.start()

sleep(1)
timer.cancel()

timer = threading.Timer(2, do_something)
timer.start()

print('Main Thread Exit')