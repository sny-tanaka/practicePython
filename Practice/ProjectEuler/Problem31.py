# coding: utf-8
'''
イギリスでは硬貨はポンド£とペンスpがあり，一般的に流通している硬貨は以下の8種類である.
1p, 2p, 5p, p10, p20, p50, £1 (p100) and £2 (p200).
以下の方法で£2を作ることが可能である．
1×£1 + 1×p50 + 2×p20 + 1×5p + 1×2p + 3×1p
これらの硬貨を使って£2を作る方法は何通りあるか?
'''


def main():
    product = 200  # 作成する数値
    i = 0
    for p200 in range(product//200+1):
        process1 = product - p200*200
        for p100 in range(process1//100+1):
            process2 = process1 - p100*100
            for p50 in range(process2//50+1):
                process3 = process2 - p50*50
                for p20 in range(process3//20+1):
                    process4 = process3 - p20*20
                    for p10 in range(process4//10+1):
                        process5 = process4 - p10*10
                        for p5 in range(process5//5+1):
                            process6 = process5 - p5*5
                            for p2 in range(process6//2+1):
                                i += 1
                                p1 = process6 - p2*2
                                print('1p:'+str(p1)+',2p:'+str(p2)+',5p:'+str(p5)+',10p:'+str(p10)+',20p:'+str(p20)+',50p:'+str(p50)+',£1:'+str(p100)+',£2:'+str(p200))
    print(i)


if __name__ == '__main__':
    main()
