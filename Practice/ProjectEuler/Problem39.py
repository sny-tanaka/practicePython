# coding: utf-8
'''
辺の長さが {a,b,c} と整数の3つ組である直角三角形を考え, その周囲の長さを p とする.
p = 120のときには3つの解が存在する:
{20,48,52}, {24,45,51}, {30,40,50}
p ≤ 1000 のとき解の数が最大になる p はいくつか?
'''


def main():
    max_i = 0
    max_p = 0
    for p in range(12, 1001):
        i = 0
        for a in range(1, (p-3)//3):
            if (2*p*a-p*p) % (2*a-2*p) == 0:
                b = (2*p*a-p*p) // (2*a-2*p)
                if a <= b:
                    c = p - a - b
                    print(p, a, b, c)
                    i += 1
        if max_i < i:
            max_i = i
            max_p = p
    print(max_p)


if __name__ == '__main__':
    main()
