#include<stdio.h>

int main(int argc, char* argv[])
{
	        printf("name of var is: %s\naddress is %p\n", argv[1], getenv(argv[1]));
		        return 0;
}

// this code can be used to get address of env_var, by this way you can override the ret-address
