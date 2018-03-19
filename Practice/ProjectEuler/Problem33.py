# coding: utf-8
'''
49/98は面白い分数である.「分子と分母からそれぞれ9を取り除くと, 49/98 = 4/8 となり, 簡単な形にすることができる」
と経験の浅い数学者が誤って思い込んでしまうかもしれないからである. (方法は正しくないが，49/98の場合にはたまたま正しい約分になってしまう．)
我々は 30/50 = 3/5 のようなタイプは自明な例だとする.
このような分数のうち, 1より小さく分子・分母がともに2桁の数になるような自明でないものは, 4個ある.
その4個の分数の積が約分された形で与えられたとき, 分母の値を答えよ.
'''
import fractions


def reduce(p, q):
    common = fractions.gcd(p, q)
    return (p // common, q // common)


def main():
    # ab/cdとしてabの少なくともどちらかとcdの少なくともどちらかに同じ数字が含まれる
    # a=c,a=d,b=c,b=dのいずれか4パターン
    # 0はabcdのいずれにも入らない
    numer = 1
    denom = 1
    for a in range(1, 10):
        for b in range(1, 10):
            # a=c
            c = a
            for d in range(1, 10):
                ab = 10*a + b
                cd = 10*c + d
                if ab < cd and ab*d == cd*b:
                    numer = numer * b
                    denom = denom * d
                    print(ab, cd, b, d)
            # a=d
            d = a
            for c in range(1, 10):
                ab = 10*a + b
                cd = 10*c + d
                if ab < cd and ab*c == cd*b:
                    numer = numer * b
                    denom = denom * c
                    print(ab, cd, b, c)
            # b=c
            c = b
            for d in range(1, 10):
                ab = 10*a + b
                cd = 10*c + d
                if ab < cd and ab*d == cd*a:
                    numer = numer * a
                    denom = denom * d
                    print(ab, cd, a, d)
            # b=d
            d = b
            for c in range(1, 10):
                ab = 10*a + b
                cd = 10*c + d
                if ab < cd and ab*c == cd*a:
                    numer = numer * a
                    denom = denom * c
                    print(ab, cd, a, c)
    numer, denom = reduce(numer, denom)
    print(numer, denom)


if __name__ == '__main__':
    main()
