#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define SPRAY_SIZE (1024 * 1024 * 256) // 256 MB per process
#define NUM_PROCESSES 10  // Number of processes
#define NUM_THREADS 10   // Number of threads per process
#define NUM_ELEMENTS (SPRAY_SIZE / sizeof(unsigned int))

// Function to fill a static array with 0xdeadbeef
void *spray_memory(void *arg) {
    static unsigned int mem[NUM_ELEMENTS]; // Static array, size of 256MB

    for (size_t i = 0; i < NUM_ELEMENTS; i++) {
        mem[i] = 0xdeadbeef;
    }

    // No need to free memory as we use static allocation
    return NULL;
}

// Function to spawn multiple threads in a process
void spray_in_process() {
    pthread_t threads[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS; i++) {
        if (pthread_create(&threads[i], NULL, spray_memory, NULL) != 0) {
            perror("pthread_create failed");
            exit(1);
        }
    }

    // Wait for all threads to complete
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }
}

int main() {
    for (int i = 0; i < NUM_PROCESSES; i++) {
        if (fork() == 0) {
            // Inside child process
            spray_in_process();
            exit(0);
        }
    }

    // Wait for all child processes to complete
    for (int i = 0; i < NUM_PROCESSES; i++) {
        wait(NULL);
    }

    // Optionally, print message after spraying is complete
    printf("Memory spraying complete.\n");
    // char *args[] = {"/manpage/manpage5", NULL};  // Arguments (NULL-terminated)

    // if (execve(args[0], args) == -1) {
    //     perror("execve failed");
    // }

    return 0;
}