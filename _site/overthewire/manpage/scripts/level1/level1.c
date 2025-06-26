#include<signal.h>
#include<stdio.h>
#include<unistd.h>

int main(int argc, char **argv){
    if(argc < 2) {
        printf("Usage: too few arguments\n");
        return 1;
    }
    char pathname[20] = "/manpage/manpage1";
    char *argv_new[] = {pathname, argv[1], NULL};
    

    signal(SIGTERM, SIG_IGN);
    execv(pathname, argv);

    return 0;
}
// gcc -m32 level1.c -o level1
