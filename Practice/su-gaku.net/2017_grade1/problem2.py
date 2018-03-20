# coding: utf-8
'''
問題冊子は以下
https://www.su-gaku.net/common/pdf/support_sample/question/1q_q_1ji.pdf
'''
from sympy import *


def main():
    z = Symbol('z')
    sol = solve(I*(z**2) - 4*(1+2*I)*z + 2*(7+6*I), z)
    print(sol)


if __name__ == '__main__':
    main()
