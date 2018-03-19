'''
ピタゴラス数(ピタゴラスの定理を満たす自然数)とは a < b < c で以下の式を満たす数の組である.
a^2 + b^2 = c^2
例えば, 3^2 + 4^2 = 9 + 16 = 25 = 5^2 である.
a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
これらの積 abc を計算しなさい.
'''

def main():
    flg = 1
    for a in range(1, 333):
        A = a * a
        for b in range(a+1, (1000-a)//2):
            B = b * b
            c = 1000 - a - b
            C = c * c
            if A + B == C:
                print(a)
                print(b)
                print(c)
                print(a*b*c)
                flg = 0
                break
        if flg == 0:
            break

if __name__ == '__main__':
    main()