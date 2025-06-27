#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define PATH "/vortex/vortex6"


int main() {
    char *args[] = {"/bin/sh", NULL};
    execv(PATH, args);

    // If execve fails, print an error message
    perror("execve");
    return 1;
}
