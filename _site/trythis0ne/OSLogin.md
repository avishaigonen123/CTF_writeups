# trythis0ne OSLogin Solution

in this level i need in the HTTP post request to send also admin=1, so, let's use wget in wsl

```
 wget --post-data="user=admin&pass=bla&admin=1&submit=send" http://trythis0ne.com/levels/levels/web-challanges/OSLogin/index.php -O OSLogin.php 
```
and then `cat OSLogin.php`, the password is in the file

**Flag:** ***`WeLoveCola`***
