import pygame

LAZER = (0, 255, 43)

class Bullet(pygame.sprite.Sprite):
    """ represents Projectiles """

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(LAZER)
        self.rect = self.image.get_rect()

    def update(self):
        """ move the bullet """

        self.rect.y -= 5
