# coding: utf-8
'''
Christian Goldbachは全ての奇合成数は平方数の2倍と素数の和で表せると予想した.
9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2
後に, この予想は誤りであることが分かった.
平方数の2倍と素数の和で表せない最小の奇合成数はいくつか?
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


def main():
    flg = True
    i = 1
    prime = []
    while flg:
        i += 2
        if prime_numbers(i) is True:
            prime.append(i)
        else:
            flg = False
            for p in prime:
                x = i - p
                if x % 2 == 0:
                    x = x // 2
                    if x ** 0.5 % 1 == 0:
                        print(str(i)+':OK')
                        flg = True
                        break
    print(str(i)+':Fale')


if __name__ == '__main__':
    main()
