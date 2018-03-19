# coding: utf-8
'''
3797は面白い性質を持っている.
まずそれ自身が素数であり, 左から右に桁を除いたときに全て素数になっている (3797, 797, 97, 7).
同様に右から左に桁を除いたときも全て素数である (3797, 379, 37, 3).
右から切り詰めても左から切り詰めても素数になるような素数は11個しかない. 総和を求めよ.
注: 2, 3, 5, 7を切り詰め可能な素数とは考えない.
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
    k = 0
    n = 11
    fin = 0
    while k != 11:
        # 右から桁を消していく
        m = n
        flg = 1
        while m > 0:
            if prime_numbers(m) is False:
                flg = 0
                break
            m = m // 10
        if flg == 1:
            # 左から桁を消していく
            s = str(n)
            for i in range(len(s)):
                st = s[i:]
                m = int(st)
                if prime_numbers(m) is False:
                    flg = 0
                    break
            if flg == 1:
                print(n)
                fin += n
                k += 1
        n += 1
    print(fin)


if __name__ == '__main__':
    main()
