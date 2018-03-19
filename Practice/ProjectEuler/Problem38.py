# coding: utf-8
'''
192 に 1, 2, 3 を掛けてみよう.
192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
積を連結することで1から9の パンデジタル数 192384576 が得られる.
192384576 を 192 と (1,2,3) の連結積と呼ぶ.
同じようにして, 9 を 1,2,3,4,5 と掛け連結することでパンデジタル数 918273645 が得られる.
これは 9 と (1,2,3,4,5) との連結積である.
整数と (1,2,...,n) (n > 1) との連結積として得られる9桁のパンデジタル数の中で最大のものはいくつか?
'''


def main():
    max_pan = 0
    for i in range(1, 10000):
        n = 1
        strings = ''
        while len(strings) < 9:
            strings += str(i*n)
            n += 1
        if n != 2 and len(strings) == 9 and strings.find('0') == -1:
            strings_list = list(strings)
            # 重複する数字を削除
            strings_list = list(set(strings_list))
            # 配列に9個残っていればパンデジタル数と判定
            if len(strings_list) == 9:
                pan = int(strings)
                if max_pan < pan:
                    max_pan = pan
    print(max_pan)


if __name__ == '__main__':
    main()
