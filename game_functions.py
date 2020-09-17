import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, alien_settings, screen, ship, bullets):
    """响应按键事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一个子弹，并加入编组
        if len(bullets) < alien_settings.max_bullets:
            new_bullet = Bullet(alien_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """响应按键释放事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    

def check_events(alien_settings, screen, ship, bullets):
    """事件检测与响应"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, alien_settings, screen, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(alien_settings, screen, ship, bullets):
    """清空屏幕，重绘图像"""
    screen.fill(alien_settings.bg_color)
    # 绘制飞船
    ship.blit()
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.blit()

    # 刷新屏幕
    pygame.display.flip()



