---
layout: default
title: Flag6 - PIN Bypass
---

Let's first have a look at the challenge:

![400](images/index.png)

Inside the source code we can see the function `checkPin` that checks the pin we input:

![](images/index-1.png)

Let's hook it using frida:

```js
Java.perform(function(){

    var PinBypass = Java.use("infosecadventures.allsafe.challenges.PinBypass");
    PinBypass["checkPin"].implementation = function (pin) {
        console.log(`PinBypass.checkPin is called: pin=${pin}`);
        let result = this["checkPin"](pin);
        console.log(`return true`);
        return true;
    };
})
```

![](images/index-2.png)

And then, we can see that we got access granted:

![400](images/index-3.png)
