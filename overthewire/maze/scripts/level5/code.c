#include <stdio.h>
#include<unistd.h>


int main(){
	
	printf("effective user id: %d\n", geteuid());
    printf("real user id: %d\n", getuid());

    setreuid(geteuid(), geteuid());

    char path[256] = "/bin/sh";
    char* argv[2];
    argv[0] = path;
    argv[1] = NULL;
    execv(path,argv);

    return 0;
}
