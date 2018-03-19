# coding: utf-8
'''
完全数とは, その数の真の約数の和がそれ自身と一致する数のことである.
たとえば, 28の真の約数の和は, 1 + 2 + 4 + 7 + 14 = 28 であるので, 28は完全数である.
真の約数の和がその数よりも少ないものを不足数といい, 真の約数の和がその数よりも大きいものを過剰数と呼ぶ.
12は, 1 + 2 + 3 + 4 + 6 = 16 となるので, 最小の過剰数である. よって2つの過剰数の和で書ける最少の数は24である.
数学的な解析により, 28123より大きい任意の整数は2つの過剰数の和で書けることが知られている.
2つの過剰数の和で表せない最大の数がこの上限よりも小さいことは分かっているのだが, この上限を減らすことが出来ていない.
2つの過剰数の和で書き表せない正の整数の総和を求めよ.
'''
import itertools


def divide(n):  # 真の約数の合計を返す
    div = 0
    for i in range(1, n):
        if n % i == 0:
            div += i
    return div


def main():
    # 過剰数を配列に格納
    abun = []
    for i in range(2, 20162):
        div = divide(i)
        if i < div:
            abun.append(i)
    sum_abun = {n + m for m in abun for n in abun if n + m <= 20161}
    not_abun = set(xrange(1, 20162)).difference(sum_abun)
    print(sum(list(not_abun)))


if __name__ == '__main__':
    main()
