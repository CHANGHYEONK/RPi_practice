from datetime import datetime
import requests
from gpiozero import MotionSensor
from signal import pause

INTRUSION_URL = 'http://172.30.1.103:8000/iot/intrusion/'

def notify_intrusion():
    now = datetime.now()
    text = now.strftime("침입감지\n%Y-%m-%d %H:%M:%S")
    params = {
        'text': text,
        'url': 'http://172.30.1.103:8000/iot/mjpeg/'
    }

    response = requests.get(INTRUSION_URL, params = params)
    res = response.json()

    if res['result'] == 'success':
        print('detection notified')
    else:
        print('detection notify fail')
        print(res['reason'])

pir = MotionSensor(12)
pir.when_motion = notify_intrusion
pause()