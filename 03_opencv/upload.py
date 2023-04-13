import requests

UPLOAD_URL = 'http://172.30.1.103:8000/iot/upload/'

def upload(file_path):
    file_name = file_path.split('/')[-1]
    data = {'file_name': file_name}
    files = {'sec_file': open(file_path, 'rb')}

    response = requests.post(UPLOAD_URL, data=data, files=files)
    res = response.json()

    if res['result'] == 'success':
        return True
    else:
        return False


INTRUSION_URL = 'http://172.30.1.103:8000/iot/intrusion/'

def notify_intrusion():
    response = requests.get(INTRUSION_URL)
    res = response.json()

    if res['result'] == 'success':
        return True
    else:
        return False