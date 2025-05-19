import pygame
from scenes.scene import Scene
from entities.background import SpaceBackground
from entities.enemy_ship import EnemyShip
from entities.double_shot_enemy_ship import DoubleShotEnemyShip
from entities.player_ship import PlayerShip
from entities.text import Text
from entities.life import Life
from utils.helpers import generate_partitions
from config import SCREEN_HEIGHT, SHIP_SPEED, H_POSITION_PLAYER, H_POSITION_ENEMY, SCREEN_WIDTH, LEVEL_X, LEVEL_Y, LEVEL_SIZE, LEVEL_COLOR

class LevelScene(Scene):
    def __init__(self, manager, level):
        super().__init__(manager)
        self.level = level
        self.stage_partitions = generate_partitions(self.level, 6)
        self.stage = 0
        self.explosions = pygame.sprite.Group()
        self.explosions.add(pygame.sprite.GroupSingle())
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.player.add(PlayerShip())
        self.texts = pygame.sprite.Group()
        self.texts.add(Text((LEVEL_X, LEVEL_Y), f"Level {self.level}", LEVEL_SIZE, LEVEL_COLOR))
        self.lifes = pygame.sprite.Group()
        self.lifes.add(Life(self.player.sprite))
        self.background = SpaceBackground()
        self.entities = [self.texts, self.player, self.lifes, self.enemies, self.projectiles, self.explosions]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.player.sprite.shoot(self.projectiles)
        pressed_keys = pygame.key.get_pressed()
        if (pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]):
            self.player.sprite.speed = -SHIP_SPEED * 2
        elif (pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]):
            self.player.sprite.speed = SHIP_SPEED * 2
        else:
            self.player.sprite.speed = 0
    
    def update(self, dt):
        self.background.update(dt)
        super().update(dt)
        for projectile in self.projectiles:
            if projectile.rect.left < 0 or projectile.rect.right > SCREEN_WIDTH:
                projectile.kill()

        for enemy in self.enemies:
            if type(enemy) == DoubleShotEnemyShip:
                view = (enemy.rect.centerx - (H_POSITION_ENEMY - H_POSITION_PLAYER), enemy.rect.top, enemy.rect.centerx, enemy.rect.top)
                if self.player.sprite.rect.clipline(view):
                    enemy.shoot(self.projectiles)
                view2 = (enemy.rect.centerx - (H_POSITION_ENEMY - H_POSITION_PLAYER), enemy.rect.bottom, enemy.rect.centerx, enemy.rect.bottom)
                if self.player.sprite.rect.clipline(view2):
                    enemy.shoot2(self.projectiles)
            else:
                view = (enemy.rect.centerx - (H_POSITION_ENEMY - H_POSITION_PLAYER), enemy.rect.centery, enemy.rect.centerx, enemy.rect.centery)
                if self.player.sprite.rect.clipline(view):
                    enemy.shoot(self.projectiles)
        
        # Melhorar renderização depois
        sprite_dict = pygame.sprite.groupcollide(self.projectiles, self.enemies, True, False)
        for projectile, enemies in sprite_dict.items():
            for enemy in enemies:
                projectile.explode(self.explosions)
                enemy.hit(projectile.damage)
                if enemy.health <= 0:
                    enemy.explode(self.explosions)
                    enemy.kill()
                break
        
        sprite_dict = pygame.sprite.groupcollide(self.projectiles, self.player, True, False)
        for projectile, player in sprite_dict.items():
            projectile.explode(self.explosions)
            player[0].hit(projectile.damage)
            if player[0].health <= 0:
                player[0].explode(self.explosions)
                player[0].kill()
            break

        if len(self.enemies) == 0:
            if self.stage < len(self.stage_partitions):
                enemy_types = self.stage_partitions[self.stage]
                self.stage += 1
                for i in range(len(enemy_types)):
                    enemy_type = enemy_types[i]-1
                    if enemy_type >> 4 & 1 == 0:
                        enemy = EnemyShip((SCREEN_WIDTH + H_POSITION_PLAYER, SCREEN_HEIGHT * (i + 1) / (len(enemy_types) + 1)), enemy_type)
                    else:
                        enemy = DoubleShotEnemyShip((SCREEN_WIDTH + H_POSITION_PLAYER, SCREEN_HEIGHT * (i + 1) / (len(enemy_types) + 1)), enemy_type)
                    self.enemies.add(enemy)
                    self.lifes.add(Life(enemy))
            else:
                self.manager.change_scene(LevelScene(self.manager, self.level + 1))

        if len(self.player) == 0:
            from scenes.game_over import GameOverScene
            self.manager.change_scene(GameOverScene(self.manager, f"#{self.level}.{self.stage}"))
    
    def draw(self, screen):
        self.background.draw(screen)
        super().draw(screen)