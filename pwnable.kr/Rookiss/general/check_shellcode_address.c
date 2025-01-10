// gcc -m32 -fno-stack-protector -z execstack -no-pie -Wl,-z,norelro check_shellcode_address.c -o check_shellcode_address


#include<stdio.h>
#include<stdlib.h>

typedef void (*FUNC)();

int main(int argc, char* argv[])
{
    if(argc < 2){
        printf("Usage: num of variable is %d, less than expected\n",argc);
        return 1;
    }


    void* func  = (void*)strtoul(argv[1], NULL, 16);
    printf("address received is %p\n", func);

    ((FUNC)func)();
    
    return 0;
}

// this code can be used to get function address, and try execute it
