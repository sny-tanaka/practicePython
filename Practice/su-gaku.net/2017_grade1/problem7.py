# coding: utf-8
'''
問題冊子は以下
https://www.su-gaku.net/common/pdf/support_sample/question/1q_q_1ji.pdf
'''
from sympy import *


def main():
    # 円筒座標に変換して積分
    r, th, z = symbols('r theta z')
    ans = integrate(integrate(integrate(r*z, (z, 0, sqrt(4-r**2))), (r, 0, 1)), (th, 0, 2*pi))
    print(ans)


if __name__ == '__main__':
    main()
