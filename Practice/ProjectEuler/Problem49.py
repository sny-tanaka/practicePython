# coding: utf-8
'''
項差3330の等差数列1487, 4817, 8147は次の2つの変わった性質を持つ.
(i)3つの項はそれぞれ素数である.
(ii)各項は他の項の置換で表される.
1, 2, 3桁の素数にはこのような性質を持った数列は存在しないが, 4桁の増加列にはもう1つ存在する.
それではこの数列の3つの項を連結した12桁の数を求めよ.
'''
import random
import itertools
import sys


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
    for a in xrange(1488, 10000):
        if prime_numbers(a):
            st = str(a)
            lst = []
            for n in xrange(4):
                x = int(st[n:n+1])
                lst.append(x)
            sortnum = list(itertools.permutations(lst))
            for n in xrange(24):
                b = sortnum[n][0]*1000 + sortnum[n][1]*100 + sortnum[n][2]*10 + sortnum[n][3]
                if a < b and prime_numbers(b):
                    for m in xrange(24):
                        c = sortnum[m][0]*1000 + sortnum[m][1]*100 + sortnum[m][2]*10 + sortnum[m][3]
                        if b < c and prime_numbers(c) and b-a == c-b:
                            print(a*100000000 + b*10000 + c)
                            sys.exit()


if __name__ == '__main__':
    main()
