# coding: utf-8
'''
すべての桁に 1 から n が一度だけ使われている数をn桁の数がパンデジタル (pandigital) であるということにしよう
例えば5桁の数 15234 は1から5のパンデジタルである.
7254 は面白い性質を持っている. 39 × 186 = 7254 と書け, 掛けられる数, 掛ける数, 積が1から9のパンデジタルとなる.
掛けられる数/掛ける数/積が1から9のパンデジタルとなるような積の総和を求めよ.
HINT: いくつかの積は, 1通り以上の掛けられる数/掛ける数/積の組み合わせを持つが1回だけ数え上げよ.
'''
import itertools


def main():
    # 桁数について
    # 1桁×4桁=4桁,2桁×3桁=4桁の2パターンしか存在しないことは自明
    # パンデジタル数を上から2桁を掛けられる数,3~5桁を掛ける数,下4桁を積として成立するかを考える
    numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    panlist = list(itertools.permutations(numlist))
    for n in range(len(panlist)):
        pl = panlist[n]
        pan = 0
        for i in range(9):
            pan += pl[i]*(10**(8-i))
        panlist[n] = pan
    finlist = []
    for pan in panlist:
        # 1桁×4桁=4桁
        pro = pan % 10000
        b = (pan//10000) % 10000
        a = pan // 100000000
        if a*b == pro:
            print(a, b, pro)
            finlist.append(pro)
        # 2桁×3桁=4桁
        pro = pan % 10000
        b = (pan//10000) % 1000
        a = pan // 10000000
        if a*b == pro:
            print(a, b, pro)
            finlist.append(pro)
    finlist_uniq = list(set(finlist))
    s = 0
    for f in finlist_uniq:
        s += f
    print(s)


if __name__ == '__main__':
    main()
