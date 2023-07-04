#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <signal.h>
#include <fcntl.h>

unsigned long secret_seed;

unsigned long random_seed() {
    unsigned long secret = time(NULL);
    char buf;
    int fd = open("/dev/random", O_RDONLY);
    read(fd, &buf, 1);
    //printf("timeNULL: %ld, fd: %d, buf: %d\n", secret, fd, buf); 
    secret = ((secret >> 8) << 8) + 0;
    //printf("secret: %ld\n", secret); 
    return secret;
}


int main() {
    secret_seed = random_seed();
    secret_seed = random_seed();
    srand(secret_seed);
    for (int i = 0; i < 7; i++){
    	printf("%02d", rand() % 100 + 1);
    }

    return 0;
}
