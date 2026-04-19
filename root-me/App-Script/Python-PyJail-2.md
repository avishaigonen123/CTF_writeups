---
layout: default
title: Python-PyJail-2
---
In this challenge, we need to escape the PyJail. First, we got this message:
```
Use getout() function if you want to escape from here and get the flag !
```
I tried the same trick like last time, however, when using the dot, it blocks me:
```python
>>> getout.bla
You're in jail dude ... Did you expect to have the key ?
```

Then, I noticed that the built-in function `getattr` isn't blocked, and also `dir`:
```python
>>> print dir(getout)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
```

I tried to get the dir of the attribute `func_code`:
```python
>>> print dir(getattr(getout,func_code))
You're in jail dude ... Did you expect to have the key ?
```

Not working, however, we can trick it, and use  `dir(getout)[25]` to grab `func_code`:
```python
>>> print dir(getattr(getout,dir(getout)[25]))
['__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
```

Well, now let's do the same operation, but now just grab `co_consts`:
```python
>>> print getattr(getattr(getout, dir(getout)[25]), dir(getattr(getout, dir(getout)[25]))[25])
(' check if arg is equal to the random password ', 'Well done ! Here is your so desired flag : ', 'cat .passwd', 'Hum ... no.', None)
```

Okay, we don't have the random password. Let's scan other attributes of the `getout` function. On the 29 place, I found `func_globals`, which looks interesting:
```python
>>> print getattr(getout,dir(getout)[29])
{'execute': <function execute at 0xb7bbf454>, 'random': <built-in method random of Random object at 0x83c50c>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/challenge/app-script/ch9/ch9.py', 'cmd': <module 'cmd' from '/usr/lib/python2.7/cmd.pyc'>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'passwd': 'a1512870f3e5881e7ff65643b2d7096c', 'intro': '                     __     _ __\n       ___  __ ____ / /__ _(_) /\tWelcome on PyJail2\n      / _ \\/ // / // / _ `/ / / \n     / .__/\\_, /\\___/\\_,_/_/_/  \tUse getout() function if you want to\n    /_/   /___/                 \tescape from here and get the flag !\n', 'Jail': <class __main__.Jail at 0xb7baffbc>, '__name__': '__main__', 'os': <module 'os' from '/usr/lib/python2.7/os.pyc'>, '__doc__': None, 'md5': <built-in function openssl_md5>}
```

Okay, now we just need to grab the password from it, notice we used the `repr` using '\` \`':
```python
>>> print `getattr(getout,dir(getout)[29])`[333:365]
a1512870f3e5881e7ff65643b2d7096c
```

Now, let's give it to the `getout` function:
```python
>>> getout(`getattr(getout,dir(getout)[29])`[333:365])
Well done ! Here is your so desired flag :
ValidateMeDude!
```

![](Python-PyJail-2.png)

So the password is **ValidateMeDude!**