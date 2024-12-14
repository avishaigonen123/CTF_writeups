#include <stdio.h>
#include<unistd.h>

// Hooked puts function
int puts(const char *str) {
    printf("%p %p %p %p %p %p %p %p %p %p %p\n");

    printf("%s\n", 0x804907d);
    printf("%s\n", 0x804917d);
    printf("%s\n", 0x804a01d);
    printf("%s\n", 0x804a008);

    return 0;
}
