import pygame
from scenes.scene import Scene
from entities.background import SpaceBackground
from entities.enemy_ship import EnemyShip
from entities.double_shot_enemy_ship import DoubleShotEnemyShip
from entities.player_ship import PlayerShip
from entities.text import Text
from entities.life import Life
from utils.helpers import generate_partitions
from config import SCREEN_HEIGHT, SHIP_SPEED, H_POSITION_PLAYER, H_POSITION_ENEMY, SCREEN_WIDTH, LEVEL_DISPLAY_CONFIG

class LevelScene(Scene):
    def __init__(self, manager, level):
        super().__init__(manager)
        self.level = level
        self._init_level_structure()
        self._init_game_objects()

    def _init_level_structure(self):
        self.wave_spawn_config = generate_partitions(self.level, 7)
        self.current_wave_index = 0

    def _init_game_objects(self):
        self.sprite_groups = {
            "enemies": pygame.sprite.Group(),
            "projectiles": pygame.sprite.Group(),
            "player": pygame.sprite.GroupSingle(PlayerShip()),
            "lifes": pygame.sprite.Group(),
            "explosions": pygame.sprite.Group(),
            "texts": pygame.sprite.Group(Text(**LEVEL_DISPLAY_CONFIG, text=f"Level {self.level}"))
        }
        self.sprite_groups["lifes"].add(Life(self.sprite_groups["player"].sprite))
        self.background = SpaceBackground()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.sprite_groups["player"].sprite.shoot(self.sprite_groups["projectiles"])
        pressed_keys = pygame.key.get_pressed()
        if (pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]):
            self.sprite_groups["player"].sprite.speed = -SHIP_SPEED * 2
        elif (pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]):
            self.sprite_groups["player"].sprite.speed = SHIP_SPEED * 2
        else:
            self.sprite_groups["player"].sprite.speed = 0
    
    def update(self, dt):
        self.background.update(dt)
        super().update(dt)
        for projectile in self.sprite_groups["projectiles"]:
            if projectile.rect.left < 0 or projectile.rect.right > SCREEN_WIDTH:
                projectile.kill()

        self._handle_enemy_attacks()
        
        # Melhorar renderização depois
        sprite_dict = pygame.sprite.groupcollide(self.sprite_groups["projectiles"], self.sprite_groups["enemies"], True, False)
        for projectile, enemies in sprite_dict.items():
            for enemy in enemies:
                projectile.explode(self.sprite_groups["explosions"])
                enemy.hit(projectile.damage)
                if enemy.health <= 0:
                    enemy.explode(self.sprite_groups["explosions"])
                    enemy.kill()
                break
        
        sprite_dict = pygame.sprite.groupcollide(self.sprite_groups["projectiles"], self.sprite_groups["player"], True, False)
        for projectile, player in sprite_dict.items():
            projectile.explode(self.sprite_groups["explosions"])
            player[0].hit(projectile.damage)
            if player[0].health <= 0:
                player[0].explode(self.sprite_groups["explosions"])
                player[0].kill()
            break

        if len(self.sprite_groups["enemies"]) == 0:
            if self.current_wave_index < len(self.wave_spawn_config):
                enemy_types = self.wave_spawn_config[self.current_wave_index]
                self.current_wave_index += 1
                for i in range(len(enemy_types)):
                    enemy_type = enemy_types[i]-1
                    if enemy_type >> 4 & 1 == 0:
                        enemy = EnemyShip((SCREEN_WIDTH + H_POSITION_PLAYER, SCREEN_HEIGHT * (i + 1) / (len(enemy_types) + 1)), enemy_type)
                    else:
                        enemy = DoubleShotEnemyShip((SCREEN_WIDTH + H_POSITION_PLAYER, SCREEN_HEIGHT * (i + 1) / (len(enemy_types) + 1)), enemy_type)
                    self.sprite_groups["enemies"].add(enemy)
                    self.sprite_groups["lifes"].add(Life(enemy))
            else:
                self.manager.change_scene(LevelScene(self.manager, self.level + 1))

        if len(self.sprite_groups["player"]) == 0:
            from scenes.game_over import GameOverScene
            self.manager.change_scene(GameOverScene(self.manager, f"#{self.level}.{self.current_wave_index}"))
    
    def draw(self, screen):
        self.background.draw(screen)
        super().draw(screen)

    def _handle_enemy_attacks(self):
        for enemy in self.sprite_groups["enemies"]:
            if self.sprite_groups["player"].sprite.rect.clipline(self._calculate_attack_line(enemy.rect)):
                enemy.shoot(self.sprite_groups["projectiles"])

    def _calculate_attack_line(self, rect):
        return (rect.centerx - (H_POSITION_ENEMY - H_POSITION_PLAYER), rect.centery, rect.centerx, rect.centery)