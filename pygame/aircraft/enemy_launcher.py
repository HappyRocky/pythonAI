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
            
    def hit(self, bullet_list):
        '''
        所有敌机和所有子弹进行判断是否相撞。如果相撞，则子弹与敌机同时消失。
        '''
        new_enemy_list = []
        for enemy in self.enemy_list:
            has_hit = False # 默认没有相撞
            for bullet in bullet_list: # 与每个子弹进行判断
                if enemy.has_hit_bullet(bullet): # 如果撞到了
                    bullet_list.remove(bullet) # 子弹消失
                    has_hit = True
                    break
            if not has_hit: # 如果没有被撞
                new_enemy_list.append(enemy) # 加入到新list中
        self.enemy_list = new_enemy_list
            
    def show_enemys(self, screen):
        '''
        将敌机显示在屏幕上
        '''
        for enemy in self.enemy_list:
            enemy.show(screen)
