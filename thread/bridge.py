from threading import Lock

class Bridge :
    def __init__(self):
        self.counter = 0
        self.name = "아무개"
        self.address = "모름"
        self.lock = Lock()

    def across(self, name, address) :
        self.lock.acquire()
        # Critical Section 보호 ##########
        self.counter += 1
        self.name = name
        self.address = address
        self.check()
        # ################################ 오직 1개의 스레드만 작업가능한 공간이 됨
        self.lock.release()

    def toString(self) :
        return "이름: {}, 출신:{}, 도전 횟수: {}".format(self.name, self.address, self.counter)
    
    def check(self) :
        if self.name[0] != self.address[0] :
            print("문제 발생!!!! " + self.toString())