# coding: utf-8
'''
2×2 のマス目の左上からスタートした場合, 引き返しなしで右下にいくルートは 6 つある.
では, 20×20 のマス目ではいくつのルートがあるか.
'''


def main():
    # 40C20を計算する

    # 21~40の掛け算
    a = 1
    for i in range(21, 41):
        a = a * i

    # 1~20の掛け算
    b = 1
    for i in range(1, 21):
        b = b * i

    n = a // b
    print(n)


if __name__ == '__main__':
    main()
