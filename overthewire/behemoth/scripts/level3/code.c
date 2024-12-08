#include<stdio.h>
#include<unistd.h>



int main()
{
    pid_t pid = getpid();
    printf("current pid is %d\n", pid);
    char pid_str[20];
    sprintf(pid_str, "%d", pid);
    FILE* file=  fopen(pid_str, "w");
    if (file==NULL){
        printf("Failed to create file\n");
        return 1;
    }

    fprintf(file,"Hello!\n");
    fclose(file);
    const char* filename = "/behemoth/behemoth2";
    execl(filename, filename ,NULL);

}

