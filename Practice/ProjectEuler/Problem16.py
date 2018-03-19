# coding: utf-8
'''
2^15 = 32768 であり, 各位の数字の和は 3 + 2 + 7 + 6 + 8 = 26 となる.
同様にして, 2^1000 の各位の数字の和を求めよ.
'''


def main():
    num = 1
    for i in range(1000):
        num = num * 2
    s = 0
    while num > 0:
        s += num % 10
        num = num // 10
    print(s)


if __name__ == '__main__':
    main()
