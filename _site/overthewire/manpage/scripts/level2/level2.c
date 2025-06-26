#include<stdio.h>
#include<unistd.h>

int main(int argc, char *argv[]) {
    if(argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }

    char *pathname = "/manpage/manpage2";
    char *new_argv[] = {argv[1], NULL};
    execv(pathname, new_argv);

    return 0;
}
// gcc -m32 level2.c -o level2
