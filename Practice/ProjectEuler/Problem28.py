# coding: utf-8
'''
1から初めて右方向に進み時計回りに数字を増やしていき, 5×5の螺旋が以下のように生成される:
21	22	23	24	25
20	7	8	9	10
19	6	1	2	11
18	5	4	3	12
17	16	15	14	13
両対角線上の数字の合計は101であることが確かめられる.
1001×1001の螺旋を同じ方法で生成したとき, 対角線上の数字の和はいくつか?
'''


def main():
    # n×nの外周の四隅の合計は4n^2 - 6(n-1)と表せる
    side = 1001  # 1辺の長さ
    sum_l = 1
    for n in range(3, side+1, 2):
        l = 4*n*n - 6*(n-1)
        sum_l += l
    print(sum_l)


if __name__ == '__main__':
    main()
