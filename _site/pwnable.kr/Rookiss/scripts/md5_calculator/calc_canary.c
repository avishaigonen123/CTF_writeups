#include<stdio.h>
#include<stdlib.h>

int main(int argc, char**argv){
    int canary, captcha, seed, arr[8];

    if(argc < 3){
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }

/*
    v10 = __readgsdword(0x14u);
    for ( i = 0; i <= 7; ++i )
        *(_DWORD *)&v2[4 * i] = rand();
    return v6 - v8 + v9 + v10 + v4 - v5 + v3 + v7;
    
    captcha = v6 - v8 + v9 + canary + v4 - v5 + v3 + v7
    canary = captcha - v6 + v8 - v9 - v4 + v5 - v3 - v7
 */
    captcha = atoi(argv[1]);
    seed = atoi(argv[2]);
    srand(seed);

    for(int i=0; i<=7; ++i )
        arr[i] = rand();

    // captcha = arr[4] - arr[6] + arr[7] + canary + arr[2] - arr[3] + arr[1] + arr[5]  
    canary = captcha - arr[4] + arr[6] - arr[7] - arr[2] + arr[3] - arr[1] - arr[5];

    printf("%x\n", canary);
    return 0;
}
// gcc -m32 calc_canary.c -o calc_canary
