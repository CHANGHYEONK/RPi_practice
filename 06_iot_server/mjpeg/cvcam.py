import time
import numpy as np
import cv2

class MJpegStreamCam :
    def __init__(self, framerate=25, width=640, height=480):
        self.size = (width, height)
        self.framerate = framerate
        self.camera = cv2.VideoCapture(0)
        


    def snapshot(self):
        ret, image = self.camera.read() # 프레임 캡처
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
        is_success, jpg = cv2.imencode(".jpg", image, encode_param)
        return jpg.tobytes()


    def __iter__(self): 
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
        while True:
            ret, image = self.camera.read()
            is_success, jpg = cv2.imencode(".jpg", image, encode_param)
            image = jpg.tobytes()
            yield (b'--myboundary\n'
                    b'Content-Type:image/jpeg\n'
                    b'Content-Length: ' + f"{len(image)}".encode() + b'\n'
                    b'\n' + image + b'\n')
