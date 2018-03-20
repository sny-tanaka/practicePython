# coding: utf-8
'''
問題冊子は以下
https://www.su-gaku.net/common/pdf/support_sample/question/1q_q_1ji.pdf
'''
from sympy import *


def main():
    x = symbols('x')
    fx = atan(1/cos(x))
    fdx = diff(fx, x)
    n = fdx.subs([(x, rad(45))])
    print(n)


if __name__ == '__main__':
    main()
