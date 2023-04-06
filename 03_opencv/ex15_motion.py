import cv2
from datetime import datetime
from gpiozero import MotionSensor
from time import sleep

cap = cv2.VideoCapture(0) # 0번 카메라
frame_size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

recording = False
recorder = None

def start_record():
    global recorder, recording
    start = datetime.now()
    fname = start.strftime('./data/%Y%m%d_%H:%M:%S.mp4')
    recorder = cv2.VideoWriter(fname, fourcc, 20.0, frame_size)
    # 전역변수 read는 global 선언 안해도 ok / write는 global 선언 필요
    recording = True
    
def stop_record():
    global recorder, recording
    recording = False
    sleep(0.1)
    recorder.release()
    recorder = None
    

pir = MotionSensor(12)
pir.when_motion = start_record
pir.when_no_motion = stop_record


while True:
    if not recording:
        sleep(0.1)
        continue

    retval, frame = cap.read() # 프레임 캡처
    if not retval: break

    now = datetime.now()
    timestamp = now.strftime('REC. %Y-%m-%d %H:%M:%S')
    cv2.putText(frame, timestamp, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 255, 255), 1, cv2.LINE_AA)
    recorder.write(frame)

    # cv2.imshow('frame', frame)
    cv2.waitKey(40)
    # key = cv2.waitKey(25)
    # if key == 27: break # ESC

# cap.release()
# out1.release()

# cv2.destroyAllWindows()