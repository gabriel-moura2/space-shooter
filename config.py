SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
FPS = 60
MENU_BACKGROUND_COLOR = ((0, 255, 255))

TITLE_DISPLAY_CONFIG = {
    "position": (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT * 3 /10)),
    "text": "Galactic Onslaught",
    "size": int(SCREEN_HEIGHT / 6),
    "color": (0, 0, 0)
}
START_DISPLAY_CONFIG = {
    "position": (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 1.5)),
    "text": "Press space",
    "size": int(SCREEN_HEIGHT / 12),
    "color": (153, 153, 0)
}

SCROLL_SPEED = 75

HEALTH = 3
SHIP_SPEED = 150 # pixels/segundo
H_POSITION_PLAYER = SCREEN_WIDTH / 8
H_POSITION_ENEMY = SCREEN_WIDTH * 7 / 8
PROJECTILE_SPEED = SCREEN_WIDTH / 1
PROJECTILE_DELAY = 0.5
PROJECTILE_DAMAGE = 1
LEVEL_DISPLAY_CONFIG = {
    "position": (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 30)),
    "size": int(SCREEN_HEIGHT / 20),
    "color": (255, 255, 255)
}

GAME_OVER_DISPLAY_CONFIG = {
    "position": (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)),
    "text": "Game Over",
    "size": int(SCREEN_HEIGHT / 6),
    "color": (255, 0, 0)
}

SCORE_DISPLAY_CONFIG = {
    "position": (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT * 3 / 10)),
    "size": int(SCREEN_HEIGHT / 10),
    "color": (175, 255, 0)
}

TO_MENU_DISPLAY_CONFIG = {
    "position": (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 1.5)),
    "text": "Press P to menu",
    "size": int(SCREEN_HEIGHT / 12),
    "color": (153, 153, 0)
}
