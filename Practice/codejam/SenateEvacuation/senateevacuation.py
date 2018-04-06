# coding: utf-8

'''
最後は必ず1,1のペアを残しておくこと
最大数の同数ペアが1組あればどこを脱出させようが過半数にはならないこと
以上に着目してやれば以下の分岐で処理可能。
'''
import os
import sys

@profile
def main():
    fp = os.path.dirname(os.path.abspath(__file__))+'\\'
    f = open(fp+'sample.txt', 'r')
    sys.stdout = open(fp+'output.txt', 'w')
    T = int(f.readline()[:-1])
    for i in range(T):
        sys.stdout.write("Case #"+str(i+1)+": ")
        N = int(f.readline()[:-1])
        lst = map(int, f.readline()[:-1].split())
        sums = sum(lst)
        while sums != 0:
            for j in range(2):
                if len(lst)-lst.count(0) != lst.count(max(lst)):
                    esc = lst.index(max(lst))
                    lst[esc] -= 1
                    sys.stdout.write(chr(esc+65))
                elif j == 1 and lst.count(max(lst)) % 2 == 0:
                    break
                else:
                    for n in range(N):
                        if lst[n] > 0:
                            lst[n] -= 1
                            sys.stdout.write(chr(n+65))
                            break
                sums = sum(lst)
                if sums == 0:
                    break
            sys.stdout.write(" ")
        print("")


if __name__ == '__main__':
    main()
