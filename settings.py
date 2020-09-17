class Settings():
    """设置类"""

    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船速度
        self.ship_speed_factor = 1.5

        # 外星人速度
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1向右,-1向左

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.max_bullets = 3