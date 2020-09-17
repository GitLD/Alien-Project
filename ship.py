import pygame

class Ship():
    def __init__(self, screen):
        """初始化飞船设置位置"""
        self.screen = screen

        # 加载图像,获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将飞船放置与屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blit(self):
        # 绘制飞船
        self.screen.blit(self.image, self.rect)
