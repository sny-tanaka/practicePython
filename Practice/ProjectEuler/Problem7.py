'''
素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.
10001 番目の素数を求めよ.
'''
#素数判定関数
def prime_numbers(n):
    flg = 1
    m = n
    while flg ==1:
        i = 2
        while True:
            if n % i == 0:
                if n == i:
                    flg = 0
                    break
                else:
                    n = n // i
                    break
            i += 1
    if m == i:
        return True
    else:
        return False

def main():
    i = 1
    n = 1
    while i <= 10001:
        n += 1
        if prime_numbers(n) == True:
            i += 1
    print(n)

if __name__ == '__main__':
    main()