# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 23:44:27 2018

@author: GongYanshang

敌机生成器
"""

import random
from enemy import Enemy

class EnemyLauncher():
    '''
    敌机生成器类，不断在最上方产生敌机
    '''
    
    def __init__(self, period_scope = [200, 400]):
        '''
        初始化
        period_scope: [min, max]，每隔多久生成一个敌机，间隔取最小值和最大值的随机值
        '''
        self.period_scope = period_scope
        self.period = random.randint(period_scope[0], period_scope[1])
        self.enemy_list = [] # 屏幕内存在的飞机
        self.time = 0 # 计时
        
    def move(self):
        '''
        每个敌机进行运动
        '''
        # 每个敌机进行move
        new_enemy_list = []
        for enemy in self.enemy_list:
            result = enemy.move()
            if result == 1: # move之后仍然在屏幕之内，则保持在list中
                new_enemy_list.append(enemy)
        self.enemy_list = new_enemy_list  
        
        # 到达周期便生成一个敌机
        self.time += 1
        if self.time % self.period == 0:
            self.enemy_list.append(Enemy()) # 生成一个敌机
            self.time = 0
            self.period = random.randint(self.period_scope[0], self.period_scope[1])
            
    def show_enemys(self, screen):
        '''
        将敌机显示在屏幕上
        '''
        for enemy in self.enemy_list:
            enemy.show(screen)
