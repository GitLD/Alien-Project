import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹类"""

    def __init__(self, alien_settings, screen, ship):
        """在飞船位置创建子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0, 0)处创建一个子弹大小的矩形
        self.rect = pygame.Rect(0, 0, 
            alien_settings.bullet_width, alien_settings.bullet_height)
        # 设置子弹位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 用浮点数储存子弹位置
        self.y = float(self.rect.y)

        self.color = alien_settings.bullet_color
        self.speed_factor = alien_settings.bullet_speed_factor
    
    def update(self):
        """更新子弹位置"""
        # 通过更新y来更新rect
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def blit(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
