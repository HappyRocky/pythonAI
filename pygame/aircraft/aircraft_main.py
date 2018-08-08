# -*- coding: utf-8 -*-
import pygame
from sys import exit
import config
from plane import Plane
from enemy_launcher import EnemyLauncher

# 初始化画布
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('aircraft')
pygame.mouse.set_visible(False)

# 加载背景
background = pygame.image.load('data/back.jpg').convert()

# 初始化对象
plane = Plane()
enemy_launcher = EnemyLauncher()

# 飞机重生周期
reborn = 500
crash_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))
    
    # 达到了重生时间
    if crash_count >= reborn:
        plane = Plane()
        enemy_launcher = EnemyLauncher()
        crash_count = 0
        continue
    
    # 继续累加重生时间
    if crash_count > 0:
        crash_count += 1
    
    # 获取鼠标位置
    x, y = pygame.mouse.get_pos()
    
    # 飞机及子弹运动
    plane.move(x, y)
    
    # 敌机运动
    enemy_launcher.move()
    
    # 碰撞子弹
    enemy_launcher.hit(plane.bullet_launcher.bullet_list)
    
    # 碰撞主机
    enemy_launcher.crash(plane)
    
    #  显示
    if plane.has_crash:
        if crash_count == 0:
            crash_count = 1
    else:
        plane.show(screen)
        
    enemy_launcher.show_enemys(screen)
    
    # 刷新
    pygame.display.update()