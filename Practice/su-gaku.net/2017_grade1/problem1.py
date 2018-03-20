# coding: utf-8
'''
問題冊子は以下
https://www.su-gaku.net/common/pdf/support_sample/question/1q_q_1ji.pdf
'''


def main():
    lst = []
    for n in range(1, 2018):
        an = 2017 // n
        lst.append(an)
    lst = list(set(lst))
    print(len(lst))


if __name__ == '__main__':
    main()
