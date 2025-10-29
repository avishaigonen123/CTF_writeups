"""
aes_bruteforce.py
Brute-force / wordlist-based password attempts for files encrypted with pyAesCrypt.

USAGE (example):
  python aes_bruteforce.py something.zip.aes wordlist.txt

Requirements:
  pip install pyAesCrypt

WARNING:
  - Only use this on files you own or have explicit permission to access.
  - Brute-forcing can be very slow; this script is single-threaded and meant for small/medium wordlists.
"""

import sys
import os
import pyAesCrypt
import tempfile
import time

BUFFER_SIZE = 64 * 1024  # recommended buffer size for pyAesCrypt


def try_password(enc_path, password):
    """
    Try to decrypt enc_path with password.
    Returns path to temporary output file on success, None on failure.
    """
    # create a temporary output file path
    fd, out_path = tempfile.mkstemp(prefix="aes_recover_")
    os.close(fd)
    try:
        pyAesCrypt.decryptFile(enc_path, out_path, password, BUFFER_SIZE)
        # If decryptFile doesn't raise, decryption succeeded.
        return out_path
    except Exception:
        # cleanup and indicate failure
        try:
            os.remove(out_path)
        except OSError:
            pass
        return None


def main():
    if len(sys.argv) != 3:
        print("Usage: python aes_bruteforce.py <encrypted_file> <wordlist_file>")
        sys.exit(2)

    enc_file = sys.argv[1]
    wordlist = sys.argv[2]

    if not os.path.isfile(enc_file):
        print(f"Encrypted file not found: {enc_file}")
        sys.exit(1)
    if not os.path.isfile(wordlist):
        print(f"Wordlist file not found: {wordlist}")
        sys.exit(1)

    total = sum(1 for _ in open(wordlist, "rb"))
    print(f"Starting attempts on '{enc_file}' using wordlist '{wordlist}' ({total} candidates)...")
    start_time = time.time()

    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for i, raw in enumerate(f, 1):
            pw = raw.rstrip("\r\n")
            if not pw:
                continue
            # Attempt decryption
            out = try_password(enc_file, pw)
            if out:
                elapsed = time.time() - start_time
                print(f"\nSUCCESS! Password found: {pw!r}")
                print(f"Decrypted file written to: {out}")
                print(f"Attempts: {i}, Time elapsed: {elapsed:.1f}s")
                print("If you want, move the file to a permanent location and inspect.")
                return
            if i % 100 == 0:
                elapsed = time.time() - start_time
                print(f"Attempted {i}/{total} passwords... (elapsed {elapsed:.1f}s)")

    elapsed = time.time() - start_time
    print(f"\nFinished wordlist. No password found. Time elapsed: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
