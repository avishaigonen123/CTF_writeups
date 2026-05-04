---
layout: default
title: part2
---
After finishing the setup on [part1](./part1), we can start research the app.

### Developer Backdoors

When trying to login, it calls the function `performLogin`, which creates intent for the class `DoLogin` with the username and password:

![](images/index.png)


Then, it calls the function `postData`. In the read boxes we can see it has the regular endpoint `/login`, and also special endpoint `/devlogin` that can be accessed using the username `devadmin`.

![400](images/index-12.png)

In addition, I've marked some more interesting code parts that might be vulnerable.

![](images/index-2.png)

### Insecure Logging mechanism

We can see here also insecure logging, when login success, it prints the credentials for the log:

```bash
adb logcat --pid=$(adb shell pidof -s com.android.insecurebankv2) '*:D'
```

![](images/index-15.png)

### Sensitive Information in Memory

Let's explore them, first, the `saveCreds`:

![](images/index-3.png)

it saves inside `mySharedPreferences.xml`, the encoded username and the super secure password, which uses some unique `CryptClass` that is probably vulnerable.

![](images/index-4.png)

We can grab the username, and the password, note I logged in with the username `devadmin`:

```bash
echo 'ZGV2YWRtaW4=' | base64 -d; echo
devadmin
```

This can be used for username enumeration. More interestingly, we can go back to the login page, remember we have the `Autofiil Credentials`.

![](images/index-5.png)

It simply grabs the data from the shared preferences. Since the username isn't encrypted, we can change the username and then use the same encrypted password that was used by another user to login in the past. 
In addition, we can login via the stored credentials, without knowing them, because that's what the button gives us.

### Insecure Content Provider access

Okay, now back to `trackUserLogin`:

![](images/index-6.png)

We can see it saves the data inside `mydb.db`:

![](images/index-7.png)

More interesting, it is contentProvider, means that we can assess the data by using query to:

```
content://com.android.insecurebankv2.TrackUserContentProvider/trackerusers
```

When checking on the `AndroidManifest.xml`, we can see it is exported:

![](images/index-8.png)

So, it means every application can simply query to credentials, via the content provider. For example, using `adb`:

```bash
adb shell content query --uri content://com.android.insecurebankv2.TrackUserContentProvider/trackerusers --projection '"*"'
```

![](images/index-9.png)

Notice, it'll work the same way from malicious app on the device, not only the user `shell` of the adb.

### Vulnerable Activity Components

Now, to the last arrow, the red one, we can see it creates explicit intent with the key `uname` and the value of the username, send to the class `PostLogin`.

![](images/index-2.png)

This class get the intent, and spawn the window of after login:

![](images/index-10.png)

This is all fine, however, this class is exported:

![](images/index-13.png)

So, we can easily call it from every application, I'll show that with `adb`:

```bash
adb shell am start -n com.android.insecurebankv2/.PostLogin --es "uname" "kobi"
```

![](images/index-14.png)

And we bypassed the login.

### Root Detection and Bypass

Now, let's explore the application, we can see it says the device is rooted:

![400](images/index-16.png)

This is the function itself that shows this message:

![](images/index-17.png)

We can hook those two functions using frida. Notice I'm initiating an instance, and just then hook the functions:

```js
Java.perform(function() {
    // Bypass Root detection
    Java.scheduleOnMainThread(function() {
        var PostLogin = Java.use("com.android.insecurebankv2.PostLogin").$new();
        console.log("bypass root detection");
        bypass_root_detection();
    });


})

function bypass_root_detection(){
    var PostLogin = Java.use("com.android.insecurebankv2.PostLogin");
    PostLogin["doesSuperuserApkExist"].implementation = function (s) {
        console.log(`PostLogin.doesSuperuserApkExist is called`);
        return false;   
    };


    var PostLogin = Java.use("com.android.insecurebankv2.PostLogin");
    PostLogin["doesSUexist"].implementation = function () {
        console.log(`PostLogin.doesSUexist is called`);
        return false;
    };
}
```

![](images/index-18.png)

And we bypassed the anti-root:

![400](images/index-19.png)

### Username Enumeration issue

when we try to login, if the user isn't exist we get the message "User Does not Exist" from the server:

![](images/index-20.png)

### Insecure Webview implementation

Let's login back with the debug username `devadmin`, we have the "View Statement" button, it shows are some page:

![400](images/index-21.png)
It loads the file `/sdcard/Statements_{uname}.html`, we can see it enables all the settings that allow `XSS` to exist.

![](images/index-22.png)

We have two ways, one to enter some payload inside the amount, for exampe `<script>alert(1337)</script>`:

![400](images/index-23.png)
And then, when we go back to the view statements, we get the `XSS`:

![400](images/index-24.png)
### Insecure SDCard storage

Another way will be to push the file into the `/sdcard`, because this is external storage:

```bash
adb push Statements_devadmin.html /sdcard/Statements_devadmin.html
```

![](images/index-25.png)

