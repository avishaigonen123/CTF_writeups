---
layout: default
title: Flag18 - Native Library
---

Let's first have a look at the challenge:

![400](images/index.png)

First, let's extract the binaries from the `apk`:

```bash
apktool d allsafe.apk -o allsafe/
```

![](images/index-1.png)

It loads the function `checkPassword` from the file `libnative_library.so`, let's grab this file. Remember to take the one that correspond to your emulator architecture:

![](images/index-2.png)

I opened this `libnative_library.so` inside *Ghidra*:

![](images/index-3.png)

Let's hook this function, and change the return value to true.

```js
Java.perform(function(){
    const checkPass_address = Process.findModuleByName("libnative_library.so").findExportByName("Java_infosecadventures_allsafe_challenges_NativeLibrary_checkPassword");
    Interceptor.attach(checkPass_address, {
        onLeave: function(retval){
            retval.replace(1);
        }
    })

})

```

Now, Execute with frida: 

```bash
frida -U -N infosecadventures.allsafe -l ./frida-script.js
```

![400](images/index-4.png)