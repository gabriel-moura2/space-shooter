import pygame
from scenes.scene import Scene
from entities.background import Background
from entities.enemy_ship import EnemyShip
from entities.player_ship import PlayerShip
from entities.explosion import ExplosionEffect
from config import SCREEN_HEIGHT, SHIP_SPEED, SCREEN_WIDTH

class LevelScene(Scene):
    def __init__(self, manager, level):
        super().__init__(manager)
        self.level = level
        self.explosions = pygame.sprite.Group()
        self.explosions.add(ExplosionEffect((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)))
        self.explosions.add(pygame.sprite.GroupSingle())
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.enemies.add(EnemyShip(SCREEN_HEIGHT / 2, 3))
        self.player = pygame.sprite.GroupSingle()
        self.player.add(PlayerShip())
        self.background = Background()
        self.entities = [self.player, self.enemies, self.projectiles, self.explosions]

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
        for projectile in self.projectiles.sprites():
            if projectile.rect.left < 0 or projectile.rect.right > SCREEN_WIDTH:
                projectile.kill()

        for enemy in self.enemies.sprites():
            view = (enemy.rect.centerx - SCREEN_WIDTH, enemy.rect.centery, enemy.rect.centerx, enemy.rect.centery)
            if self.player.sprite.rect.clipline(view):
                enemy.shoot(self.projectiles)
        
        # Melhorar renderização depois
        sprite_dict =pygame.sprite.groupcollide(self.projectiles, self.enemies, True, False)
        for projectile, enemies in sprite_dict.items():
            for enemy in enemies:
                enemy.hit(projectile.damage)
                if enemy.health <= 0:
                    enemy.kill()
                break
        
        sprite_dict = pygame.sprite.groupcollide(self.projectiles, self.player, True, False)
        for projectile, player in sprite_dict.items():
            player[0].hit(projectile.damage)
            if player[0].health <= 0:
                pygame.quit()
                exit()
            break
    
    def draw(self, screen):
        self.background.draw(screen)
        super().draw(screen)