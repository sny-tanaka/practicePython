# coding: utf-8
'''
問題冊子は以下
https://www.su-gaku.net/common/pdf/support_sample/question/1q_q_1ji.pdf
'''
import itertools
import numpy


def main():
    # 全100caseを配列に格納
    bag = []
    # 赤球5個を袋へ
    for i in range(5):
        bag.append('r')
    # 青球3個を袋へ
    for i in range(3):
        bag.append('b')
    # 黒球2個を袋へ
    for i in range(2):
        bag.append('k')
    case = list(itertools.product(bag, repeat=2))
    xlist = []
    ylist = []
    for c in case:
        if c[0] == 'r' and c[1] == 'r':
            x = 2
        elif c[0] == 'r' or c[1] == 'r':
            x = 1
        else:
            x = 0
        xlist.append(x)
        if c[0] == 'b' and c[1] == 'b':
            y = 2
        elif c[0] == 'b' or c[1] == 'b':
            y = 1
        else:
            y = 0
        ylist.append(y)
    print(numpy.var(xlist))
    print(numpy.cov([xlist, ylist])[0][1])


if __name__ == '__main__':
    main()
