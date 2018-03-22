# coding: utf-8
'''
五角数は Pn = n(3n-1)/2 で生成される. 最初の10項は
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
である.
P4 + P7 = 22 + 70 = 92 = P8 である. しかし差 70 - 22 = 48 は五角数ではない.
五角数のペア Pj と Pk について, 差と和が五角数になるものを考える.
差を D = |Pk - Pj| と書く. 差 D の最小値を求めよ.
'''


def create_pentagon(n):
    pn = n*(3*n - 1) // 2
    return pn


def check_pentagon(pn):
    return (1 + (1+24*pn)**0.5) % 6 == 0


def main():
    # an = P(n+1)-Pn
    # an = {4, 7, 10, 13, 16, 19, ...} となり, 初項4, 公差3の等差数列である
    # an = 4 + 3(n-1) = 3n + 1
    # D = Pk - Pj = Σ(n=j→k-1)an
    k = 1
    flg = True
    while flg:
        pk = create_pentagon(k)
        for j in xrange(1, k):
            pj = create_pentagon(j)
            if check_pentagon(pk-pj) and check_pentagon(pk+pj):
                flg = 0
                break
        k += 1
    print(pk, pj, pk-pj)


if __name__ == '__main__':
    main()
