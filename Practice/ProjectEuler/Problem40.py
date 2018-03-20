# coding: utf-8
'''
正の整数を順に連結して得られる以下の10進の無理数を考える:
0.123456789101112131415161718192021...
小数第12位は1である.
dnで小数第n位の数を表す. d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000 を求めよ.
'''


def main():
    # 1桁 1~9 9個
    # 2桁 10~99 90個
    # 3桁 100~999 900個
    # n桁 9×10^(n-1)
    fin = 1
    for p in range(7):
        # 桁数の確定
        order = 10**p
        n = 0
        s = 0
        while s < order:
            n += 1
            r = 9*(10**(n-1)) * n
            s += r
        s -= r
        order -= s  # n桁の中の数字を繋げた内のorder番目
        r = order % n
        k = order // n
        # r=0のときは数字の1の位
        if r == 0:
            k -= 1
            r = n
        # n桁の中のk+1番目の数字の左からr番目の数字
        order = 10**(n-1) + k
        strings = str(order)
        strings = strings[r-1:r]
        order = int(strings)
        fin = fin * order
    print(fin)


if __name__ == '__main__':
    main()
