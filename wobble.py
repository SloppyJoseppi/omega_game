import pygame
from bullet import Bullet

WOBBLE = pygame.image.load('assets/wobble.png')


class Wobble_shot(Bullet, pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Wobble_shot, self).__init__(pos)

        self.image = WOBBLE.convert_alpha()
        self.wobble = 'right'
        self.speed = 3
        self.x_origin = pos[0]

    # def explode(self):


    def update(self):

        super().update()

        delta = 10
        diff = self.x_origin - self.rect.x

        # always moving
        if self.wobble == 'right':
            self.rect.x += 2
        else:
            self.rect.x -= 2

        if diff < -delta:
            self.wobble = 'left'
        elif diff > delta:
            self.wobble = 'right'

        if self.rect.y < 250:
            growth = 250 - self.rect.y
            if growth < 30:
                self.image = pygame.transform.scale(WOBBLE.convert_alpha(), (growth, growth))
