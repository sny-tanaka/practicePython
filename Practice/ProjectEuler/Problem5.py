'''
2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり, そのような数字の中では最小の値である.
では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.
'''
#ユークリッド互助法による最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#1~nの最小公倍数を求める
def least_common_multiple(n):
    lcm = 1
    for i in range(2, n+1):
        lcm = lcm * i // gcd(lcm, i)
    return lcm

def main():
    lcm = least_common_multiple(20)
    print(lcm)

if __name__ == '__main__':
    main()