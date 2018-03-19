# coding: utf-8
'''
5000個以上の名前が書かれている46Kのテキストファイル filenames.txt を用いる. まずアルファベット順にソートせよ.
のち, 各名前についてアルファベットに値を割り振り, リスト中の出現順の数と掛け合わせることで, 名前のスコアを計算する.
たとえば, リストがアルファベット順にソートされているとすると, COLINはリストの938番目にある.
またCOLINは 3 + 15 + 12 + 9 + 14 = 53 という値を持つ.
よってCOLINは 938 × 53 = 49714 というスコアを持つ.
ファイル中の全名前のスコアの合計を求めよ.
'''
import os


def main():
    fp = os.path.dirname(os.path.abspath(__file__))+'\\sorce\\'
    f = open(fp+'Problem22.txt', 'r')
    fn = 0
    nlst = [str(x) for x in f.readline().split()]
    nlst.sort()
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for n in range(len(nlst)):
        st = nlst[n]
        score = 0
        for i in range(len(st)):
            s = st[i:i+1]
            sco = alph.index(s) + 1
            score += sco
        score = score * (n+1)
        fn = fn + score
    print(fn)


if __name__ == '__main__':
    main()
