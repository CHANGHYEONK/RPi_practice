# 인터넷에서 파일 다운로드받기

from threading import Thread 
import requests
import time

def getHtml(url):
    resp = requests.get(url) 
    time.sleep(1)
    print(url, len(resp.text), resp.text)          # text / content / json() 등을 다운받을 수 있음.

t1 = Thread(target=getHtml, args=('https://naver.com',))
# t1.daemon = True   # start()보다 먼저 설정해줘야함
t1.start()