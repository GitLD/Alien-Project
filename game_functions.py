import sys

import pygame
from bullet import Bullet
from alien import Alien

def get_number_aliens_x(alien_settings, alien_width):
    """获取一行可以容纳的外星人数"""
    available_space_x = alien_settings.screen_width - 2*alien_width
    number_aliens_x = available_space_x // (2*alien_width)
    return number_aliens_x

def get_number_aliens_y(alien_settings, ship_height, alien_height):
    """获取列方向可以容纳的外星人数"""
    # 初始外星人群距离飞船2倍外星人距离
    available_space_y = alien_settings.screen_height - ship_height - 3*alien_height
    number_aliens_y = available_space_y // (2*alien_height)
    return number_aliens_y

def create_alien(alien_settings, screen, aliens, alien_number, row_number):
    """创建行内的一个外星人"""
    alien = Alien(alien_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien_height = alien.rect.height
    alien.y = alien_height + 2*alien_height*row_number
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(alien_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(alien_settings, screen)
    # 计算一行能放置的外星人数
    number_aliens_x = get_number_aliens_x(alien_settings, alien.rect.width)
    number_aliens_y = get_number_aliens_y(alien_settings, ship.rect.height, 
    alien.rect.width)

    # 创建一行外星人
    for row_number in range(number_aliens_y):
        for alien_number in range(number_aliens_x):
            create_alien(alien_settings, screen, aliens, alien_number, row_number) 
        
def fire_bullet(alien_settings, screen, ship, bullets):
    """如果没有达到最大子弹数,就发射一颗子弹"""
    # 创建一个子弹，并加入编组
    if len(bullets) < alien_settings.max_bullets:
        new_bullet = Bullet(alien_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, alien_settings, screen, ship, bullets):
    """响应按键事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一个子弹，并加入编组
        fire_bullet(alien_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

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

def update_screen(alien_settings, screen, ship, aliens, bullets):
    """清空屏幕，重绘图像"""
    screen.fill(alien_settings.bg_color)
    # 绘制飞船
    ship.blit()
    # 绘制外星人
    aliens.draw(screen)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.blit()

    # 刷新屏幕
    pygame.display.flip()

def check_bullet_alien_collision(alien_settings, screen, ship, aliens, bullets):
    """响应子弹与外星人的碰撞"""
    # 外星人与子弹间碰撞检测
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 清空屏幕残留子弹，生成一批外星人
        bullets.empty()
        create_fleet(alien_settings, screen, ship, aliens)

def update_bullets(alien_settings, screen, ship, aliens, bullets):
    """更新子弹位置，并删除消失的子弹"""
    # 更新所有子弹位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():   # 使用copy避免遍历过程对列表修改的问题
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(alien_settings, screen, ship, aliens, bullets)

def check_fleet_edges(alien_settings, aliens):
    """当外星人群越界时"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(alien_settings, aliens)
            break

def change_fleet_direction(alien_settings, aliens):
    """外星人群下移，改变左右移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += alien_settings.fleet_drop_speed
    alien_settings.fleet_direction *= -1

def update_aliens(alien_settings, aliens):
    """更新外星人位置"""
    check_fleet_edges(alien_settings, aliens)
    aliens.update()


