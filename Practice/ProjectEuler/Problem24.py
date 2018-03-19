# coding: utf-8
'''
順列とはモノの順番付きの並びのことである. たとえば, 3124は数 1, 2, 3, 4 の一つの順列である.
すべての順列を数の大小でまたは辞書式に並べたものを辞書順と呼ぶ. 0と1と2の順列を辞書順に並べると
012 021 102 120 201 210
になる.
0,1,2,3,4,5,6,7,8,9からなる順列を辞書式に並べたときの100万番目はいくつか?
'''
import itertools


def main():
    nlist = []
    for i in range(10):
        nlist.append(str(i))
    plist = list(itertools.permutations(nlist))
    slist = []
    for i in range(len(plist)):
        strings = ''
        for j in range(10):
            strings += plist[i][j]
        slist.append(strings)
    slist.sort()
    n = 1000000  # 調べたい項番
    print(slist[n-1])


if __name__ == '__main__':
    main()
