#include <stdio.h>
#include <string.h>

void vuln_function(char *source)
{
   char buffer[10];

   printf("\n\nInside vuln_function():\n");
   printf("   Address of the target buffer         = %p\n", &buffer);
   printf("   The return address in the call stack = %p\n", __builtin_return_address(0));

   strcpy(buffer, source);

   printf("   The value of buffer after strcpy()   = %s\n", buffer); 
   printf("   The return address is now            = %p\n\n", __builtin_return_address(0));

   return;
}

int main(int argc, char **argv)
{
   char input_string[200];

   printf("Enter your input string: ");
   gets(input_string);
   vuln_function(input_string);

   printf("The main() is exiting.\n\n");
   return 1;
}
