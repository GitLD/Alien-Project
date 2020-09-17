import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    alien_setting = Settings()
    screen = pygame.display.set_mode(
        (alien_setting.screen_width, alien_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始主循环
    while True:

        # 监视键盘鼠标事件
        gf.check_events()
        
        # 更新屏幕图像
        gf.update_screen(alien_settings, screen, ship)


run_game()