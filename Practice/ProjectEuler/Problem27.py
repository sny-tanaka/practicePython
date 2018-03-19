# coding: utf-8
'''
オイラーは以下の二次式を考案している:
n2 + n + 41.
この式は, n を0から39までの連続する整数としたときに40個の素数を生成する.
しかし, n = 40 のとき 402 + 40 + 41 = 40(40 + 1) + 41 となり41で割り切れる.
また, n = 41 のときは 412 + 41 + 41 であり明らかに41で割り切れる.
計算機を用いて, 二次式 n2 - 79n + 1601 という式が発見できた.
これは n = 0 から 79 の連続する整数で80個の素数を生成する. 係数の積は, -79 × 1601 で -126479である.
さて, |a| < 1000, |b| ≤ 1000 として以下の二次式を考える (ここで |a| は絶対値)
n2 + an + b
n = 0 から始めて連続する整数で素数を生成したときに最長の長さとなる上の二次式の, 係数 a, b の積を答えよ.
'''


def prime_numbers(n):  # 素数判定関数
    if n < 2:
        return False
    elif n == 2:
        return True
    flg = 1
    for i in range(2, n):
        if n % i == 0:
            flg = 0
            break
    if flg == 1:
        return True
    else:
        return False


def main():
    max_i = 0
    max_a = 0
    max_b = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1000):
            i = 0
            while True:
                n = i*i + a*i + b
                if prime_numbers(n) is True:
                    i += 1
                else:
                    break
            if max_i < i:
                max_i = i
                max_a = a
                max_b = b
    print(max_a*max_b)


if __name__ == '__main__':
    main()
