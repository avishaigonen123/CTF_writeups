---
layout: default
title: OperationsConsole
---

We start with this operations console, I tried to give common users and passwords, nothing helped:

![[Pasted image 20260308194541.png]]

I looked at BurpSuite and so there was some request to `/operations-console/i/api/graphql/auth:login/Login` with the variables I sent, and another things added.

Then, I found the file `assets/main.212f0b4a.js`, which contain several things. First, It contains more endpoints that are aviliable for us:
```js
m = Object.freeze({
                login: c.keys["auth.session.boot"],
                listUsers: c.keys["users.list"],
                profile: c.keys["profile.show"]
            })
```

I tried each endpoint, the first endpoint is the login endpoint

![[Pasted image 20260308195128.png]]

The second is `/users:list/Users`, list all users:

![[Pasted image 20260308194945.png]]

we can see there are 3 users, `guest`, `analyst` and `admin`.

The third endpoint is `/auth:profile/AccessProfile` which require some session token

![[Pasted image 20260308195043.png]]

I looked at the javascript file and found 2 encrypted strings that being decoded using `xor`, I decoded them manuually, and found the first string at features `enable_analysis_access`.

I tried to send it, with differnet usernames as login, and managed to login using `anaylist`:
```
/operations-console/i/api/graphql/auth:login/Login?variables={"username":"analyst","password":"analyst"}&features={"enable_analysis_access":true}
```

![[Pasted image 20260308195315.png]]

The full response is:

```json
{
  "data": {
    "login": {
      "success": true,
      "message": "Legacy analyst console unlocked",
      "token": "8b43e1100a1eb4e1bd9c79ccc39615ecb246edd0",
      "role": "analyst",
      "flag": null
    }
  }
}
```

Okay, I tried to send the token using the cookie `auth_token` which I detected in the source code to the third endpoint

![[Pasted image 20260308195510.png]]

We got back response with internal routes, and also some routeToken 
```json
{
  "data": {
    "accessProfile": {
      "username": "analyst",
      "routes": [
        "/internal/raw"
      ],
      "routeTokens": [
        "59c6c889f95eaa731babdca5c5b14f60"
      ]
    }
  }
}
```

Here I'm a bit stuck, There is another string I decoded which is `ops.analysis.hint`.
Also, there is the hint that was given at the challenge site:

	Enter the government's secret console.  
	Check out this snippet I found while pentesting their secret app:  
	
	/^\s*query\s+[A-Za-z0-9_]+\s*\{[\s\S]*\}\s*$/i

I think it is something to do with graphql, this is the strucutre of query, and i'm probably able to access the original graphql to get request and then grab the flag, but i'm not sure how.

