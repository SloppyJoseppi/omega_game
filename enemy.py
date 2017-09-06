import pygame
import random

ENEMY = pygame.image.load('assets/enemy.png')
DESTRO_ENEMY = pygame.image.load('assets/destro_enemy.png')

class Enemy(pygame.sprite.Sprite):
    """ represents the enemy """

    def __init__(self):
        super().__init__()

        self.image = ENEMY
        self.rect = self.image.get_rect()
        self.time = None
        self.speed = random.randrange(1,4)
        self.direction = random.randrange(0,2)
        self.hit = False
        self.alive = True

    def explode(self):
        """ mark enemy as hit """

        self.hit = True
        self.time = pygame.time.get_ticks()
        self.image = DESTRO_ENEMY

    def update(self):
        """ update movement and state of enemy"""

        current_ticks = pygame.time.get_ticks()

        if self.time and self.hit:
            if (current_ticks - self.time) < 500:
                if self.direction == 0:
                    self.rect.x += 1
                else:
                    self.rect.x -= 1
                self.rect.y += 1
            else:
                self.alive = False
                self.kill()

        elif self.direction == 0:
            self.rect.x += self.speed

            if self.rect.x > 700:
                self.rect.x = -20
        elif self.direction == 1:
            self.rect.x -= self.speed

            if self.rect.x < -20 :
                self.rect.x = 720
