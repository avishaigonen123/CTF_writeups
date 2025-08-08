---
layout: default
title: JWT-Public-key
---

In the `key` endpoint we get this public key:
```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArqCfzoJbPSEveCcVgLodsT99ZSAJY6CRu7VnyZ2RiiP43S3SntM7c9EbsexWWiXV2JtZoiRPtSZnWuSdrclDoRAgicziyFVy+uJ5cnVWJDvguYYJQOxNuQx2O1W+SfrXj6uR719oCSHwnqtKeXl1bdNPSMPhI8PHxznP5Ab9TFiKz5JT9vzJx9FZvuSXZF3zXFtEfEa3qXiEsc2q68EssrGvcJjpLpAtxn6+2izWp/3ChADxs4L7GA9AAQJQi+7c+9ssYoiLE+cdEwh+4g4k95YtuOvZBydkk8UQK4q7G6nhvpXvZXTdhKySxBi+QWxCx3ipjliQdb+0RUl5AGZdDQIDAQAB
-----END PUBLIC KEY-----
```

In the `auth` endpoint, we supply `username=myName`, and then get this `jwt token`:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXJuYW1lIn0.OC2hLfBVS5DxmycXtWgPsPmcd-FyshZsS36e5NNI3kwWjt0urAIt-nHiTS6ykOe0-N9W8A1wxJZsIWCeor_7KVWCNUqWwjm2wnKf7MUG1AFhfMEoIP8ghrw6voPNmjWUdVpbVKrl05DlM3syL3Q23z47BYPF_t_HW2n0LeUmQrM8TLwRg46WUo3hx8vrocTac2bA_3_Xq6jQnAP2DBIvROLFw281WkxMsv32r3suCOkeKNd3Qw5Kq3uvesO9CY9S5vGUW3FCgy7k5O5FbQO1LfS1Z3-0292_KwKT1QMXMdYKfuBq8e5FNggwlyPxYKt2hsqdD1Xy-LYGpgAzfZgyNA
```
As you can see, it uses `RSA256`
![jwt token](./images/JWT-Public-key_get_jwt.png)

Let's try and go on `algorithm confusion attack`, like shown here https://avishaigonen123.github.io/CTF_writeups/AppSec-IL-2025/PublicEnemy.html.

We supply `HS256`, and sign the public key, and then the server will verify with its public key. This should work because `HS256` is a symmetric algorithm (While RSA is asymmetric).

Let's get the key, using this command: `openssl ec -pubin -in out.pem | base64 -w 0` where `out.pem` contain the key we obtained before.

Then, I'm using jwt-editor to create the key for the symmetric algorithm, the encryption on the client side. Notice we supply the output from the last command (base64 encoded string)
![jwt editor](./images/JWT-Public-key_jwt_editor.png)

Lastly, just create your own payload and sign it using the key: 
![FINAL](./images/JWT-Public-key_FINAL.png)

**Flag:** **_`HardcodeYourAlgoBro`_**
