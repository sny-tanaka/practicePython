# coding: utf-8

import pygame
from pygame.locals import *
import sys
import random


def create_puyo():
    # 新規ぷよを作成する
    puyolist = ['None', 'red', 'blue', 'green', 'yellow', 'purple']
    puyo1 = puyolist[random.randint(1, 5)]
    puyo2 = puyolist[random.randint(1, 5)]
    return puyo1, puyo2


def main():
    pygame.init()  # 初期化
    screen = pygame.display.set_mode((400, 565))  # ウィンドウサイズの指定
    pygame.display.set_caption('ぷよぷよ')  # タイトルバー
    bg = pygame.image.load('images\\bg.png').convert_alpha()
    rect_bg = bg.get_rect()
    flame = pygame.image.load('images\\flame.png').convert_alpha()
    rect_flame = flame.get_rect()
    rect_flame.center = (160, 280)
    subflame = pygame.image.load('images\\subflame.png').convert_alpha()
    rect_subflame = subflame.get_rect()
    rect_subflame.center = (360, 120)
    push_enter = pygame.image.load('images\\enter.png').convert_alpha()
    rect_push_enter = push_enter.get_rect()
    rect_push_enter.center = (200, 280)

    # ぷよをストックに２つ作成
    puyo1, puyo2 = create_puyo()
    stock1_puyo1 = pygame.image.load('images\\'+puyo1+'.png').convert_alpha()
    stock1_puyo1_color = puyo1
    rect_stock1_puyo1 = stock1_puyo1.get_rect()
    rect_stock1_puyo1.center = (360, 55)
    stock1_puyo2 = pygame.image.load('images\\'+puyo2+'.png').convert_alpha()
    stock1_puyo2_color = puyo2
    rect_stock1_puyo2 = stock1_puyo2.get_rect()
    rect_stock1_puyo2.center = (360, 95)
    puyo1, puyo2 = create_puyo()
    stock2_puyo1 = pygame.image.load('images\\'+puyo1+'.png').convert_alpha()
    stock2_puyo1_color = puyo1
    rect_stock2_puyo1 = stock2_puyo1.get_rect()
    rect_stock2_puyo1.center = (360, 145)
    stock2_puyo2 = pygame.image.load('images\\'+puyo2+'.png').convert_alpha()
    stock2_puyo2_color = puyo2
    rect_stock2_puyo2 = stock2_puyo2.get_rect()
    rect_stock2_puyo2.center = (360, 185)

    game_start_flg = False
    puyo_drop_flg = False
    underground = [480, 480, 480, 480, 480, 480]
    puyo_stack =[]
    for i in range(12):
        puyo_stack.append(['None', 'None', 'None', 'None', 'None', 'None'])

    while(True):
        # ぷよの落下速度
        pygame.time.Clock().tick(60)

        # 各列の一番下の判定
        for c in range(6):
            for r in range(12):
                if puyo_stack[r][c] == 'None':
                    underground[c] = 480 + 40*r
                    break

        screen.blit(bg, rect_bg)
        screen.blit(flame, rect_flame)
        screen.blit(subflame, rect_subflame)
        screen.blit(stock1_puyo1, rect_stock1_puyo1)
        screen.blit(stock1_puyo2, rect_stock1_puyo2)
        screen.blit(stock2_puyo1, rect_stock2_puyo1)
        screen.blit(stock2_puyo2, rect_stock2_puyo2)

        if game_start_flg:
            if puyo_drop_flg is False:
                # 落ちぷよをストックから出す
                drop_puyo1 = stock1_puyo1
                drop_puyo1_color = stock1_puyo1_color
                rect_drop_puyo1 = drop_puyo1.get_rect()
                drop_puyo2 = stock1_puyo2
                drop_puyo2_color = stock1_puyo2_color
                rect_drop_puyo2 = drop_puyo2.get_rect()
                x1, y1 = 115, 20
                x2, y2 = x1, y1+40

                # ストック2をストック1へ移動
                stock1_puyo1 = stock2_puyo1
                stock1_puyo1_color = stock2_puyo1_color
                rect_stock1_puyo1 = rect_stock2_puyo1
                rect_stock1_puyo1.center = (360, 55)
                stock1_puyo2 = stock2_puyo2
                stock1_puyo2_color = stock2_puyo2_color
                rect_stock1_puyo2 = rect_stock2_puyo2
                rect_stock1_puyo2.center = (360, 95)

                # ストック2を新たに作成
                puyo1, puyo2 = create_puyo()
                stock2_puyo1 = pygame.image.load('images\\'+puyo1+'.png').convert_alpha()
                stock2_puyo1_color = puyo1
                rect_stock2_puyo1 = stock2_puyo1.get_rect()
                rect_stock2_puyo1.center = (360, 145)
                stock2_puyo2 = pygame.image.load('images\\'+puyo2+'.png').convert_alpha()
                stock2_puyo2_color = puyo2
                rect_stock2_puyo2 = stock2_puyo2.get_rect()
                rect_stock2_puyo2.center = (360, 185)

                # 落ちぷよ中の判定へ
                puyo_drop_flg = True
            else:
                # 落ちぷよを表示
                rect_drop_puyo1.topleft = (x1, y1)
                rect_drop_puyo2.topleft = (x2, y2)
                screen.blit(drop_puyo1, rect_drop_puyo1)
                screen.blit(drop_puyo2, rect_drop_puyo2)

                # 落ちぷよを下へ移動
                if y1 != underground[(x1-25)//45] and y2 != underground[(x2-25)//45]:
                    y1 += 1
                    y2 += 1
                else:
                    puyo_drop_flg = False
        else:
            screen.blit(push_enter, rect_push_enter)
        
        # ぷよを置く
        if game_start_flg and puyo_drop_flg is False:
            if y1 > y2:
                for r in range(12):
                    if puyo_stack[r][(x1-25)//45] == 'None':
                        to_y1 = 480 - r*40
                        puyo_stack[r][(x1-25)//45] = drop_puyo1_color
                        break
                for r in range(12):
                    if puyo_stack[r][(x2-25)//45] == 'None':
                        to_y2 = 480 - r*40
                        puyo_stack[r][(x1-25)//45] = drop_puyo2_color
                        break
            else:
                for r in range(12):
                    if puyo_stack[r][(x2-25)//45] == 'None':
                        to_y2 = 480 - r*40
                        puyo_stack[r][(x1-25)//45] = drop_puyo2_color
                        break
                for r in range(12):
                    if puyo_stack[r][(x1-25)//45] == 'None':
                        to_y1 = 480 - r*40
                        puyo_stack[r][(x1-25)//45] = drop_puyo1_color
                        break
            while y1 != to_y1 or y2 != to_y2:
                if y1 != to_y1:
                    y1 += 1
                if y2 != to_y2:
                    y2 += 1
                pygame.display.update()
        
        # スタックぷよの表示
        if game_start_flg:
            for c in range(6):
                for r in range(12):
                    rect_drop_puyo1.topleft = (x1, y1)
                    stack = pygame.image.load('images\\'+puyo_stack[r][c]+'.png').convert_alpha()
                    rect_stack = stack.get_rect()
                    rect_stack.topleft = (25+c*45, 480-r*40)
                    screen.blit(stack, rect_stack)
        
        # ぷよが消える判定
        #if game_start_flg and puyo_drop_flg is False:
            

        pygame.display.update()  # 画面更新

        for event in pygame.event.get():  # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    game_start_flg = True
                if puyo_drop_flg:
                    if event.key == K_SPACE:
                        # ぷよの回転
                        if y2 - y1 == 40 and x1 != 25:  # 下にある場合左へ
                            y2 = y1
                            x2 = x1-45
                        elif x1 - x2 == 45:  # 左にある場合上へ
                            x2 = x1
                            y2 = y1-40
                        elif y1 - y2 == 40 and x1 != 250:  # 上にある場合右へ
                            y2 = y1
                            x2 = x1+45
                        elif x2 - x1 == 45 and y1 < underground[(x1-25)//45]-40:  # 右にある場合下へ
                            x2 = x1
                            y2 = y1+40
                    if event.key == K_LEFT:
                        # ぷよを1マス左へ移動
                        if x1 != 25 and x2 != 25:
                            x1 -= 45
                            x2 -= 45
                    if event.key == K_RIGHT:
                        # ぷよを1マス右へ移動
                        if x1 != 250 and x2 != 250:
                            x1 += 45
                            x2 += 45


if __name__ == '__main__':
    main()
