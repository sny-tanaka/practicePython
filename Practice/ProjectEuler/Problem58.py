# coding: utf-8
'''
螺旋状に並べた数字の対角線上の素数の割合が10%未満になる最初の辺の長さ

解法の要点
・辺の長さは1,3,5...と奇数ずつ増える
    ⇒n番目の辺の長さは、2n-1
・分母の初項は1、1周増えると分母となる数字は4ずつ増える
    ⇒n番目の分母は、4n-3
・右下の数字は必ず奇平方数であるため素数ではない
・n番目の右上の数字は、4n^2-10n+7
・n番目の左上の数字は、4n^2-8n+5
・n番目の左下の数字は、4n^2-6n+3
'''

import random

def is_prime(q):
    k = 50
    #計算するまでもなく判定できるものははじく
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    #n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1
    
    #判定をk回繰り返す
    for i in range(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        #[0,s-1]の範囲すべてをチェック
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True


def right_up_number(n):
    return 4*(n**2) - 10*n + 7

def left_up_number(n):
    return 4*(n**2) - 8*n + 5

def left_down_number(n):
    return 4*(n**2) - 6*n + 3


def main():
    n = 1
    plist = [0]
    p = 1.00
    while p >= 0.1:
        n += 1

        plist.append(0)

        if is_prime(right_up_number(n)):
            plist.append(1)
        else:
            plist.append(0)
        
        if is_prime(left_up_number(n)):
            plist.append(1)
        else:
            plist.append(0)
        
        if is_prime(left_down_number(n)):
            plist.append(1)
        else:
            plist.append(0)
        
        p = sum(plist) / len(plist)
        print(n, p)
        
    print(2*n - 1)


if __name__ == '__main__':
    main()
