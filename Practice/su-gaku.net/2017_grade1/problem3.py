# coding: utf-8
'''
問題冊子は以下
https://www.su-gaku.net/common/pdf/support_sample/question/1q_q_1ji.pdf
'''
import numpy


def main():
    a = numpy.array([2, 1, -3])
    b = numpy.array([0, -2, 3])
    c = numpy.array([1, -3, 5])
    bc = numpy.cross(b, c)
    abc = numpy.cross(a, bc)
    print(abc)


if __name__ == '__main__':
    main()
