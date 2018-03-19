'''
13195 の素因数は 5, 7, 13, 29 である.
600851475143 の素因数のうち最大のものを求めよ.
'''
def main():
    #2から順番に割っていく
    d = 600851475143
    flg = 1
    while flg ==1:
        i = 2
        while True:
            if d % i == 0:
                if d == i:
                    print(i)
                    flg = 0
                    break
                else:
                    d = d // i
                    break
            i += 1       

if __name__ == '__main__':
    main()