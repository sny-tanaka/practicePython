# coding: utf-8

import os

#ユークリッド互助法による最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#配列Mの最小公倍数を求める
def least_common_multiple(M):
    lcm = 1
    for i in range(len(M)):
        num = M[i]
        lcm = lcm * num // gcd(lcm, num)
    return lcm

#最小公倍数までに何人の客を捌けるか
def cycle(M):
    lcm = least_common_multiple(M)
    cnt = 0
    for i in range(len(M)):
        cnt += lcm // M[i]
    return cnt

def main():
    fp = os.path.dirname(os.path.abspath(__file__))+'\\'
    f = open(fp+'B-small-practice.in', 'r')
    T = int(f.readline()[:-1])
    for i in range(T):
        B, N = [int(x) for x in f.readline()[:-1].split()]
        M = [int(x) for x in f.readline()[:-1].split()]
        cnt = cycle(M)
        N = N % cnt
        if N == 0:
            N = cnt
        if B >= N:
            k = N
        else:
            N = N - B
            tl = list(M)
            j = 0
            while j != N:
                #一番早く施術が終わる理髪師
                mini = min(tl)
                #すべてのタイムラインをminiだけ進める
                for time in range(len(tl)):
                    rem = tl[time] - mini
                    #0になったら施術終了なので列を1進めてタイムラインを初期値に戻す
                    if rem == 0:
                        tl[time] = M[time]
                        j += 1
                        if j == N:
                            k = time + 1
                            break
                    else:
                        tl[time] = rem
        print("Case #" + str(i + 1) + ": " + str(k))
    print("終了")

if __name__ == '__main__':
    main()