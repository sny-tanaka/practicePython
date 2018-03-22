# coding: utf-8
'''
三角数のn項は tn = ½n(n+1)で与えられる. 最初の10項は
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
である.
単語中のアルファベットを数値に変換した後に和をとる. この和を「単語の値」と呼ぶことにする.
例えば SKY は 19 + 11 + 25 = 55 = t10である. 単語の値が三角数であるとき, その単語を三角語と呼ぶ.
テキストファイル Problem42.txt 中に約2000語の英単語が記されている. 三角語はいくつあるか?
'''
import os
import numpy


def triangle(n):
    n = 2 * n
    x = int(numpy.sqrt(n))
    return x*(x+1) == n


def main():
    fp = os.path.dirname(os.path.abspath(__file__))+'\\sorce\\'
    f = open(fp+'Problem42.txt', 'r')
    nlst = [str(x) for x in f.readline().split()]
    nlst.sort()
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ans = 0
    for n in range(len(nlst)):
        st = nlst[n]
        score = 0
        for i in range(len(st)):
            s = st[i:i+1]
            sco = alph.index(s) + 1
            score += sco
        if triangle(score) is True:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
