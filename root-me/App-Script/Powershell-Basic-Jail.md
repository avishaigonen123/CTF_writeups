---
layout: default
title: Powershell-Basic-Jail
---
First step was trying some basic commands, I noticed that letters were missing:
![[Pasted image 20260311135305.png]]

As you can see, the letter `h` is missing. I gave it list of all ascii_letters, using python snippet:
```python
import string;
print(string.ascii_letters)
```

The string is `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`:

```powershell
PS JAIL:\powershell\restricted> abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
abefjklmnopqrstuvwxyzABEFJKLMNOPQRSTUVWXYZ : The term 'abefjklmnopqrstuvwxyzABEFJKLMNOPQRSTUVWXYZ' is not recognized as the name of a cmdlet, function,
script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ abefjklmnopqrstuvwxyzABEFJKLMNOPQRSTUVWXYZ
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (abefjklmnopqrst...LMNOPQRSTUVWXYZ:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

We got back the string `abefjklmnopqrstuvwxyzABEFJKLMNOPQRSTUVWXYZ`, and using short script I identified the missing characters.

```python
>>> for i in string.ascii_letters:
...     if i not in 'abefjklmnopqrstuvwxyzABEFJKLMNOPQRSTUVWXYZ':
...         print(i,end="")
...
cdghiCDGHI
```
This is a bit false positive, after manually checking, I verified that only the letter `h` is being censored.
Same for `string.punctuation`:
```powershell
PS JAIL:\powershell\restricted> !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
iex : At line:1 char:2
+ !"#$%&\')*,.:;<=>?@\\]^_`{|}~
+  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The string is missing the terminator: ".
At C:\cygwin64\challenge\app-script\ch20\ch20.ps1:119 char:5
+     iex $line
+     ~~~~~~~~~
    + CategoryInfo          : ParserError: (:) [Invoke-Expression], ParseException
    + FullyQualifiedErrorId : TerminatorExpectedAtEndOfString,Microsoft.PowerShell.Commands.InvokeExpressionCommand
```

and detecting the missing:
```python
>>> for i in string.punctuation:
...     if i not in '!"#$%&\')*,.:;<=>?@\\]^_`{|}~':
...         print(i,end="")
...
(+-/[
```

So, the missing characters are: `h(+-/[`.
In addition, there are other words like `select`, `sl`, `mp` that are blocked.
Oh, it seems that also `cd` not working, and many others. I need to think on solution. 

Wait, I know it filters the word `cat`:
```powershell
PS JAIL:\powershell\restricted> 'cat'

PS JAIL:\powershell\restricted>
```

However, maybe the filtering isn't recursive, let's put `cat` inside the `cat`:
```powershell
PS JAIL:\powershell\restricted> 'ccatat'
cat
PS JAIL:\powershell\restricted>
```

Well, let's use it to read `.passwd` :D
```powershell
PS JAIL:\powershell\restricted> ccatat .passwd
PowerSh3llIsPowerFull
```

So, we got the password **PowerSh3llIsPowerFull**.
The source code of this challenge, you can see this isn't recursive.

```powershell
[Environment]::SetEnvironmentVariable("Path", "")
$ExecutionContext.SessionState.LanguageMode = "ConstrainedLanguage"

# [System.Console]::WriteLine("Hello")

while($true){
    Write-Host -NoNewline "PS JAIL:\powershell\restricted> "
    $line = Read-Host
    $line = $line -replace '\-',''
    $line = $line -replace '\+',''
    $line = $line -replace '\[',''
    $line = $line -replace '/',''
    $line = $line -replace 'h',''
    $line = $line -replace '\(',''
    $line = $line -replace 'system32',''
    $line = $line -replace 'windows',''
$line = $line -replace 'ac',''
$line = $line -replace 'asnp',''
$line = $line -replace 'clc',''
$line = $line -replace 'clhy',''
$line = $line -replace 'cli',''
$line = $line -replace 'clp',''
$line = $line -replace 'cat',''
$line = $line -replace 'cd',''
$line = $line -replace 'clv',''
$line = $line -replace 'cnsn',''
$line = $line -replace 'compare',''
$line = $line -replace 'cpi',''
$line = $line -replace 'cpp',''
$line = $line -replace 'cvpa',''
$line = $line -replace 'dbp',''
$line = $line -replace 'diff',''
$line = $line -replace 'dnsn',''
$line = $line -replace 'ebp',''
$line = $line -replace 'epal',''
$line = $line -replace 'epcsv',''
$line = $line -replace 'fc',''
$line = $line -replace 'fl',''
$line = $line -replace 'foreach',''
$line = $line -replace 'ft',''
$line = $line -replace 'fw',''
$line = $line -replace 'gal',''
$line = $line -replace 'gbp',''
$line = $line -replace 'gc',''
$line = $line -replace 'gci',''
$line = $line -replace 'gcm',''
$line = $line -replace 'gcs',''
$line = $line -replace 'gdr',''
$line = $line -replace 'ghy',''
$line = $line -replace 'gi',''
$line = $line -replace 'gl',''
$line = $line -replace 'gm',''
$line = $line -replace 'gmo',''
$line = $line -replace 'gp',''
$line = $line -replace 'gps',''
$line = $line -replace 'gpv',''
$line = $line -replace 'group',''
$line = $line -replace 'gsnp',''
$line = $line -replace 'gsv',''
$line = $line -replace 'gu',''
$line = $line -replace 'gv',''
$line = $line -replace 'gwmi',''
$line = $line -replace 'iex',''
$line = $line -replace 'ihy',''
$line = $line -replace 'ii',''
$line = $line -replace 'ipal',''
$line = $line -replace 'ipcsv',''
$line = $line -replace 'ipmo',''
$line = $line -replace 'irm',''
$line = $line -replace 'ise',''
$line = $line -replace 'iwmi',''
$line = $line -replace 'iwr',''
$line = $line -replace 'measure',''
$line = $line -replace 'mi',''
$line = $line -replace 'mp',''
$line = $line -replace 'nal',''
$line = $line -replace 'ndr',''
$line = $line -replace 'ni',''
$line = $line -replace 'nmo',''
$line = $line -replace 'npssc',''
$line = $line -replace 'nv',''
$line = $line -replace 'ogv',''
$line = $line -replace 'oh',''
$line = $line -replace 'rbp',''
$line = $line -replace 'rcsn',''
$line = $line -replace 'rdr',''
$line = $line -replace 'ri',''
$line = $line -replace 'rmo',''
$line = $line -replace 'rni',''
$line = $line -replace 'rnp',''
$line = $line -replace 'rp',''
$line = $line -replace 'rsnp',''
$line = $line -replace 'rv',''
$line = $line -replace 'rvpa',''
$line = $line -replace 'rwmi',''
$line = $line -replace 'sal',''
$line = $line -replace 'saps',''
$line = $line -replace 'sasv',''
$line = $line -replace 'sbp',''
$line = $line -replace 'sc',''
$line = $line -replace 'select',''
$line = $line -replace 'shcm',''
$line = $line -replace 'si',''
$line = $line -replace 'sl',''
$line = $line -replace 'sleep',''
$line = $line -replace 'sort',''
$line = $line -replace 'sp',''
$line = $line -replace 'spps',''
$line = $line -replace 'spsv',''
$line = $line -replace 'start',''
$line = $line -replace 'sv',''
$line = $line -replace 'swmi',''
$line = $line -replace 'tee',''
$line = $line -replace 'trcm',''
$line = $line -replace 'where',''
$line = $line -replace 'write',''
$line = $line -replace 'type',''

    iex $line
}
```
