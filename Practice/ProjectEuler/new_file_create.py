# coding: utf-8
'''
Problem0を元にProblem[n]を作成する
'''
import shutil
import os


def main():
    flg = 0
    i = 0
    while flg == 0:
        i += 1
        filename = 'Problem' + str(i) + '.py'
        if os.path.exists(filename) is False:
            flg = 1
    shutil.copyfile('Problem0.py', filename)


if __name__ == '__main__':
    main()
