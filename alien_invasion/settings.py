class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self, bg_color):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_hight = 800
        self.bg_color = bg_color
        # Ship settings
        self.ship_speed = 1.5
        # Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, bg_color):
        self._bg_color = bg_color


