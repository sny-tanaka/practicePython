# coding: utf-8
'''
問題冊子は以下
https://www.su-gaku.net/common/pdf/support_sample/question/1q_q_1ji.pdf
'''
from sympy import *


def main():
    # A^3
    A, B, x = symbols('A B x')
    A = Matrix(([3, 0, 2], [-4, 1, -3], [1, 5, -2]))
    B = Matrix(([3-x, 0, 2], [-4, 1-x, -3], [1, 5, -2-x]))
    A3 = expand(det(B))+x**3
    print(A3)

    # A^5 - 5A^4 + 16A^3 - 24A^2
    A4 = expand(A3*x)
    fn = expand((x**2)*A3 - 5*x*A3 + 16*A3 - 24*(x**2))
    fn = fn.replace('x**4', A4)
    fn = fn.replace('x**3', A3)
    print(fn)


if __name__ == '__main__':
    main()
