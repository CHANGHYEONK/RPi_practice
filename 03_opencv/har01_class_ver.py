import cv2
from harrdetect import HarrDetect

har = HarrDetect('haarcascade_frontalface_default.xml')

image_file = "./data/face2.jpg"
image = cv2.imread(image_file)

face_list = har.detect(image)

if len(face_list) > 0:
    print(face_list)
    har.draw_rect(image, face_list)
    cv2.imwrite("./data/facedetect-output.PNG", image)
else:
    print("no face")