---
layout: default
title: Flag19 - Smali Patch
---

Let's first have a look at the challenge:

![400](images/index.png)

This is the code in java:

![](images/SCR-20260430-iycc.png)

It sets the `Firewall` to `INACTIVE`, and then checks if it `ACTIVE`.

In the smali code, we can do 2 things:

1. Change the `if-eqz`, to `if-ne`, and then the check will pass

![](images/index-1.png)

2. Change the value of firewall from `INACTIVE` to `ACTIVE`

![](images/SCR-20260430-jafu.png)

I want to change the `INACTIVE` to `ACTIVE`.

So, first step is to decompile the apk:

```bash
apktool d allsafe.apk -o allsafe/
```

![](images/index-2.png)

Then, we want to find the smali file of the class `SmaliPatch`:

![](images/index-3.png)

So, let's edit this file:

![](images/index-4.png)

I changed it to `ACTIVE`, and saved the file. Now, we need to compile the data back into apk, align the apk and sign it.

```bash
apktool b allsafe -o modified_allsafe.apk
```

![](images/index-5.png)

Now, create the keystore for the application signing:

```bash
keytool -genkeypair \
  -keystore key.keystore \
  -storepass password \
  -keypass password \
  -alias john \
  -keyalg RSA \
  -keysize 2048 \
  -validity 1000 \
  -dname "CN=John Doe, OU=Test, O=Test, L=Test, S=Test, C=US"
```

![](images/index-6.png)

Then, we need to align the apk, before we sign it. Notice we'll use tools from the android sdk, they can be located at `~/Library/Android/sdk/build-tools/<version>/`.

```bash
~/Library/Android/sdk/build-tools/37.0.0/zipalign -p -f -v 4 modified_allsafe.apk allsafe_aligned.apk
```

Next, we need to sign the aligned apk:

```bash
~/Library/Android/sdk/build-tools/37.0.0/apksigner sign \
  --ks key.keystore \
  --ks-pass pass:password \
  --key-pass pass:password \
  allsafe_aligned.apk
```

We can verify that this apk is actually signed:

```bash
~/Library/Android/sdk/build-tools/37.0.0/apksigner verify --verbose allsafe_aligned.apk
```

![](images/index-7.png)

Finally, let's install this apk, after uninstalling the original apk:

![](images/index-8.png)

Will it work?

![400](images/index-9.png)

Yep, it worked :D