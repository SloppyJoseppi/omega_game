import pygame
import random

POWER_UP = pygame.transform.scale(pygame.image.load("assets/powerup.png"), [25,25])




class PowerUp(pygame.sprite.Sprite):

    def __init__(self, center):
        super().__init__()
        self.image = POWER_UP
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.center = center
        self.collect = False

#   def __init__(self, pos):
#       super().__init__()
#        self.image = POWER_UP
#
#
#      self.mask = pygame.mask.from_surface(self.image)
#       self.rect = self.image.get_rect(center=pos)



        self.speedy = +1


    def collected(self):
        self.collect = True
        self.kill()

    def update(self):

        self.rect.y += self.speedy


        if self.rect.bottom < 35:
            self.kill()




