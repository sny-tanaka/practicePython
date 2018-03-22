# coding: utf-8
'''
三角数, 五角数, 六角数は以下のように生成される.
三角数	Tn=n(n+1)/2	    1, 3, 6, 10, 15, ...
五角数	Pn=n(3n-1)/2	1, 5, 12, 22, 35, ...
六角数	Hn=n(2n-1)	    1, 6, 15, 28, 45, ...
T285 = P165 = H143 = 40755であることが分かる.
次の三角数かつ五角数かつ六角数な数を求めよ.
'''


def is_triangular(n):
    return ((1+8*n)**0.5 - 1) % 2 == 0


def is_pentagonal(n):
    return (1 + (1+24*n)**0.5) % 6 == 0


def create_hexagonal(n):
    return n*(2*n-1)


def main():
    n = 144
    while True:
        hn = create_hexagonal(n)
        if is_triangular(hn) and is_pentagonal(hn):
            break
        n += 1
    print(hn)


if __name__ == '__main__':
    main()
