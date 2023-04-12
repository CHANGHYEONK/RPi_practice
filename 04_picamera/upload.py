import requests

# file_name = '20230407_140736.mp4'
# file_path = './' + file_name

# data = {
# 'file_name': file_name
# }
# files = {
# 'sec_file': open(file_path, 'rb')
# }

# response = requests.post('http://172.30.1.106:8000/iot/upload/', 
#                         data=data, files=files)

# data = response.json()
# if data['result'] == 'success':
#     print('upload 성공')
# else:
#     print('실패')

UPLOAD_URL = 'http://172.30.1.106:8000/iot/upload/'

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
    