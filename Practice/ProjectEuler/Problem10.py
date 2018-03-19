# coding: utf-8
'''
10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.
200万以下の全ての素数の和を求めよ.
'''
from tqdm import tqdm


def prime_numbers(n, plist):  # 素数判定関数
    # 以下の素数は初期値として既に判明済として高速化を図る
    # plist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # 入力された数未満の判定済素数で割り切れなければ素数と判定
    flg = 1
    for i in plist:
        if n % i == 0:
            flg = 0
            break
    if flg == 1:
        return True
    else:
        return False


def main():
    plist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # 偶数は素数じゃないので判定外とする
    for i in tqdm(range(31, 2000000, 2)):
        if prime_numbers(i, plist) is True:
            plist.append(i)
    s = 0
    for i in plist:
        s += i
    print(s)


if __name__ == '__main__':
    main()
