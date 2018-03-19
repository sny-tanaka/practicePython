# coding: utf-8
'''
197は巡回素数と呼ばれる. 桁を回転させたときに得られる数 197, 971, 719 が全て素数だからである.
100未満には巡回素数が13個ある: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97である.
100万未満の巡回素数はいくつあるか?
'''


def prime_numbers(n):  # 素数判定関数
    if n < 2:
        return False
    elif n == 2:
        return True
    flg = 1
    for i in range(2, n):
        if n % i == 0:
            flg = 0
            break
    if flg == 1:
        return True
    else:
        return False


def exceptjudge(n):
    s = str(n)
    exceptlist = [0, 2, 4, 5, 6, 8]
    for ex in exceptlist:
        if s.find(str(ex)) != -1:
            return False
    return True


def main():
    # 偶数は2以外素数でないので奇数のみを調べる
    num = 0
    for n in range(3, 1000000, 2):
        # nの中に偶数もしくは5が含まれている場合、循環させると必ず素数でなくなるので即除外
        if exceptjudge(n) is True:
            # 素数判定
            if prime_numbers(n) is True:
                # 桁数を調べる
                d = len(str(n)) - 1
                if d == 0:
                    num += 1
                else:
                    cir = n
                    flg = 1
                    for times in range(d):
                        cir = cir//10 + (cir % 10)*(10**d)
                        if prime_numbers(cir) is False:
                            flg = 0
                            break
                    if flg == 1:
                        num += 1
    # この処理では2と5が判定から除外されるため足す
    num += 2
    print(num)


if __name__ == '__main__':
    main()
