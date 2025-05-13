from entities.space_ship import SpaceShip
from utils.helpers import load_image
from config import H_POSITION_ENEMY

class EnemyShip(SpaceShip):
    def __init__(self, position):
        super().__init__(load_image("enemy"), (H_POSITION_ENEMY, position))
    
    def update(self, dt):
        super().update(dt)
    
    def draw(self, screen):
          super().draw(screen)
        