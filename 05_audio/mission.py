# 프로그램 시작시 녹음 시작
# Enter 를 누르면 녹음 중단
# 파일 명 묻기
# 녹음 파일 저장
from threading import Thread
import pyaudio
import wave
from time import sleep
    
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000

frames = None #녹음 데이터 저장
recording = False #녹음 상태 관리

audio = pyaudio.PyAudio()

def record():
    global frames, recording

    recording = True
    
    stream = audio.open(input_device_index=2, 
                        format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("REC●. .")
    frames = []
    
    while(recording):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)
        
    stream.stop_stream()
    stream.close()
    audio.terminate()
        
def stop_record():
    global recording
    
    recording = False
    sleep(0.1) #대기

def save(fileName):
    fileName += '.wav'
    wf = wave.open(fileName, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(2) #임의로 작성
    wf.setframerate(RATE)
    
    wf.writeframes(b''.join(frames))
    wf.close()

# MainThread
print("녹음 시작")
work = Thread(target=record)
work.start()

key = input("녹음을 종료하고 싶다면 Enter를 눌러주세요")
stop_record()

fileName = input("저장할 파일 명을 입력하세요 . . >> ")
save(fileName)