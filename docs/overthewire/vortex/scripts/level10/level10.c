#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h> 
#include <string.h>

#define PATH "/vortex/vortex10"

int checkSeed(int* numbers, int* checkBuffer) {
    for (int i = 0; i < 20; i++) {
        if (numbers[i] != checkBuffer[i])
            return 0;
    }
    return 1;
}

// Function to convert the captured string into a numbers array
void parseVortexOutput(char* output, int* numbers) {
    char* token = strtok(output, "[], ");
    int index = 0;

    while (token != NULL && index < 20) {
        sscanf(token, "%x", &numbers[index]);
        token = strtok(NULL, "[], ");
        index++;
    }
}

int main(int argc, char** argv){
    if (argc < 2) {
        printf("not enough params\n");
        return 1;
    }
    
    int numbers[20];
    parseVortexOutput(argv[1], numbers);

    int checkBuf[20];

    time_t time_start = time(NULL) - 500;
    time_t time_end = time(NULL) + 500;
    int seed;
    int i;
    int iVar3;

    for (int tVar2 = time_start; tVar2 <= time_end; tVar2++) {
        for (int local_8c = 0x180; local_8c >= -0x20; local_8c--) {
            seed = tVar2 + local_8c;
            srand(seed);
            setvbuf(stdout, (char*)0x0, 2, 0);
            for (i = 0; i < local_8c; i = i + 1) {
                rand();
            }
            //putchar(0x5b);
            for (i = 0; i < 20; i = i + 1) {
                iVar3 = rand();
                checkBuf[i] = iVar3;
                //printf(" %08x,", iVar3);
            }
            //puts("]");

            if (checkSeed(numbers, checkBuf)) {
                // Print the seed as raw binary bytes
                fwrite(&seed, sizeof(seed), 1, stdout);
                printf("\n");
                return 1;
            }
        }
    }
    return 0;
}
