# Why not Solution

I wrote this code that do the reverse operation
```
var a = [];
var u = "administrator";
var k = new Array(176,214,205,246,264,255,227,237,242,244,265,270,283);

for(i=0; i<u.length; i++){
    a.push(-i*10 - u.charCodeAt(i) + k[i]);
}
String.fromCharCode(...a)
```
then, we got this password: `OhLord4309111` and the username is: `administrator`

**Flag:** ***`FLAG-65t23674o6N2NehA44272G24`***
