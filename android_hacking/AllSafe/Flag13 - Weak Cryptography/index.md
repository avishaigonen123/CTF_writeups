---
layout: default
title: Flag13 - Weak Cryptography
---

Let's first have a look at the challenge:

![400](images/index.png)

Here, we can see several weak methods.

![](images/index-1.png)

First, it have hardcoded key. In addition, it uses `AES` which is fine, but in `ECB`mode, which is very vulnerable, remember the tux image.

![](images/index-2.png)

We can use frida to hook the messages, for example, hook the string a moment before it get encrypted:

```js
Java.perform(function(){
    var WeakCryptography = Java.use("infosecadventures.allsafe.challenges.WeakCryptography");
    WeakCryptography["encrypt"].implementation = function (value) {
        console.log(`WeakCryptography.encrypt is called: value=${value}`);
        let result = this["encrypt"](value);
        console.log(`WeakCryptography.encrypt result=${result}`);
        return result;
    };
})
```

For example, when trying to encrypt the string `1`:

![](images/index-3.png)

