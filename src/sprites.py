import pygame
import random
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Intentar cargar la imagen generada por IA, si no, crear un rectángulo
        try:           
            # Carga de la nave del jugador
            self.image = pygame.image.load(f"{IMG_DIR}/player.png").convert_alpha()

        except:
            self.image = pygame.Surface((50, 40))
            self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.speed_x = PLAYER_SPEED
        
        self.rect.x += self.speed_x

        # Mantener al jugador dentro de la pantalla
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, bullet_group):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullet_group.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load(f"{IMG_DIR}/enemy.png").convert_alpha()
        except:
            self.image = pygame.Surface((30, 30))
            self.image.fill(RED)
            
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)

    def update(self):
        self.rect.y += self.speed_y
        # Si sale de la pantalla, desaparece para ahorrar memoria
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = BULLET_SPEED

    def update(self):
        self.rect.y += self.speed_y
        # Eliminar si sale de la pantalla
        if self.rect.bottom < 0:
            self.kill()