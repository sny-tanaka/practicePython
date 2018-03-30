#include <stdio.h>

#define FALSE 0
#define TRUE 1

int main()
{
    int num = 1;
    int fizz = FALSE;
    int buzz = FALSE;

    for (num = 1; num <= 100; num++)
    {
        if (num % 3 == 0)
        {
            fizz = TRUE;
        }
        else
        {
            fizz = FALSE;
        }

        if (num % 5 == 0)
        {
            buzz = TRUE;
        }
        else
        {
            buzz = FALSE;
        }

        if (fizz == TRUE && buzz == TRUE)
        {
            printf("fizzbuzz\n");
        }
        else if (fizz == TRUE)
        {
            printf("fizz\n");
        }
        else if (buzz == TRUE)
        {
            printf("buzz\n");
        }
        else
        {
            printf("%i\n", num);
        }
    }
}