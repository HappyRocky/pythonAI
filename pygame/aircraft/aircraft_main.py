# -*- coding: utf-8 -*-
import pygame
from sys import exit
from bullet import Bullet
from plane import Plane

# 初始化画布
pygame.init()
screen = pygame.display.set_mode((450, 800), 0, 32)
pygame.display.set_caption('aircraft')

# 加载背景
background = pygame.image.load('data/back.jpg').convert()

# 初始化飞机
plane = Plane()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))
    
    # 获取鼠标位置
    x, y = pygame.mouse.get_pos()
    
    # 飞机及子弹运动
    plane.move(x, y)
    
    # 飞机及子弹显示
    plane.show(screen)
    
    # 刷新
    pygame.display.update()