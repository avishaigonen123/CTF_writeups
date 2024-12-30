#include<stdio.h>
#include<unistd.h>

#define PATH "/vortex/vortex13"

int main() {
    char *argv[] = {NULL};
    char *path = "/vortex/vortex13";
    char *envp[] = {NULL};
    execve(path, argv ,envp);
    return 0;
}
// gcc -m32 level13.c -o level13
