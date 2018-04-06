# coding: utf-8
import os

def sum_position(n, p):
    s = 0
    for i in range(p):
        s = s + n % 10
        n = n // 10
    return s

def decimal_transform(n):
    st = bin(n)
    st = st.replace('0b', '')
    n = int(st)
    return n

def main():
    fp = os.path.dirname(os.path.abspath(__file__))+'\\'
    f = open(fp+'A-small-practice.in', 'r')
    T = int(f.readline()[:-1])
    for i in range(T):
        N, K = [int(x) for x in f.readline()[:-1].split()]
        K = decimal_transform(K)
        s = sum_position(K, N)
        if N == s:
            switch = 'ON'
        else:
            switch = 'OFF' 
        print("Case #" + str(i + 1) + ": " + str(switch))
    print("終了")

if __name__ == '__main__':
    main()