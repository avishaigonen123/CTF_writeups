# bof Solution

this is simple buffer overflow, notice it takes us 52 bytes till we reach the arguments pass to the function, which is where 0xdeadbeef is stored.
you can use this script [bof.py](./scripts/bof/bof.py) and run this line `(./bof.py ;cat) | nc pwnable.kr 9000`

![image](./images/bof.png)

**Flag:** ***`daddy, I just pwned a buFFer :)`***
