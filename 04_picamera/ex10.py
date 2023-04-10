from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(1280, 720), framerate=30)
sleep(2)

# 고정된 설정으로 여러 사진 찍기
camera.capture_sequence([f'image{i:02d}.jpg' for i in range(10)])