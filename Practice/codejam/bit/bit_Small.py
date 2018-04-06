# coding: utf-8
import os

def sum_position(n):
    s = 0
    while n > 0:
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
    f = open(fp+'C-small-practice.in', 'r')
    T = int(f.readline()[:-1])
    for i in range(T):
        N = int(f.readline()[:-1])
        nlist = []
        for j in range(0,N//2+1):
            a = j
            b = N - a
            a = decimal_transform(a)
            b = decimal_transform(b)
            a = sum_position(a)
            b = sum_position(b)
            s = a + b
            nlist.append(s)
        max_number = max(nlist)
        print("Case #" + str(i + 1) + ": " + str(max_number))
    print("終了")

if __name__ == '__main__':
    main()