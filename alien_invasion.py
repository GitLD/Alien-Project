import sys

import pygame
from settings import Settings
from ship import Ship

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    alien_setting = Settings()
    screen = pygame.display.set_mode(
        (alien_setting.screen_width, alien_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 设置背景色
    bg_color = alien_setting.bg_color  # 浅灰色

    # 开始主循环
    while True:

        # 监视键盘鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 清空屏幕,重新绘制
        screen.fill(bg_color)
        ship.blit()

        # 刷新画面
        pygame.display.flip()

run_game()