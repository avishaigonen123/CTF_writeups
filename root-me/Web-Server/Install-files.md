---
layout: default
title: Install-files
---

First, I checked the source code and found this:
`<!--  /web-serveur/ch6/phpbb -->
`

I simply searched google for `install file phpbb` and enterd the first result. 
There, I could see the path `/phpbb/install/install.php`, so I entered him, that's what I got:
```
Congratulations, you've just discovered one of phpBB's many vulnerabilities.<br>
<br>
This vulnerability is actually an oversight by the webmaster who should have removed<br>
these folders. They contain the phpBB forum installation pages.<br>
This kind of thing no longer exists because developers implement<br>
verification systems to make things easier for the most scatterbrained.<br>
What you need to understand, however, is that we often discover a lot of things<br>
by fiddling with URLs...<br>
Thanks to them, you can reset the forum and change all the administrator passwords, since you're resetting the forum.<br>
You then have complete control of the forum!!<br>
<br>
The password to validate is: karambar<br>
<br>
Good luck!
```


**Flag:** **_`karambar`_**
