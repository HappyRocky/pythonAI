# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 23:19:34 2018

@author: GongYanshang

敌人战机类
"""
import random
import pygame
import config

class Enemy():
    '''
    敌人战机类，从上而下运动
    '''
    
    def __init__(self):
        self.x = random.randint(50, config.SCREEN_WIDTH - 50)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + 0.1
        self.image = pygame.image.load('data/enemy.png').convert_alpha()
        
    def move(self):
        '''
        移动飞机
        return -1：超出屏幕；1：在屏幕内
        '''
        self.y += self.speed
        if self.y > config.SCREEN_HEIGHT + 50:
            return -1
        else:
            return 1
        
    def show(self, screen):
        '''
        显示在屏幕上
        '''
        # 计算左上角坐标值
        x = self.x - self.image.get_width() / 2
        y = self.y - self.image.get_height() / 2
        # 显示
        screen.blit(self.image, (x, y))
        
    def has_hit_bullet(self, bullet):
        '''
        是否撞到了子弹
        '''
        
        # 只要子弹位于敌机的矩形图片内，便认为相撞了
        if abs(bullet.x - self.x) <  self.image.get_width() / 2\
        and abs(bullet.y - self.y) <  self.image.get_height() / 2:
            return True
        return False
    
    def has_crash(self, plane):
        '''
        是否和飞机相撞
        '''
        if plane.has_crash:
            return False
        
        if abs(plane.x - self.x) < (self.image.get_width() + plane.image.get_width()) / 2\
        and abs(plane.y - self.y) < (self.image.get_height() + plane.image.get_height()) / 2:
            return True
        return False

