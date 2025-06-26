#include<stdio.h>
#include<stdlib.h>

int main(int argc, char* argv[])
{
    if(argc < 2){
        printf("Usage: num of variable is %d, less than expected\n",argc);
        return 1;
    }
    printf("name of var is: %s\n", argv[1]); 
    printf("address is %p\n", (void*)getenv(argv[1]));
        return 0;
}

// this code can be used to get address of env_var, by this way you can override the ret-address
// gcc -m32 get_address.c -o get_address
