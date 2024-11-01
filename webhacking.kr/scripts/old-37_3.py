import requests
import time


URL = "https://webhacking.kr/challenge/web-18/"
SESSION_ID = "1"
cookies = {'PHPSESSID':SESSION_ID}
# params ={'val':"b UNION database()", 'answer':''}
# while True:
while True:
    filename = "tmp-"+str(int(time.time()))
    # files['upfile'] = "hello:("

    response = requests.get(URL+"tmp/"+filename, cookies=cookies)
    print(response.text)
    if response.status_code==200:
       print(response.text)

