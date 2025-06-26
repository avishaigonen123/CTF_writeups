#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

#define PATH_BACKGROUND "/tmp/manpage5_sol"

int main(int argc, char **argv) {
    if(argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    pid_t pid = atoi(argv[1]);

    int value_to_send = 0xdeadbeef;

    union sigval sv;
    sv.sival_int = value_to_send;       // Set the integer value

    if (sigqueue(pid, SIGINT, sv) == -1) {
        perror("sigqueue");
        exit(EXIT_FAILURE);
    }

    return 0;
}

// gcc -m32 code.c -o code
