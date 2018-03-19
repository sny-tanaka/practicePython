# coding: utf-8
'''
n × (n - 1) × ... × 3 × 2 × 1 を n! と表す.
例えば, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 となる.
この数の各桁の合計は 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 である.
では, 100! の各位の数字の和を求めよ.
'''


def main():
    num = 1
    for i in range(1, 101):
        num = num * i
    s = 0
    while num > 0:
        s += num % 10
        num = num // 10
    print(s)


if __name__ == '__main__':
    main()
