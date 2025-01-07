#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void handle_sigint(int sig) {
    int j;
    printf("got signal \n");
    printf("%p \n",&j);
}

int main(int argc, char **argv) {
    if(argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    pid_t pid = atoi(argv[1]);

    if (signal(SIGINT, handle_sigint) == SIG_ERR) {
        perror("Unable to set signal handler");
        return 1;
    }

    signal(SIGINT, SIG_IGN);

    int stam;
    int buff[2048];
    for(int i=0;i<2048;i++){
       buff[i]=*(buff-i);
    }
    //printf("%p \n",&stam);
    for(int i=0;i<2048;i+=16){
        printf("\n%p: ",(buff-i));
        for(int j=0;j<16;j++){
            printf("%p ",buff[i+j]);
        }
    }
    int value_to_send = 0xdeadbeef;

    union sigval sv;
    sv.sival_int = value_to_send;       // Set the integer value

    pid_t pid = getpid();
    if (sigqueue(pid, SIGINT, sv) == -1) {
        perror("sigqueue");
        exit(EXIT_FAILURE);
    }

    value_to_send = 0xbbbbbbbb;
    sv.sival_int = value_to_send;       // Set the integer value

    // scanf("%d",&stam);
    for(int i=0;i<2048;i++){
       buff[i]=*(buff-i);
    }
    //printf("%p \n",&stam);
    for(int i=0;i<2048;i+=16){
        printf("\n%p: ",(buff-i));
        for(int j=0;j<16;j++){
            printf("%p ",buff[i+j]);
        }
    }

    return 0;
}

// gcc -m32 code.c -o code
