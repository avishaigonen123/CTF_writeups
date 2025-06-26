# manpage level1 Solution

here is almost as before, but we defuse the SIGTERM by setting our signal handler, in this case, a simple SIG_IGN.
this will be the injection, [level1.c](./scripts/level1/level1.c), while the payload can be found here [payload.py](./scripts/level1/payload.py). don't forget to put the shellcode in an environment variable, and put the address of the shellcode in `shellcode_address`, in the payload.py file.

![image](./images/level1.png)

**Flag:** ***`s8gSofSE2b`*** 
