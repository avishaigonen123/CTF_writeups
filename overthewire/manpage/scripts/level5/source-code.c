#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int canyou()
{
    int i;
    if (i == 0xdeadbeef)
    {
        printf("I CAN! %d\n", geteuid());
        setreuid(geteuid(), geteuid());
        system("sh");
        return &i;
    }
    else
        canyou();
}

int main()
{
    int x = canyou();
    printf("%p\n", (void *)&x - x);

    return 0;
}