import pygame
import random
from sprite_sheet_loader import sprite_sheet

ASTEROID = 'assets/asteroid.png'

class Asteroid(pygame.sprite.Sprite):
    """ represents the asteroids """
    def __init__(self, size, hp, x, y, speed=2):
        super().__init__()

        self.sheet = sprite_sheet((64,64), ASTEROID)
        self.image =  self.sheet[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.height = size[0]
        self.rect.width = size[1]
        self.size = size
        self.speed = speed
        self.hp = hp

    # def explode(self):



    def update(self):
        """ update the player's position to the mouse x position """

        self.rect.y += self.speed

        if self.rect.y > 460:
            self.rect.y = -60
            self.rect.x = random.randint(0, 700)

        # current_ticks = pygame.time.get_ticks()

        if self.hp <= 0:
            self.kill()

        elif self.hp < 5:
            self.image = self.sheet[6]

        elif self.hp < 10:
            self.image = self.sheet[5]
            self.rect.height = self.size[0]/2
            self.rect.width = self.size[1]/2

        elif self.hp < 12:
            self.image = self.sheet[4]

        elif self.hp < 14:
            self.image = self.sheet[3]

        elif self.hp < 16:
            self.image = self.sheet[2]

        elif self.hp < 18:
            self.image = self.sheet[1]
