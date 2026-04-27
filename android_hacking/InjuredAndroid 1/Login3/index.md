---
layout: default
title: Login3
---
This is the challenge:

![400](images/index.png)
This is the `submitFlag` function:

![](images/index-1.png)

It decodes the string `k3FElEG9lnoWbOateGhj5pX6QsXRNJKh///8Jxi8KXW7iDpk2xRxhQ==` which is base64 encoded, and also DES encrypted.

![](images/index-2.png)

Let's hook this function using this frida script:

```js
Java.perform(function (){
	var k = Java.use("b3nac.injuredandroid.k");
	k["a"].implementation = function (str) {
	    console.log(`k.a is called: str=${str}`);
	    let result = this["a"](str);
	    console.log(`k.a result=${result}`);
	    return result;
	};

})
```

![](images/index-3.png)

Okay, the flag is `{This_Isn't_Where_I_Parked_My_Car}`.

We could have hook also the compare function, using same method as on [Login](../Login/index.md).

