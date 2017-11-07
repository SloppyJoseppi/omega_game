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
        self.rect_img = self.image.get_rect()
        self.rect_img.x = x
        self.rect_img.y = y
        self.rect = self.rect_img.copy()
        self.rect.height = size[0] / 2
        self.rect.width = size[1] / 2
        self.size = size
        self.speed = speed
        self.hp = hp

    def draw(self, screen):
        """ draws the asteroids with new image based on hp"""

        if self.hp < 5:
            self.image = self.sheet[6]

        elif self.hp < 10:
            self.image = self.sheet[5]

        elif self.hp < 12:
            self.image = self.sheet[4]

        elif self.hp < 14:
            self.image = self.sheet[3]

        elif self.hp < 16:
            self.image = self.sheet[2]

        elif self.hp < 18:
            self.image = self.sheet[1]

        if self.hp > 0:
          screen.blit(self.image, self.rect_img)

    def update(self):
        """ update the asteroids's position """

        self.rect_img.y += self.speed

        if self.rect_img.y > 460:
            self.rect_img.y = -60
            self.rect_img.x = random.randint(0, 680)

        self.rect.center = self.rect_img.center
        # current_ticks = pygame.time.get_ticks()

        if self.hp <= 0:
            self.kill()


