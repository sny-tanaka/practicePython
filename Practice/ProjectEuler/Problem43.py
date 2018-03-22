# coding: utf-8
'''
数1406357289は0から9のパンデジタル数である (0から9が1度ずつ現れるので).
この数は部分文字列が面白い性質を持っている.
d1を上位1桁目, d2を上位2桁目の数とし, 以下順にdnを定義する. この記法を用いると次のことが分かる.
d2d3d4=406 は 2 で割り切れる
d3d4d5=063 は 3 で割り切れる
d4d5d6=635 は 5 で割り切れる
d5d6d7=357 は 7 で割り切れる
d6d7d8=572 は 11 で割り切れる
d7d8d9=728 は 13 で割り切れる
d8d9d10=289 は 17 で割り切れる
このような性質をもつ0から9のパンデジタル数の総和を求めよ.
'''
import itertools


def pandegital_special(s):
    if int(s[1:4]) % 2 != 0:
        return False
    if int(s[2:5]) % 3 != 0:
        return False
    if int(s[3:6]) % 5 != 0:
        return False
    if int(s[4:7]) % 7 != 0:
        return False
    if int(s[5:8]) % 11 != 0:
        return False
    if int(s[6:9]) % 13 != 0:
        return False
    if int(s[7:10]) % 17 != 0:
        return False
    return True


def main():
    numlist = []
    for n in range(10):
        numlist.append(n)
    panlist = itertools.permutations(numlist)
    ans = 0
    for pan in panlist:
        if pan[0] != 0:
            strings = ''
            for i in range(10):
                strings += str(pan[i])
            if pandegital_special(strings) is True:
                ans += int(strings)
    print(ans)


if __name__ == '__main__':
    main()
