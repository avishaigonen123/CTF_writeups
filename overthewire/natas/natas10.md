---
layout: default
title: natas10
---



in this challenge we use command injection, this is the vuln part: `passthru("grep -i $key dictionary.txt");`

here we can't use `;`, so we will use this payload we gives 
`a /etc/natas_webpass/natas11`
if you don't get the password for 'a', try insert different characters.

**Flag:** ***`UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk`*** 