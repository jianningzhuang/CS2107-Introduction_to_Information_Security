#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
   /* Print UIDs */
   printf("At the beginning of the progam:\n");
   printf("Real user ID = %d, Effective user ID = %d\n\n", getuid(), geteuid());
   fflush(stdout);
 
   /* Change the real UID to 0, and print UIDs again */
   setuid(0);
   printf("After setting the real UID to 0:\n");
   printf("Real user ID = %d, Effective user ID = %d\n\n", getuid(), geteuid());
   fflush(stdout);

   /* Cat the shadow file */
   system("cat /etc/shadow");

   return 0;
}