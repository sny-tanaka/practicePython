# coding: utf-8

import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()  # 初期化
    screen = pygame.display.set_mode((400, 565))  # ウィンドウサイズの指定
    pygame.display.set_caption('ぷよぷよ')  # タイトルバー
    bg = pygame.image.load('images\\bg.png').convert_alpha()
    rect_bg = bg.get_rect()

    while(True):
        screen.fill((0, 0, 0))  # 背景色の指定。RGBだと思う
        screen.blit(bg, rect_bg)
        pygame.display.update()  # 画面更新

        for event in pygame.event.get():  # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
