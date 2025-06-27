#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>

int main() {
    int size = 100;
    int i;
    // Use mmap to allocate memory without initialization (MAP_ANONYMOUS)
   int *ptr = &i;

    // Print the contents of the uninitialized memory as hexadecimal
    int j = 0;
    for (int i = 0; i < size; i++) {
        if (*(ptr + i) != 0) {
            printf("%08x ", *(ptr + i));
            j++;
        }
        if (j % 8 == 0) printf("\n");
    }
        printf("\n");

    return 0;
}