#include <stdio.h>

/* 偶奇の判定関数 */
char *is_even_odd(int num)
{
    int d = num % 2;
    if (d == 0)
    {
        return "偶数";
    }
    else
    {
        return "奇数";
    }
}

int main()
{
    int a = 0;
    int b = 0;
    printf("a = ");
    scanf("%d", &a);
    printf("b = ");
    scanf("%d", &b);
    printf("aは%s\n", is_even_odd(a));
    printf("bは%s\n", is_even_odd(b));
}