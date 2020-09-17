import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    alien_settings = Settings()
    screen = pygame.display.set_mode(
        (alien_settings.screen_width, alien_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(alien_settings, screen)
    bullets = Group()

    # 开始主循环
    while True:

        # 监视键盘鼠标事件
        gf.check_events(alien_settings, screen, ship, bullets)
        # 更新飞船位置
        ship.update()
        # 更新所有子弹位置
        bullets.update()
        # 删除消失的子弹
        for bullet in bullets.copy():   # 使用copy避免遍历过程对列表修改的问题
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        # 更新屏幕图像
        gf.update_screen(alien_settings, screen, ship, bullets)


run_game()