# coding: utf-8
'''
三角数の数列は自然数の和で表わされ, 7番目の三角数は 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 である. 三角数の最初の10項は:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
となる.
最初の7項について, その約数を列挙すると, 以下のとおり.
 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
これから, 7番目の三角数である28は, 5個より多く約数をもつ最初の三角数であることが分かる.
では, 500個より多く約数をもつ最初の三角数はいくつか.
'''


def triangular(n):  # 三角数を返す
    s = 0
    for i in range(1, n+1):
        s += i
    return s


def divisors(n):  # 約数の個数を返す
    lst = []
    if n == 1:
        return 1
    for i in range(1, n//2+1):
        if n % i == 0:
            j = n // i
            if j < i:
                break
            lst.append(i)
            lst.append(j)
    return len(lst)


def main():
    n = 0
    i = 0
    while n <= 500:
        i += 1
        t = triangular(i)
        n = divisors(t)
    print(t)


if __name__ == '__main__':
    main()
