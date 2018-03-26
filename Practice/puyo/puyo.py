# coding: utf-8

import pygame
from pygame.locals import *
import sys
import random
import os


def load_image(imgname, fp):
    filename = fp + '\\images\\' + imgname + '.png'
    img_object = pygame.image.load(filename).convert_alpha()
    rect_img_object = img_object.get_rect()
    return img_object, rect_img_object


def create_puyo():
    # 新規ぷよを作成する
    puyolist = ['None', 'red', 'blue', 'green', 'yellow', 'purple']
    puyo1 = puyolist[random.randint(1, 5)]
    puyo2 = puyolist[random.randint(1, 5)]
    return puyo1, puyo2


def check_connection(puyo_stack, x, y, n, check_flg):
    color = puyo_stack[y][x]
    vec = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    check_flg[y][x] = True
    for v in vec:
        if x+v[0] >= 0 and x+v[0] < 6:
            if y+v[1] >= 0 and y+v[1] < 12:
                if check_flg[y+v[1]][x+v[0]] is False:
                    if puyo_stack[y+v[1]][x+v[0]] == color:
                        n += 1
                        n, check_flg = check_connection(puyo_stack, x+v[0], y+v[1], n, check_flg)
    return n, check_flg


def erase_puyo(puyo_stack, x, y, n, check_flg, erase_flg):
    n, check_flg = check_connection(puyo_stack, x, y, n, check_flg)
    if n >= 4:
        erase_flg = True
        for r in range(12):
            for c in range(6):
                if check_flg[r][c]:
                    puyo_stack[r][c] = 'bomb'
    return puyo_stack, erase_flg


def bomb2none(puyo_stack):
    for r in range(12):
        for c in range(6):
            if puyo_stack[r][c] == 'bomb':
                puyo_stack[r][c] = 'None'
    return puyo_stack


def drop_all(puyo_stack):
    for c in range(6):
        for r in range(12):
            if puyo_stack[r][c] == 'None':
                for x in range(r+1, 12):
                    if puyo_stack[x][c] != 'None':
                        puyo_stack[r][c] = puyo_stack[x][c]
                        puyo_stack[x][c] = 'None'
                        break
    return puyo_stack


def stack_display(puyo_stack, fp, screen):
    rect_list = []
    for c in range(6):
        for r in range(12):
            filename = fp + '\\images\\'+puyo_stack[r][c]+'.png'
            stack = pygame.image.load(filename).convert_alpha()
            rect_stack = stack.get_rect()
            rect_stack.topleft = (25+c*45, 480-r*40)
            screen.blit(stack, rect_stack)
            rect_list.append(rect_stack)
    pygame.display.update(rect_list)


