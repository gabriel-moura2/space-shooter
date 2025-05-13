from entities.space_ship import SpaceShip
from utils.helpers import load_image
from config import H_POSITION_PLAYER, SCREEN_HEIGHT

class PlayerShip(SpaceShip):
    def __init__(self):
        super().__init__(load_image("player"), (H_POSITION_PLAYER, SCREEN_HEIGHT / 2))