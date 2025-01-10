// gcc -m32 -fno-stack-protector -z execstack -no-pie -Wl,-z,norelro check_shellcode_hex.c -o check_shellcode_hex


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>

typedef void (*FUNC)();

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <shellcode>\n", argv[0]);
        return 1;
    }

    size_t shellcode_size = strlen(argv[1]) / 2; // Each byte is 2 hex characters
    unsigned char *shellcode = mmap(NULL, shellcode_size, 
                                    PROT_READ | PROT_WRITE | PROT_EXEC, 
                                    MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

    if (shellcode == MAP_FAILED) {
        perror("mmap failed");
        return 1;
    }

    // Convert shellcode string to raw bytes
    for (size_t i = 0; i < shellcode_size; i++) {
        sscanf(argv[1] + 2 * i, "%2hhx", &shellcode[i]);
    }

    printf("Shellcode loaded at %p\n", shellcode);

    // Execute the shellcode
    FUNC func = (FUNC)shellcode;
    func();

    // Cleanup
    munmap(shellcode, shellcode_size);

    return 0;
}
