import sys

import pygame

def check_events():
    """事件检测与响应"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(alien_settings, screen, ship):
    """清空屏幕，重绘图像"""
    screen.fill(alien_settings.bg_color)
    ship.blit()

    # 刷新屏幕
    pygame.display.flip()



