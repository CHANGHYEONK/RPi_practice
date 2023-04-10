# 스레드 상속받기

from threading import Thread

class WorkerThread(Thread):

    def __init__(self):
        super().__init__()
        # 속성 초기화


    def run(self):
        # 워커 스레드 작업 정의
        pass

t = WorkerThread()
t.start()               # (주의!) t.run() 은 main thread 가 실행하는것이고, 작업스레드는 생성되지 않는다!!