'''
最初の10個の自然数について, その二乗の和は,
1^2 + 2^2 + ... + 10^2 = 385
最初の10個の自然数について, その和の二乗は,
(1 + 2 + ... + 10)^2 = 3025
これらの数の差は 3025 - 385 = 2640 となる.
同様にして, 最初の100個の自然数について二乗の和と和の二乗の差を求めよ.
'''
#二乗の和
def sum_of_square(n):
    s = 0
    for i in range(1, n+1):
        s += i * i
    return s
    
#和の二乗
def square_of_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    s = s * s
    return s
    
def main():
    n = 100
    d = square_of_sum(n) - sum_of_square(n)
    print(d)

if __name__ == '__main__':
    main()