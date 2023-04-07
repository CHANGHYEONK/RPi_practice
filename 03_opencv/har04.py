import cv2
from harrdetect import HarrDetect
from video import Video

cascade = HarrDetect('haarcascade_frontalface_default.xml')

with Video(0) as v:
    for frame in v:
        object_list = cascade.detect(frame)
        if len(object_list) > 0:
            cascade.draw_rect(frame, object_list, thickness=1)

        if not Video.show(frame): break