from bullet import Bullet

class BulletLauncher():
    '''
    子弹发射器类
    '''
    def __init__(self, period = 200):
        '''
        初始化
        period:每隔多久发射一颗子弹
        '''
        self.period = period
        self.bullet_list = [] # 子弹发射器已经发射出的子弹
        self.time = 0 # 计时
        
        
    def move(self, plane_x, plane_y):
        '''
        每个子弹的进行运动
        plane_x:飞机x坐标
        plane_y:飞机y坐标
        '''
        # 每个子弹进行move
        new_bullet_list = []
        for bullet in self.bullet_list:
            result = bullet.move()
            if result == 1: # move之后仍然在屏幕之内，则保持在list中
                new_bullet_list.append(bullet)
        self.bullet_list = new_bullet_list  
        
        # 到达周期便发射一颗子弹
        self.time += 1
        if self.time % self.period == 0:
            self.bullet_list.append(Bullet(plane_x, plane_y)) # 在飞机位置增加一颗子弹
            self.time = 0
            
    def show_bullets(self, screen):
        '''
        将子弹显示在屏幕上
        '''
        for bullet in self.bullet_list:
            bullet.show(screen)