#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_NAME_LEN 1024

void win(void)
{
    system("cat /src/flag.txt");
    exit(0);
}

int main(int argc, char ** argv)
{
    char name[16];

    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);

    printf("Please enter your name: ");
    fgets(name, MAX_NAME_LEN, stdin);
    printf("Hello, %s!\n", name);

    return 0;
}
