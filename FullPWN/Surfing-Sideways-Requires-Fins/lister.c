#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    setuid(0);
    setgid(0);
    int result = system("ls");
    if (result == 0) {
        printf("ls command was successful!\n");
    } else {
        printf("ls command failed!\n");
    }
    return result;
}
