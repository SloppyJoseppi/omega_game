import pygame

PLAYER = pygame.image.load('assets/ship.png')

class Player(pygame.sprite.Sprite):

    """ represents the Player. """

    def __init__(self):
        super().__init__()

        self.image = PLAYER
        self.rect = self.image.get_rect()

    def draw(self, screen):
        """ draw player specifically """

        screen.blit(self.image, self.rect)

    def update(self):
        """ update the player's position to the mouse x position """

        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]
