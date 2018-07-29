from bullet_launcher import BulletLauncher
import pygame

class Plane():
    '''
    飞机类
    '''
    def __init__(self, bullet_launcher = BulletLauncher()):
        self.x = 0 # 飞机中心x坐标
        self.y = -1 # 飞机中心y坐标
        self.image = pygame.image.load('data/plane.png').convert_alpha()
        self.bullet_launcher = bullet_launcher # 飞机采用的哪种发射器
    
    def move(self, mouse_x, mouse_y):
        '''
        飞机里的一切部件进行运动
        mouse_x:鼠标x坐标
        mouse_y:鼠标y坐标
        '''
        # 飞机运动
        self.x = mouse_x
        self.y = mouse_y
        
        # 发射器运动
        self.bullet_launcher.move(self.x, self.y)

    def show(self, screen):
        '''
        显示飞机及子弹
        '''
        # 计算飞机左上角坐标值
        x = self.x - self.image.get_width() / 2
        y = self.y - self.image.get_height() / 2
        # 显示飞机
        screen.blit(self.image, (x, y))        
        
        # 显示子弹
        self.bullet_launcher.show_bullets(screen)