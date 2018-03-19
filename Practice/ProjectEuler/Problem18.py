# coding: utf-8
'''
以下の三角形の頂点から下まで移動するとき, その数値の和の最大値は23になる.

3
7 4
2 4 6
8 5 9 3
この例では 3 + 7 + 4 + 9 = 23.

以下の三角形を頂点から下まで移動するとき, その最大の和を求めよ.

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
import os


def main():
    # 三角形を二次元配列にする
    tri = []
    fp = os.path.dirname(os.path.abspath(__file__))+'\\sorce\\'
    f = open(fp+'Problem18.txt', 'r')
    for line in f:
        tri.append([int(x) for x in line[:-1].split()])
    # そこまでの合計の最大値で値を更新
    for i in range(1, len(tri)):
        n = len(tri[i])
        for j in range(n):
            if j == 0:
                tri[i][j] = tri[i-1][j] + tri[i][j]
            elif j == n-1:
                tri[i][j] = tri[i-1][j-1] + tri[i][j]
            else:
                if tri[i-1][j-1] > tri[i-1][j]:
                    tri[i][j] = tri[i-1][j-1] + tri[i][j]
                else:
                    tri[i][j] = tri[i-1][j] + tri[i][j]
    print(max(tri[i]))


if __name__ == '__main__':
    main()
