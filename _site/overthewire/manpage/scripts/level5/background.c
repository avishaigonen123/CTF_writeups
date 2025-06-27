#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

#define BUF_SIZE 2048
void handle_sigint(int sig) {
    int j;
    printf("got signal \n");
    printf("%p \n",&j);
}

int main() {
    // if (signal(SIGINT, handle_sigint) == SIG_ERR) {
    //     perror("Unable to set signal handler");
    //     return 1;
    // }

    // signal(SIGINT, SIG_IGN);

    int stam;
    int buff[BUF_SIZE];
    for(int i=0;i<BUF_SIZE;i++){
       buff[i]=*(buff-i);
    }
    //printf("%p \n",&stam);
    for(int i=0;i<BUF_SIZE;i+=16){
        printf("\n%p: ",(buff-i));
        for(int j=0;j<16;j++){
            printf("%p ",buff[i+j]);
        }
    }
    printf("start sleeping\n");
    sleep(5); // Wait for a signal

    printf("end sleeping\n");
    printf("\n\n\n");
    for(int i=0;i<BUF_SIZE;i++){
       buff[i]=*(buff-i);
    }
    //printf("%p \n",&stam);
    for(int i=0;i<BUF_SIZE;i+=16){
        printf("\n%p: ",(buff-i));
        for(int j=0;j<16;j++){
            printf("%p ",buff[i+j]);
        }
    }

    return 0;
}

// gcc -m32 background.c -o background
