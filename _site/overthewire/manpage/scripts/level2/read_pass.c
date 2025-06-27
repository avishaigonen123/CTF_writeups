#include<stdio.h>

int main(){
    int fd = 3;
    char pass[32];

    if(lseek(fd, 0, 0) == -1){
        printf("Error: lseek failed\n");
        return 1;
    }
    if(read(fd, pass, 32) == -1){
        printf("Error: read failed\n");
        return 1;
    }

    printf("Password: %s\n", pass);
    return 0;
}
// gcc -m32 read_pass.c -o read_pass
