# 스레드에서 이미지파일 다운로드받기

from threading import Thread 
import requests
import time

def getHtml(url):
    resp = requests.get(url)
    with open('./image.png', 'wb') as f:
        f.write(resp.content)


url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'

t1 = Thread(target=getHtml, args=(url,))       # 이 작업스레드는 getHtml 함수가 끝나면 종료된다.
t1.start()                                     # 작업스레드 시작!