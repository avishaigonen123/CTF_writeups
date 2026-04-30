---
layout: default
title: Flag16 - Insecure Providers
---

Let's first have a look at the challenge:

![400](images/index.png)
When looking at `AndroidManifest.xml`, we can see there is an exported content provider named `DataProvider`:

![](images/index-1.png)

When getting down into the source code, we can see that if it gets request of `query`, it simply sends it to the sqlite helper:

![](images/index-2.png)

Let's send query request to this host:

```bash
adb shell content query --uri content://infosecadventures.allsafe.dataprovider
```

![](images/index-3.png)

I got the full table, because when `projection` is null, it interprets it as `*`.

We could have the same result, using the next line:

```bash
adb shell content query --uri content://infosecadventures.allsafe.dataprovider --projection '"*"'
```

Anyway, because this is exported, and also the query is misconfigured, we can get the whole db.