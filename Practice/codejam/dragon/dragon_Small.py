# -*- coding: utf-8 -*-

'''
行動優先度
デバフ>バフ>攻撃（回復はできるだけ使わない）

処理順
最小攻撃ターン数の決定（バフをかけるかどうか）
※攻撃ターン数＜防御ターン数であることの確認
無理ならデバフをかけるか回復をするかで防御ターン数を延ばす
再度※の判定処理
'''

def buffjudge(Hk, Ad, B):
    #バフをi回かけたときの行動ターン数
    i = 0 #初期化
    n = 1
    m = 0
    while n > m:
        m = n
        n = Hk // (Ad + B * i) + i + 1
        i = i + 1
    return n

def debuffjudge(Hd, Ak, D, n):
    #n-1ターンの間に自分が受けるダメージを計算
    dmg = (n - 1) * Ak
    if dmg < Hd: #防御行動なしで倒せる
        return n
    else: #デバフか回復を入れないと死ぬ
        i = 0
        while dmg >= Hd:
            i = i + 1
            dmg = (n + i - 1) * Ak + (i - 1) * i / 2

        

        

    
def main():
    
