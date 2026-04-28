---
layout: default
title: Flag7 - Root Detection
---

Let's first have a look at the challenge:

![400](images/index.png)

It uses some well known which is called `RootBeer`:

![](images/index-1.png)

Let's simply hook the function `isRooted`:

```js
Java.perform(function(){
    var RootBeer = Java.use("com.scottyab.rootbeer.RootBeer");
    RootBeer["isRooted"].implementation = function () {
        console.log(`RootBeer.isRooted is called`);
        let result = this["isRooted"]();
        console.log('Bypass root detection');
        return false;
    };
})
```

![](images/index-3.png)

And we got the root detection bypassed

![400](images/index-2.png)