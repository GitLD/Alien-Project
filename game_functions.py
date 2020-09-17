import sys

import pygame

def check_events(ship):
    """事件检测与响应"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(alien_settings, screen, ship):
    """清空屏幕，重绘图像"""
    screen.fill(alien_settings.bg_color)
    ship.blit()

    # 刷新屏幕
    pygame.display.flip()



