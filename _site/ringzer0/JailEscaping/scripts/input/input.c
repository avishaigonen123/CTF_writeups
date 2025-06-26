#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

#define PATH "/home/input2/input"

int main()
{
    char *pathname = PATH;
    
    // Stage 1:
    char *argv[100];
    argv[0] = pathname;
    for(int i=1;i<100;i++)
        argv[i] = "";

    argv['A'] = "\x00";
    argv['B'] = "\x20\x0a\x0d";
    argv[100] = NULL;
    
    // Stage 2:
    // char buf[4] = "\x00\x0a\x00\xff";
    // write(0, buf, 4);
    // buf[4] = "\x00\x0a\x02\xff";
    // write(2, buf, 4);
        

    // Stage 3:
    char *envp[2] = {"\xde\xad\xbe\xef=\xca\xfe\xba\xbe", NULL};


    execve(pathname, argv, envp);
    return 0;   
}
// gcc -m32 input.c -o input
