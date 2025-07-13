import hashlib
import itertools

def find_input():
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for length in range(1, 10):  # Adjust max length as needed
        for candidate in itertools.product(charset, repeat=length):
            s = ''.join(candidate)
            digest = hashlib.sha1(s.encode()).digest()
            if digest[0] == 0x7c and digest[1] == 0x00:
                print(f'Found: {s}')
                return s
    print('No input found.')
    return None

if __name__ == '__main__':
    find_input()