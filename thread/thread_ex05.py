# 스레드 클래스 상속 및 호출하여 사용(html 다운받기)

import threading, requests, time

class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self) 
        self.url = url
        self.daemon = True      # 데몬스레드 설정, 디폴트는 False


    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), resp.text)


t = HtmlGetter('https://google.com')
t.daemon = True               # 데몬스레드로 실행.

t.start()

# t.join()   # t스레드(작업스레드)가 끝날때까지  메인 스레드가 기다려주는것
print("### End ###")