import pygame

PLAYER = pygame.image.load('assets/ship.png')

class Player(pygame.sprite.Sprite):
    """ represents the Player. """

    def __init__(self):
        super().__init__()

        self.image = PLAYER
        self.rect = self.image.get_rect()
        self.rect.centerx = 10
        self.rect.x = 350
        self.speed = 4

    def draw(self, screen):
        """ draw player specifically """

        screen.blit(self.image, self.rect)

    def update(self):
        """ update the player's position to the mouse x position """

        pos = pygame.mouse.get_pos()

        if self.rect.centerx + 5 == 0 or self.rect.x - 5 == 0:
            self.rect.centerx = pos[0]
        elif self.rect.centerx > pos[0] + 5:
            self.rect.x -= self.speed
        elif self.rect.centerx < pos[0] - 5:
            self.rect.x += self.speed


