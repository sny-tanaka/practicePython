# coding: utf-8
'''
1 から 5 までの数字を英単語で書けば one, two, three, four, five であり, 全部で 3 + 3 + 5 + 4 + 4 = 19 の文字が使われている.
では 1 から 1000 (one thousand) までの数字をすべて英単語で書けば, 全部で何文字になるか.
'''


def num2str(n):  #数字を英単語に変換
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tys = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    hund = 'hundred'

    a = ''
    b = ''
    c = ''

    u = n % 10  # 1の位
    a = units[u]
    n = n // 10
    if n > 0:
        t = n % 10  # 10の位
        if t == 1:
            a = ''
            b = teens[u]
        else:
            b = tys[t]
        n = n // 10
        if n > 0:
            h = n % 10  # 100の位
            if a == '' and b == '':
                c = units[h] + hund
            else:
                c = units[h] + hund + 'and'
    return c + b + a


def main():
    s = 0
    for i in range(1, 1000):
        n = num2str(i)
        s += len(n)
    s += 11
    print(s)


if __name__ == '__main__':
    main()
