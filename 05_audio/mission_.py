import pyaudio
from threading import Thread
from time import sleep
import wave

CHUNK = 1024                        # 버퍼 크기
FORMAT = pyaudio.paInt16            # 16비트 정수샘플 형식
CHANNELS = 1
RATE = 48000 # 44100

frames = None      # 녹음 데이터 저장
recording = False  # 녹음상태 확인
stream = None
p = None

p = pyaudio.PyAudio()

def start_record() : 
    global frames, recording
    recording = True
    
    stream = p.open(input_device_index = 2, # 자신에게 맞는 장치 번호 지정, 생략가능
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,                    # input -> 마이크장치
                    frames_per_buffer=CHUNK)
    
    print("Start Recording....")
    frames = []

    while recording :
        data = stream.read(CHUNK, exception_on_overflow=False) # 녹음
        frames.append(data)

    print("Recording is finished.")

    


def stop_record() :
    global recording, stream, p
    recording = False
    sleep(0.1)
    if stream is not None :
        stream.stop_stream()
        stream.close()
    if p is not None :
        p.terminate()

def save(file_name) : 
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(2)            # 2byte
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



print("녹음 시작")
t = Thread(target = start_record)
t.start()

input("녹음을 끝내려면 enter를 누르세요")
stop_record()

file_name = input("녹음 파일명 : ")
save(file_name)