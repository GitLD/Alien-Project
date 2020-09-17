import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人类"""
    def __init__(self, alien_settings, screen):
        """初始化外星人的位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.alien_settings = alien_settings

        # 加载外星人图像,获取rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置外星人位置(屏幕左上角)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 外星人位置浮点数
        self.x = float(self.rect.x)

    def check_edges(self):
        """边缘检测，越界True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
        return False

    def update(self):
        """更新外星人位置"""
        self.x += (self.alien_settings.alien_speed_factor*
        self.alien_settings.fleet_direction)
        self.rect.x = self.x

    def blit(self):
        """绘制外星人"""
        self.screen.blit(self.image, self.rect)
