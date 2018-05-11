# coding: utf-8
'''
常用対数を取って比較するだけ
'''

import math

def main():
    maxVal = 0
    maxRow = 0
    row = 1
    f = open('Problem67.txt')
    line = f.readline()[:-1]
    while line:
        x, y = [int(i) for i in line.split(',')]
        nowVal = y*(math.log10(x))
        if maxVal < nowVal:
            maxVal = nowVal
            maxRow = row
        row += 1
        line = f.readline()[:-1]
    print(maxRow)

if __name__ == '__main__':
    main()
