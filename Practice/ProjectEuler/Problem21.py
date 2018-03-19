# coding: utf-8
'''
d(n) を n の真の約数の和と定義する. (真の約数とは n 以外の約数のことである. )
もし, d(a) = b かつ d(b) = a (a ≠ b のとき) を満たすとき, a と b は友愛数(親和数)であるという.

例えば, 220 の約数は 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 なので d(220) = 284 である.
また, 284 の約数は 1, 2, 4, 71, 142 なので d(284) = 220 である.

それでは10000未満の友愛数の和を求めよ.
'''


def divide(n):
    div = 0
    for i in range(1, n):
        if n % i == 0:
            div += i
    return div


def amicable(n):
    div = divide(n)
    if div > n:
        div2 = divide(div)
        if n == div2:
            return n + div
    return 0


def main():
    s = 0
    for i in range(2, 10000):
        s += amicable(i)
    print(s)


if __name__ == '__main__':
    main()
