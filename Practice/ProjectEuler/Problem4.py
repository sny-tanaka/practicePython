'''
左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
では, 3桁の数の積で表される回文数の最大値を求めよ.
'''
#反転した数値を返す関数
def palindrome(n):
    rev = 0
    while n > 0:
        rem = n % 10
        n = n // 10
        rev = rev * 10 + rem
    return rev

def main():
    #100×100から999×999までを配列に入れる
    lst = []
    for x in range(100, 1000):
        for y in range(100, 1000):
            lst.append(x*y)

    #配列を降順にソート
    lst.sort(reverse=True)

    #配列内の数値を順番に調べて初めて回文数だった値が最大値
    for i in range(len(lst)):
        if lst[i] == palindrome(lst[i]):
            print(lst[i])
            break

if __name__ == '__main__':
    main()