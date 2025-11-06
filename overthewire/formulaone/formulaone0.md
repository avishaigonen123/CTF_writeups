---
layout: default
title: formulaone0
---

First we login into the server, using ssh to `bandit`
```bash
┌──(me㉿PC4)-[~/formulaOne]
└─$ ssh bandit0@bandit.labs.overthewire.org -p 2220
```

We can find the source code inside `/formulaone`:

```c
bandit0@bandit:/formulaone$ cat formulaone0.c
#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

#define PORT 4091

int createsocket(int portno)
{
  int yes = 1;
        struct sockaddr_in addr;
        bzero(&addr, sizeof(addr));
        addr.sin_family = AF_INET;
        addr.sin_addr.s_addr = INADDR_ANY;
        addr.sin_port = htons(portno);

        int sock = socket(AF_INET, SOCK_STREAM, 0);
        if (sock < 0)
        {
                perror("open socket failed");
                return -1;
        }

        setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int));

        if (bind(sock, (struct sockaddr *)&addr, sizeof(addr)) < 0)
        {
                perror("bind failed");
                close(sock);
                return -1;
        }

        if (listen(sock, 5) < 0)
        {
                perror("listen failed");
                close(sock);
                return -1;
        }

        return sock;
}


int read_byte(int fd) {
  int ret;
  char buf = 0;
//  sleep(1);
  ret = recv(fd, &buf, 1, 0);
  if(ret == 0) { printf("RECV FAIL :(\n"); return -1; }
  if(ret < 0) return 0;

  return buf & 0xff;
}

#ifndef PASSWD
#define PASSWD "s3cret"
#endif

void client(int fd)
{
  int i = 0;

  send(fd, "Password: ", 10, 0);
  for(i=0; i < strlen(PASSWD); i++){
    if( PASSWD[i] != read_byte(fd) ){
      break;
    }
  }

  if(i != strlen(PASSWD) ) {
    send(fd, "WRONG PASSWORD\n", 15, 0);
    close(fd);
  } else {
    dup2(fd,0);
    dup2(fd,1);
    dup2(fd,2);

    system("/bin/sh");
    printf("system just closed\n");
  }
  return;
}

int main()
{
  int fd;
  int n;
        struct sockaddr_in addr;
        socklen_t addrlen = sizeof(addr);

        signal(SIGCHLD, SIG_IGN);


        fd = createsocket(PORT);

  while(1){
    n = accept(fd, (struct sockaddr *)&addr, &addrlen);
//    printf("[+] Connection from %s\n", inet_ntoa(addr.sin_addr));
    if( fork() == 0 ) {
      close(fd);
      client(n);
      exit(0);
    }  else {
      close(n);
    }
  }
}
```

We can see it checks byte by byte if the char is correct. so, there is possible `TOCTOU` situation here:
```C
send(fd, "Password: ", 10, 0);
  for(i=0; i < strlen(PASSWD); i++){
    if( PASSWD[i] != read_byte(fd) ){
      break;
    }
  }
```

We can measure the time it takes to give us "WRONG PASSWORD", and then find char by char. It should take `26*len(password)`, which isn't bruteforce at all.



**Flag:** ***`8YpAQCAuKf`*** 
