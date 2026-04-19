---
layout: default
title: Python-PyJail-1
---
In this challenge, we need to escape the PyJail. First, when login to the service we get this message:
```
Welcome to my Python sandbox! Everything is in exit() function (arg == get the flag!)
```

We can see that several inputs are disabled, like `__`, `import` and `os`.
Also, when I typed `Ctrl+C` to exit, we got error message that told us this is `python2.7`.

![sandbox](Python-PyJail-1.png)

I know we have the exit function:

![exit function](Python-PyJail-1-1.png)

Since this is python2, we might be able to grab some info from `exit` function without using `__`.
First, I went to my local python2 version, and opened terminal:

```python
>>> def fn(): pass
...
>>> dir(fn)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
```

We can see the `func_code`, which contains:
```python
>>> dir(fn.func_code)
['__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
```

Okay, we grab the `co_code`, and maybe other fields, which we'll check. Notice that the word `name` is banned, so automatically it removes some attributes.

Also, when printing `co_code`, I used '\` \`', to get the raw string and not only printable string.
```python
>>> print `exit.func_code.co_code`
'|\x00\x00d\x01\x00k\x02\x00rH\x00t\x00\x00t\x01\x00\x83\x01\x00\x01d\x02\x00d\x00\x00l\x02\x00}\x01\x00|\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x01d\x02\x00d\x00\x00l\x04\x00}\x02\x00|\x02\x00j\x05\x00\x83\x00\x00\x01n\x05\x00d\x04\x00GHd\x00\x00S'
>>> print `exit.func_code.co_consts`
(None, 'flag-WQ0dSFrab3LGADS1ypA1', -1, 'cat .passwd', 'You cannot escape !')
```

Okay, in the const strings, we can see some flag `flag-WQ0dSFrab3LGADS1ypA1`. Let's try to give it to the exit function:

```python
>>> exit(exit.func_code.co_consts[1])
Well done flag : YjHRUZEa9irCPS2llubR
```

we got the flag **YjHRUZEa9irCPS2llubR**