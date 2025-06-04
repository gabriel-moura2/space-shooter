import pygame, asyncio
from core.game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game()
    asyncio.run(game.run())
    pygame.quit()
