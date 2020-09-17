import pygame

class Ship():
    def __init__(self, alien_settings, screen):
        """初始化飞船设置位置"""
        self.screen = screen
        self.alien_settings = alien_settings

        # 加载图像,获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将飞船放置与屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 储存位置的浮点数
        self.center = float(self.rect.centerx)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """根据移动标志调整飞船位置"""
        # 由于rect只储存整数，这边通过调整center，来调整rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.alien_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.alien_settings.ship_speed_factor
        
        self.rect.centerx = self.center
    
    def blit(self):
        # 绘制飞船
        self.screen.blit(self.image, self.rect)
