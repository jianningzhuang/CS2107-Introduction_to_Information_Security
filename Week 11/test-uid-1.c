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
  
   /* Cat the shadow file */ 
   system("cat /etc/shadow");

   return 0;
}