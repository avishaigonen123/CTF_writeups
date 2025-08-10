---
layout: default
title: SQL-injection-Blind
---

Here we need to extract data using `blind SQL Injection`.
Via the error messages I relized this is `sqlite` behined the scenes, so i gave this query `Select SQL FROM sqlite_master` to extract the schema.

This is the schema:
```
CREATE TABLE users (username TEXT, password TEXT)
```

Then, we extracted line by line from the `users` tables, until we dumped the data.

This script is very fast, I wrote it using chatGPT, and it do the job.
```py
{% include_relative scripts/SQL-injection-Blind.py %}
```

After execution, we get this:
```
Extracted credentials snippets:
Cred 0: user1 DsD6z756f
Cred 1: admin e2azO93
Cred 2: user2 Z28gsya65ze34de
Cred 3:
Cred 4:
```
So, the password is:

```
e2azO93
```

**Flag:** **_`e2azO93`_**