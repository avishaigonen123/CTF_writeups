---
layout: default
title: CyberGym
---
We will do the series of challenges from [CyberGym](https://github.com/lucideus-repo/cybergym/tree/master/CyberGym%202/mobile)

I won't do the first challenge, because i can't install the raw apk on my emulator. The apk has `.so` file compiled for x86 system, while my Mac can have only arm emulators.

Also, building the source itself was a daunting task I decided to give up on.

So, let's start with the second challenge, here is the apk [com.cybergym.lab2.apk](https://github.com/lucideus-repo/cybergym/blob/master/CyberGym%202/mobile/lab2/app/release/com.cybergym.lab2.apk).

Let's access the app after installing it using adb:

![431](CyberGym.png)

Okay, Let's open it using jadx and read the files.
First, from `AndroidManifest.xml` we can see that the name of the package is `com.moksh.lab2`, and that there is one activity:

```java
<activity android:name="com.moksh.lab2.MainActivity">  
            <intent-filter>  
                <action android:name="android.intent.action.MAIN"/>  
                <category android:name="android.intent.category.LAUNCHER"/>  
            </intent-filter>  
        </activity>
```

We can see in the main activity that it first checks if the application got tempered, and then do another call to some function from the weird package `defpackage.ja`:

![](CyberGym-1.png)

The first function actually checks for something with the application signature:

![](CyberGym-2.png)

However, we don't really want to modify the apk, and anyway we can manually sign it with our key.

The second function takes this two keys from the string.xml file:

![](CyberGym-3.png)

the class itself do some aes decryption, where the first key is encrypted base64 message, and the second key is the key itself for the decryption:

![](CyberGym-4.png)

Let's hook this function and print the result:

```js
Java.perform(function() {
    Java.use("ja").a.overload('java.lang.String','java.lang.String').implementation = function(str1, str2) {
        const res = this.a(str1, str2);
        console.log("result is: " + res);
        return res;
    };
    }
)
```

![](CyberGym-5.png)

Okay, we got some false flag. Interesting.

I tried different approach, I unzipped the apk:

```bash
unzip com.cybergym.lab2.apk -d lab2/
```

Then, I simply searched using grep for the flag:

```bash
grep -rani "cygym3{.*}" --color *
```

![](CyberGym-6.png)

and i got this flag **`cygym3{You_did_it_again_morty}`**

-------

lab3, first i downloaded the apk [com.cybergym.lab3.apk](https://github.com/lucideus-repo/cybergym/blob/master/CyberGym%202/mobile/lab3/app/release/com.cybergym.lab3.apk), and installed it on the emulator using adb.


![400](CyberGym-7.png)
Okay, let's start analyze the files using jadx, first we can see main activity, and that the package name is `com.moksh.lab3`:

```java
<activity android:name="com.moksh.lab3.MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
```

Next, we can see it first checks for tempering, same as on previous challenge. Then, it creates some json object, and send the encrypted flag.

![](CyberGym-8.png)

When we check the code of the class `t`, we can see it creates the flag, and than hash it, and send its `sha256` hash:

![](CyberGym-9.png)

Let's simply hook the function `a` with the one byte param, and grab the value moment before it get hashed. This is the code:

```js
Java.perform(function() {
        Java.use("com.moksh.lab3.t").a.overload('[B').implementation = function(bytes){
            console.log("str is: " + String.fromCharCode.apply(null, bytes));
            return this.a(bytes);
        };
    }
)
```

![](CyberGym-10.png)

So, the flag is **`cygym3{Morty_solved_Frida_flag}`**

-----

Now, we are at part4, the apk is [com.cybergym.lab4.apk](https://github.com/lucideus-repo/cybergym/blob/master/CyberGym%202/mobile/lab4/app/release/com.cybergym.lab4.apk).

![400](CyberGym-11.png)
First, let's analyze the code using jadx, again, we have one main activity and the package name is `com.moksh.lab4`:

```java
<activity android:name="com.moksh.lab4.MainActivity">  
            <intent-filter>  
                <action android:name="android.intent.action.MAIN"/>  
                <category android:name="android.intent.category.LAUNCHER"/>  
            </intent-filter>  
        </activity>
```

We can see that it has some click counter, when we reach 3 it prints the partial flag, and when we reach 10 it resets the counter.

![](CyberGym-12.png)

Also, there is something at the bottom, looks like some encoded or encrypted strings, let's dive into this class.

![](CyberGym-14.png)

The code here looks very simple, it saves the two first strings it gets, and that's all. 

I looked at the `strings.xml` and found that it has firebase url:

![](CyberGym-15.png)

We got two interesting values, first the url `https://moksh-test.firebaseio.com`, and second, the *lbl_url_part2*, which is `/cybergym3.json`.

Let's try to access the firebase database, on this path:
```
https://moksh-test.firebaseio.com/cybergym3.json
```

![](CyberGym-16.png)

So, we got the second part of the flag :)

remember, the first part was `cygym3{damn_morty`, so the full flag will be:
**`cygym3{damn_morty_you_are_smart`**

