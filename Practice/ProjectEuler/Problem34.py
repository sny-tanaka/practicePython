# coding: utf-8
'''
145は面白い数である. 1! + 4! + 5! = 1 + 24 + 120 = 145となる.
各桁の数の階乗の和が自分自身と一致するような数の和を求めよ.
注: 1! = 1 と 2! = 2 は総和に含めてはならない.
'''


def main():
    fact = []
    for n in range(10):
        if n == 0:  # 数学の定義上0!=1
            fact.append(1)
        else:
            s = 1
            for i in range(1, n+1):
                s = s * i
            fact.append(s)
    fin = 0
    for i in range(3, fact[9]*7):
        k = i
        s = 0
        while k > 0:
            r = k % 10
            k = k // 10
            s += fact[r]
        if s == i:
            fin += i
            print(i)
    print(fin)


if __name__ == '__main__':
    main()
