---
layout: default
title: Flag14 - Insecure Service
---

Let's first have a look at the challenge:

![400](images/index.png)
When we check the `AndroidManifest.xml`, we can see this `RecorderService`, which can be exported:

![](images/index-1.png)

We can trying to start this service manually, using `adb`:

```bash
adb shell am startservice infosecadventures.allsafe/.challenges.RecorderService
```

![400](images/index-2.png)

We got audio recording, we can check at `/sdcard/Download`:

![](images/index-3.png)

The vulnerability here is that every app or piece of code that running on the phone, can request this recording. 