def main():
    fp = os.path.abspath(os.path.dirname(sys.argv[0]))
    pygame.init()  # 初期化
    screen = pygame.display.set_mode((400, 565))  # ウィンドウサイズの指定
    pygame.display.set_caption('ぷよぷよ')  # タイトルバー
    bg, rect_bg = load_image('bg', fp)
    flame, rect_flame = load_image('flame', fp)
    rect_flame.center = (160, 280)
    subflame, rect_subflame = load_image('subflame', fp)
    rect_subflame.center = (360, 120)
    batsu, rect_batsu = load_image('batsu', fp)
    rect_batsu.topleft = (115, 40)
    batsu2, rect_batsu2 = load_image('batsu', fp)
    rect_batsu2.topleft = (160, 40)
    push_enter, rect_push_enter = load_image('enter', fp)
    rect_push_enter.center = (200, 280)
    gameover, rect_gameover = load_image('over', fp)
    rect_gameover.center = (200, 280)

    # ぷよをストックに２つ作成
    puyo1, puyo2 = create_puyo()
    stock1_puyo1, rect_stock1_puyo1 = load_image(puyo1, fp)
    stock1_puyo1_color = puyo1
    rect_stock1_puyo1.center = (360, 55)
    stock1_puyo2, rect_stock1_puyo2 = load_image(puyo2, fp)
    stock1_puyo2_color = puyo2
    rect_stock1_puyo2.center = (360, 95)
    puyo1, puyo2 = create_puyo()
    stock2_puyo1, rect_stock2_puyo1 = load_image(puyo1, fp)
    stock2_puyo1_color = puyo1
    rect_stock2_puyo1.center = (360, 145)
    stock2_puyo2, rect_stock2_puyo2 = load_image(puyo2, fp)
    stock2_puyo2_color = puyo2
    rect_stock2_puyo2.center = (360, 185)

    game_start_flg = False
    game_over_flg = False
    puyo_drop_flg = False
    ug = [480, 480, 480, 480, 480, 480]
    puyo_stack = []
    for i in range(12):
        puyo_stack.append(['None', 'None', 'None', 'None', 'None', 'None'])

    while(True):
        # ぷよの落下速度
        pygame.time.Clock().tick(60)

        # 各列の一番下の判定
        for c in range(6):
            for r in range(12):
                if puyo_stack[r][c] == 'None':
                    ug[c] = 480 - 40*r
                    break
        
        # ゲームオーバー判定
        if game_start_flg:
            if puyo_stack[11][2] != 'None' or puyo_stack[11][3] != 'None':
                game_start_flg = False
                game_over_flg = True

        screen.blit(bg, rect_bg)
        screen.blit(flame, rect_flame)
        screen.blit(subflame, rect_subflame)
        screen.blit(batsu, rect_batsu)
        screen.blit(batsu2, rect_batsu2)
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
                stock2_puyo1, rect_stock2_puyo1 = load_image(puyo1, fp)
                stock2_puyo1_color = puyo1
                rect_stock2_puyo1.center = (360, 145)
                stock2_puyo2, rect_stock2_puyo2 = load_image(puyo2, fp)
                stock2_puyo2_color = puyo2
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
                if y1 != ug[(x1-25)//45] and y2 != ug[(x2-25)//45]:
                    y1 += 2
                    y2 += 2
                else:
                    puyo_drop_flg = False
        else:
            if game_over_flg:
                screen.blit(gameover, rect_gameover)
            else:
                screen.blit(push_enter, rect_push_enter)

        # ぷよを置く
        if game_start_flg and puyo_drop_flg is False:
            if y1 == y2:
                for r in range(12):
                    if puyo_stack[r][(x1-25)//45] == 'None':
                        to_y1 = 480 - r*40
                        r1 = r
                        c1 = (x1-25)//45
                        ug[(x1-25)//45] = 480 - (r+1)*40
                        break
                for r in range(12):
                    if puyo_stack[r][(x2-25)//45] == 'None':
                        to_y2 = 480 - r*40
                        r2 = r
                        c2 = (x2-25)//45
                        ug[(x2-25)//45] = 480 - (r+1)*40
                        break
            elif y1 < y2:
                for r in range(12):
                    if puyo_stack[r][(x2-25)//45] == 'None':
                        to_y2 = 480 - r*40
                        to_y1 = to_y2 - 40
                        r2 = r
                        c2 = (x2-25)//45
                        r1 = r2 + 1
                        c1 = c2
                        ug[(x2-25)//45] = 480 - (r+1)*40
                        break
            else:
                for r in range(12):
                    if puyo_stack[r][(x1-25)//45] == 'None':
                        to_y1 = 480 - r*40
                        to_y2 = to_y1 - 40
                        r1 = r
                        c1 = (x1-25)//45
                        r2 = r1 + 1
                        c2 = c1
                        ug[(x1-25)//45] = 480 - (r+1)*40
                        break
            while y1 != to_y1 or y2 != to_y2:
                pygame.time.Clock().tick(60)
                if y1 != to_y1:
                    y1 += 4
                if y2 != to_y2:
                    y2 += 4
                rect_drop_puyo1.topleft = (x1, y1)
                rect_drop_puyo2.topleft = (x2, y2)
                screen.blit(flame, rect_flame)
                screen.blit(batsu, rect_batsu)
                screen.blit(batsu2, rect_batsu2)
                stack_display(puyo_stack, fp, screen)
                screen.blit(drop_puyo1, rect_drop_puyo1)
                screen.blit(drop_puyo2, rect_drop_puyo2)
                pygame.display.update()
            puyo_stack[r1][c1] = drop_puyo1_color
            puyo_stack[r2][c2] = drop_puyo2_color

        # スタックぷよの表示
        if game_start_flg:
            stack_display(puyo_stack, fp, screen)

        # ぷよが消える判定
        if game_start_flg and puyo_drop_flg is False:
            erase_flg = True
            while erase_flg:
                erase_flg = False
                flg = False
                for r in range(12):
                    for c in range(6):
                        if puyo_stack[r][c] != 'None':
                            check_flg = []
                            for i in range(12):
                                check_flg.append([False, False, False, False, False, False])
                            puyo_stack, erase_flg = erase_puyo(puyo_stack, c, r, 1, check_flg, erase_flg)
                            if erase_flg:
                                screen.blit(flame, rect_flame)
                                screen.blit(batsu, rect_batsu)
                                screen.blit(batsu2, rect_batsu2)
                                stack_display(puyo_stack, fp, screen)
                                puyo_stack = bomb2none(puyo_stack)
                                puyo_stack = drop_all(puyo_stack)
                                pygame.time.delay(1000)
                                stack_display(puyo_stack, fp, screen)
                                flg = True
                                break
                    if flg:
                        break

        pygame.display.update()  # 画面更新

        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    game_start_flg = True
                if puyo_drop_flg:
                    # ぷよの回転
                    if event.key == K_SPACE:
                        # 下にある場合左へ
                        if y2 - y1 == 40 and x1 != 25:
                            y2 = y1
                            x2 = x1-45
                        # 左にある場合上へ
                        elif x1 - x2 == 45:
                            x2 = x1
                            y2 = y1-40
                        # 上にある場合右へ
                        elif y1 - y2 == 40 and x1 != 250:
                            y2 = y1
                            x2 = x1+45
                        # 右にある場合下へ
                        elif x2 - x1 == 45 and y1 < ug[(x1-25)//45]-40:
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
