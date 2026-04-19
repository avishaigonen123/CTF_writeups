---
layout: default
title: flarebear
---
First, let's install the apk `flarebear.apk` on our android emulator:

```bash
adb install flarebear.apk
```

![](flarebear.png)
Okay, let's create our bear and check for functionalities.  
First, we'll call our bear **kobi**. 

Now, we can see that we have 3 operations: Feed Play and Clean.
![](flarebear-2.png)
After feeding the bear, he pooped and we need to clean his poo.

Fine, now let's start investigating the code using `jadx-gui`.

Inside `AndroidManifest.xml`we can see there are 3 activities, the most interesting one is of course the `MainActivity`:

```xml
<activity android:name="com.fireeye.flarebear.FlareBearActivity"/>  
<activity  
	android:name="com.fireeye.flarebear.NewActivity"  
	android:noHistory="true"/>  
<activity android:name="com.fireeye.flarebear.CreditsActivity"/>  
<activity android:name="com.fireeye.flarebear.MainActivity">  
	<intent-filter>  
		<action android:name="android.intent.action.MAIN"/>  
		<category android:name="android.intent.category.LAUNCHER"/>  
	</intent-filter>  
</activity>
```

Also, the package name is `com.fireeye.flarebear`.

The interesting activity is `FlareBearActivity`.

We can see there is some operation that is called `danceWithFlag()`, which probably shows the flag somehow:

![](flarebear-3.png)

This function is being called inside `setMood`if the code passes some checks:
```java
public final void setMood() {  
        if (isHappy()) {  
            ((ImageView) _$_findCachedViewById(R.id.flareBearImageView)).setTag("happy");  
            if (isEcstatic()) {  
                danceWithFlag();  
                return;  
            }  
            return;  
        }  
        ((ImageView) _$_findCachedViewById(R.id.flareBearImageView)).setTag("sad");  
    }
```

Let's try to simply summon the `danceWithFlag` function using Frida.

We can see the package name is `com.fireeye.flarebeer`:

![](flarebear-4.png)

This will be our script for frida, to create instance of `FlareBearActivity` and then call the function `danceWithFlag`

```js
Java.perform(function() {
    Java.use("com.fireeye.flarebear.FlareBearActivity").getPassword.implementation = function() {
        console.log("Inside getPassword function");
        const password = this.getPassword();
        console.log("Password: " + password);
        return password;
    };

});
```

However, this won't work, because the password that is required to decrypt the flag is based on some parameters that can be obtained only using the normal flow of the program:

![](SCR-20260414-rhjd.png)

![432](flarebear-5.png)

Okay, we can see that the function `danceWithFlag` is being called from `setMood`, which is being called from `clean` (simply click the clean button on the UI).

Also, there are 2 checks we need to check in order to get the `danceWithFlag`, which are `isEcstatic`and `isHappy`.

```java
public final boolean isEcstatic() {  
        return getState("mass", 0) == 72 && getState("happy", 0) == 30 && getState("clean", 0) == 0;  
    }  
  
public final boolean isHappy() {  
	double stat = getStat('f') / getStat('p');  
	return stat >= 2.0d && stat <= 2.5d;  
}
```

Okay, we can see in that each function of the three functionalities has some parameters:

Let's say mass=m, happy=h, clean=cl
- Function feed:
f = 10m + 2h - cl

```java
public final void feed(@NotNull View view) {  
        Intrinsics.checkParameterIsNotNull(view, "view");  
        saveActivity("f");  
        changeMass(10);  
        changeHappy(2);  
        changeClean(-1);  
        incrementPooCount();  
        feedUi();  
    }
```

* Function clean:
p = -2m +4h - cl

```java
public final void play(@NotNull View view) {  
        Intrinsics.checkParameterIsNotNull(view, "view");  
        saveActivity("p");  
        changeMass(-2);  
        changeHappy(4);  
        changeClean(-1);  
        playUi();  
    }
```

* Function clean:
c = -h + 6cl

```java
public final void clean(@NotNull View view) {  
        Intrinsics.checkParameterIsNotNull(view, "view");  
        saveActivity("c");  
        removePoo();  
        cleanUi();  
        changeMass(0);  
        changeHappy(-1);  
        changeClean(6);  
        setMood();  
    }
```

we also need to reach a state where we have:
72m + 30h + 0cl

```java
return getState("mass", 0) == 72 && getState("happy", 0) == 30 && getState("clean", 0) == 0; 
```

Last condition is:
2 <= f/p <= 2.5

```java
double stat = getStat('f') / getStat('p');  
return stat >= 2.0d && stat <= 2.5d; 
```

Okay, let's sumup:
f =   10m + 2h + -cl
p =  -2m + 4h + -cl
c =              -h + 6cl
     72m + 30h + 0cl
so:
10f -2p = 72
-f -p +6c = 0
2f + 4p -c = 30

Let's go chatGPT!

*f=8,p=4,c=2*

Now, let's create new bear.

We'll feed him 8 times, then play with him 4 times, and lastly clean after him 2 times.

![](flarebear-6.png)
We got the flag which is **`th4h_was_be4rly_a_chall3nge@flare-on.com`**
