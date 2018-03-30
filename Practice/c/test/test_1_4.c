#include <stdio.h>

int main()
{
    int a = 0;
    int b = 0;
    int c = 0;
    printf("a = ");
    scanf("%d", &a);
    printf("b = ");
    scanf("%d", &b);
    printf("c = ");
    scanf("%d", &c);
    printf("aを10で割った余りは%d\n", a % 10);
    printf("bを10で割った余りは%d\n", b % 10);
    printf("cを10で割った余りは%d\n", c % 10);
}