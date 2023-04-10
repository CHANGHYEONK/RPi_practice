import threading

def sum(low, high) :
    total = 0
    for i in range(low, high) :
        total += i
    print("Subthread", total)

t = threading.Thread(target=sum, args=(1, 100000))
t.start()                                              # 반드시 thread start 해줘야 작업스레드 생성됨.

# t.join() # t 스레드가 끌날 때까지 대기
print("Main Thread")