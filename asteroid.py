import pygame

ASTEROID = pygame.image.load('assets/asteroid.png')

class Asteroid(pygame.sprite.Sprite):
  def __init__(self, size, hp, x, y):
    super().__init__()

    self.image = ASTEROID
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.size = size
    self.hp = hp

  def update(self):
        """ update the player's position to the mouse x position """

        self.rect.x -= 4
