'''
子弹类
'''
import pygame
class Bullet:
    '''
    子弹类
    '''
    def __init__(self, x = 0, y = -1, speed = 1):
        '''
        初始化成员变量
        '''
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load('data/bullet.png').convert_alpha()
    
    def move(self):
        '''
        子弹运动
        return -1：子弹摧毁，否则子弹存在
        '''
        self.y -= self.speed
        if self.y < 0:
            return -1
        else:
            return 1
        
    def show(self, screen):
        '''
        子弹显示在屏幕上
        '''
        # 计算子弹左上角坐标值
        x = self.x - self.image.get_width() / 2
        y = self.y - self.image.get_height() / 2
        # 显示
        screen.blit(self.image, (x, y))