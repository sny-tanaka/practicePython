#include <stdio.h>

int main()
{
    int price = 0;
    printf("商品の値段 : ");
    scanf("%d円", &price);
    double taxin = price * 1.08;
    int rounded = taxin;
    printf("税込価格 : %d円", rounded);
}