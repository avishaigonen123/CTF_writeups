# utumno level2 Solution

here, we need to put our shellcode after "sh_". there is a small problem that we can't use "\\" in the shell code, because this char can't be in filname

we use this shellcode: [level2.py](./scripts/level2/level2.py)
and run this script to create the file: [script.sh](./scripts/level2/script.sh)

In the shellcode it tries to execute this command: `system("sh")`, so it means we need to link it to `/bin/sh`.

put the code in the files `cat > script.sh` and `cat > shellcode.py`

these are the commands that you need to run.
```
chmod +x script.sh
ln -sf /bin/sh sh
./script.sh
```
lastly, run this: `/utumno/utumno1 .`

![image](./images/level2.png)

**Flag:** ***`RdUzprHKSm`*** 
