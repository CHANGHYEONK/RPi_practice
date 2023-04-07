import cv2
from datetime import datetime
from harrdetect import HarrDetect

# har = HarrDetect('haarcascade_frontalface_default.xml')
har = HarrDetect('haarcascade_fullbody.xml')

# cap = cv2.VideoCapture(0) # 0번 카메라
cap = cv2.VideoCapture('./data/vtest.avi')

while True:
    retval, frame = cap.read() # 프레임 캡처
    if not retval: break

    face_list = har.detect(frame, minSize=(40, 40))

    if len(face_list) > 0:
        har.draw_rect(frame, face_list, thickness = 1)
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(25)
    if key == 27: break # ESC

cap.release()
cv2.destroyAllWindows()