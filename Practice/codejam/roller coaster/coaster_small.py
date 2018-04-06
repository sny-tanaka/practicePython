# coding: utf-8
import os

def main():
    fp = os.path.dirname(os.path.abspath(__file__))+'\\'
    f = open(fp+'C-small-practice.in', 'r')
    T = int(f.readline()[:-1])
    for i in range(T):
        R, K, N = [int(x) for x in f.readline()[:-1].split()]
        glist = []
        glist = map(int, f.readline()[:-1].split())
        sale = 0
        for times in range(R):
            ride_num = 0
            for j in range(N):
                ride_num = ride_num + glist[0]
                if ride_num > K:
                    ride_num = ride_num - glist[0]
                    break
                else:
                    a = glist[0]
                    del glist[0]
                    glist.append(a)
            sale = sale + ride_num
        print("Case #" + str(i + 1) + ": " + str(sale))
    print("終了")

if __name__ == '__main__':
    main()