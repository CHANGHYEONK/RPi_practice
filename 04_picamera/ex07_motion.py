from picamera import PiCamera
from gpiozero import MotionSensor
from datetime import datetime
from signal import pause
from video_util import convert

camera = PiCamera()
camera.framerate = 24
fname = None

def start_record():
    global fname
    start = datetime.now()
    fname = start.strftime("%Y%m%d_%H%M%S")
    camera.start_recording(fname + ".h264")
    print("start recording...", fname)

def stop_record():
    camera.stop_recording()
    src = fname + ".h264"
    dst = fname + ".mp4"
    convert(src, dst)
    print("stop recording")

pir = MotionSensor(21)
pir.when_motion = start_record
pir.when_no_motion = stop_record

camera.start_preview()
pause()