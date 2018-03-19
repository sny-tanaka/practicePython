# coding: utf-8
'''
Problem18の拡張
'''
import os


def main():
    # 三角形を二次元配列にする
    tri = []
    fp = os.path.dirname(os.path.abspath(__file__))+'\\sorce\\'
    f = open(fp+'Problem67.txt', 'r')
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
