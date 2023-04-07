import cv2
from harrdetect import HarrDetect
from video import Video

cascade = HarrDetect('haarcascade_frontalface_default.xml')

FACE_WIDTH = 200

def detect_face(frame):
    object_list = cascade.detect(frame)

    if len(object_list) > 0:
        cascade.draw_rect(frame, object_list, thickness=1)
        x, y, w, h = object_list[0] # 첫 번째 얼굴
    
        # 얼굴 부분 검출(정사각형으로 영역 지정)
        width = max(w, h)
        x = x + w//2 - width//2
        y = y + h//2 - width//2
        face_image = frame[y:y+width, x:x+width].copy()

        # 얼굴 부분만 좌측 상단에 출력
        face_image = cv2.resize(face_image,
                                dsize=(FACE_WIDTH, FACE_WIDTH), 
                                interpolation=cv2.INTER_AREA)
        frame[0:FACE_WIDTH, 0:FACE_WIDTH] = face_image[:]

        return frame


with Video(0) as v:
    for image in v:
        detect_face(image)
        # 보여주기
        if not Video.show(image): break