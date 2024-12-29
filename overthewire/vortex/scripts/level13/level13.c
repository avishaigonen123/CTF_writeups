#include<stdio.h>
#include<unistd.h>

#define PATH "/vortex/vortex13"

int main() {
    char *args[] = {NULL};
    char *envp[] = {NULL};
    execve(PATH,NULL , NULL);
    return 0;
}
// gcc -m32 level13.c -o level13
