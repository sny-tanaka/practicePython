# coding: utf-8
'''
正の整数に以下の式で繰り返し生成する数列を定義する.
n → n/2 (n が偶数)
n → 3n + 1 (n が奇数)
13からはじめるとこの数列は以下のようになる.
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
13から1まで10個の項になる. この数列はどのような数字からはじめても最終的には 1 になると考えられている.
さて, 100万未満の数字の中でどの数字からはじめれば最長の数列を生成するか.
注意: 数列の途中で100万以上になってもよい
'''


def collatz(n):  # コラッツ予想
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count


def main():
    max_cnt = 0
    n = 0
    for i in range(1, 1000000, 2):
        cnt = collatz(i)
        if max_cnt < cnt:
            max_cnt = cnt
            n = i
    print(n)


if __name__ == '__main__':
    main()
