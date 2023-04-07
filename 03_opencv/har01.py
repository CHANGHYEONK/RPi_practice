from cv2.data import haarcascades
import cv2

xml = haarcascades + 'haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(xml)

image_file = "./data/face1.jpg" # ./data/face2.jpg
image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1,
                                    minNeighbors=1, minSize=(150,150))

if len(face_list) > 0:
    print(face_list)
    color = (0, 0, 255)
    for face in face_list:
        x,y,w,h = face
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=8)
    cv2.imwrite("./data/facedetect-output.PNG", image)
else:
    print("no face")