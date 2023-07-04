// gcc -g -no-pie vegas.c -o vegas

#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <signal.h>
#include <fcntl.h>

void setup();
void read_string(char* buffer, size_t len); int read_int();
char* read_file(char *);
void give_flag();
void timeout();
void jackpot();
void play();
void reset();
unsigned long random_seed();

char name[0x10];
unsigned long secret_seed;
int score = 0;


void play() {
    printf("\n=================== ALLOCATED A JACKPOT MACHINE ===================\n");

    while (1) {
        printf("Current score: %d\n", score);
        if (score >= 7) {
            jackpot();
            break;
        }

        printf("Give me a number between 1 and 100: ");

        int lucky = rand() % 100 + 1;
        printf("%d\n",lucky);
        //if (lucky == read_int())
        //{
            score++;
            //printf("Lucky!");
        //}
        //else
        //{
           //score = 0;
            //printf("Unlucky!\n");
            //break;
        //}
    }

    printf("Thanks for playing!\n");
    return;
}

void reset()
{
    char buffer[30];
    puts("Believe you can change your fate?");
    read_string(buffer, 20);
    if (!strcmp(buffer, "yes!yes!yes!")) {
        secret_seed = random_seed();
        printf("Tell me your name: ");
        read_string(name, 0x10);
        srand(secret_seed);
    }
}

int main(int argc, char *argv[])
{
    setup();
    puts("");
    printf(" -----------------------------------------------------------------\n");
    printf(" * $ * $ * $ * WELCOME TO VEGAS, THE CITY OF LIGHTS * $ * $ * $ *\n");
    printf(" * $ * $ Guess correctly 7 times in a row to win a prize $ * $ *\n");
    printf(" -----------------------------------------------------------------\n");

    secret_seed = random_seed();
    srand(secret_seed);

    printf("Before we start, tell me your name: ");
    read_string(name, 0x10);

    reset();
    play();

    return 0;
}

// read n bytes from user
void read_string(char* buffer, size_t len)
{
    fflush(stdout);
    int i = 0;
    for (; i < len; ++i)
    {
        read(0, &buffer[i], 1);
        if (buffer[i] == '\n')
        {
            buffer[i] = 0;
            return;
        }
    }
    buffer[i] = 0;
}

// read int from user
int read_int()
{
    char buffer[8];
    read_string(buffer, 5);
    return atoi(buffer);
}

// generate random seed
unsigned long random_seed() {
    unsigned long secret = time(NULL);
    char buf;
    int fd = open("/dev/random", O_RDONLY);
    read(fd, &buf, 1);
    printf("timeNULL: %ld, fd: %d, buf: %d\n", secret, fd, buf); 
    secret = ((secret >> 8) << 8) + 0;
    printf("secret: %ld\n", secret); 
    return secret;
}

void jackpot() {
    printf("\n\n$ $ $ KACHING! CONGRATULATIONS YOU HACKED THE JACKPOT!!! $ $ $\n");
    give_flag();
}

// Read contents of file and return a string containing the contents
char * read_file(char * filename)
{
    char * file_contents = malloc(4096 * sizeof(char));

    FILE * file;
    file = fopen(filename, "r");

    if (file == NULL) {
        printf("\nUnable to open file!\n");
        exit(1);
    }

    fread(file_contents, 4096, sizeof(char), file);
    fclose(file);

    return file_contents;
}

// Print flag
void give_flag()
{
    printf("\n$ * $ * $ YOU'RE A MILLIONAIRE! $ * $ * $\n");
    printf("%s", read_file("/home/vegas/flag"));
}

// Exit program after 10s
void timeout()
{
    printf("\nToo slow... Vegas' security team is watching @.@\n");
    exit(1);
}


void setup()
{
    setvbuf(stdin,  NULL, _IONBF, 0);   // Switch off I/O buffering
    setvbuf(stdout, NULL, _IONBF, 0);   // Switch off I/O buffering
    setvbuf(stderr, NULL, _IONBF, 0);   // Switch off I/O buffering

    signal(SIGALRM, timeout);           // Set program to exit on timeout
    alarm(30);                          // Exit program after 10s
}
