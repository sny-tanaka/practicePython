# coding: utf-8
'''
n桁パンデジタルであるとは, 1からnまでの数を各桁に1つずつ持つこととする.
例えば2143は4桁パンデジタル数であり, かつ素数である.
n桁（この問題の定義では9桁以下）パンデジタルな素数の中で最大の数を答えよ.
'''
import itertools
import sys
import random


def prime_numbers(q, k=100):  # 素数判定関数
    q = abs(q)
    # 計算するまでもなく判定できるものははじく
    if q == 2:
        return True
    if q < 2 or q & 1 == 0:
        return False

    # n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q-1) >> 1
    while d & 1 == 0:
        d >>= 1

    # 判定をk回繰り返す
    for i in xrange(k):
        a = random.randint(1, q-1)
        t = d
        y = pow(a, t, q)
        # [0,s-1]の範囲すべてをチェック
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q-1 and t & 1 == 0:
            return False
    return True


def main():
    for n in range(9, 0, -1):
        numlist = []
        for num in range(n, 0, -1):
            numlist.append(num)
        panlist = itertools.permutations(numlist, n)
        for pan in panlist:
            strings = ''
            for i in range(n):
                strings += str(pan[i])
            pan = int(strings)
            if prime_numbers(pan) is True:
                print(pan)
                sys.exit()


if __name__ == '__main__':
    main()
