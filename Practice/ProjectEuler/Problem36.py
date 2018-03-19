# coding: utf-8
'''
585 = 1001001001 (2進) は10進でも2進でも回文数である.
100万未満で10進でも2進でも回文数になるような数の総和を求めよ.
(注: 先頭に0を含めて回文にすることは許されない.)
'''


def decimal_transform(n):  # 10進数を2進数に変換する
    st = bin(n)
    st = st.replace('0b', '')
    n = int(st)
    return n


def main():
    fin = 0
    for n in range(1, 1000000):
        # 10進数での回文数チェック
        s = str(n)
        r = s[::-1]
        if s == r:
            # 2進数に変換
            k = decimal_transform(n)
            s = str(k)
            r = s[::-1]
            if s == r:
                fin += n
    print(fin)


if __name__ == '__main__':
    main()
