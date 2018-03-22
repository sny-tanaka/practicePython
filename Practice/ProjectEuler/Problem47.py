# coding: utf-8
'''
それぞれ2つの異なる素因数を持つ連続する2つの数が最初に現れるのは:
14 = 2 × 7
15 = 3 × 5
それぞれ3つの異なる素因数を持つ連続する3つの数が最初に現れるのは:
644 = 22 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19
最初に現れるそれぞれ4つの異なる素因数を持つ連続する4つの数を求めよ. その最初の数はいくつか?
'''
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


def prime_factorization(n, prime):
    pf = []
    while n != 1:
        for p in prime:
            if n % p == 0:
                n = n // p
                pf.append(p)
                break
    return pf


def main():
    k = 4  # 素因数の数
    i = 1
    n = 1
    prime = []
    pf_list = []
    while n < k+1:
        i += 1
        if prime_numbers(i):
            prime.append(i)
            pf_list = []
            n = 1
        else:
            pf = prime_factorization(i, prime)
            if len(list(set(pf))) == k:
                # 候補数としてpf_listに一時保存
                pf_list.append(i)
                n += 1
            else:
                pf_list = []
                n = 1
    print(pf_list)


if __name__ == '__main__':
    main()
