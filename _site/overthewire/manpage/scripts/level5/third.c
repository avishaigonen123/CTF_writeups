#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

#define PATH_BACKGROUND "/tmp/manpage5_sol/background"

int main() {
    pid_t pid = fork();


    if (pid == 0) {
        // Child process: execute the background task
        printf("Hello from child, executing background task\n");
        char* path = PATH_BACKGROUND;
        char* args[2] = {path, NULL};
        execv(path, args);
        perror("execv failed");
        exit(EXIT_FAILURE);
    } 
    else if (pid > 0) {
        // Parent process: send the signal
        sleep(1); // Give the child process time to set up
        printf("Hello from parent, sending signal to child (PID: %d)\n", pid);

        int value_to_send = 0xaaaaaaaa;
        union sigval sv;
        sv.sival_int = value_to_send;

        if (sigqueue(pid, SIGSTOP, sv) == -1) {
            perror("sigqueue");
            exit(EXIT_FAILURE);
        }
        
        if (sigqueue(pid, SIGCONT, sv) == -1) {
            perror("sigqueue");
            exit(EXIT_FAILURE);
        }
    } 
    else {
        perror("fork failed");
        exit(EXIT_FAILURE);
    }

    return 0;
}
// gcc -m32 third.c -o third
