import pygame

PLAYER = pygame.image.load('assets/ship.png')

class Player(pygame.sprite.Sprite):
    """ represents the Player. """

    def __init__(self):
        super().__init__()

        self.image = PLAYER
        self.mask = pygame.mask.from_surface(self.image)
        self.rect_image = self.image.get_rect()
        self.rect = self.rect_image.copy()
        self.rect_image.centerx = 10
        self.rect_image.x = 350
        self.rect_image.y = 330
        self.rect.centerx = self.rect.width / 2
        self.speed = 4

    def draw(self, screen):
        """ draw player specifically """

        screen.blit(self.image, self.rect_image)

    def update(self):
        """ update the player's position to the mouse x position """

        pos = pygame.mouse.get_pos()

        self.rect.center = self.rect_image.center

        if self.rect_image.centerx + 5 == 0 or self.rect.x - 5 == 0:
            self.rect_image.centerx = pos[0]
        elif self.rect_image.centerx > pos[0] + 5:
            self.rect_image.x -= self.speed
        elif self.rect_image.centerx < pos[0] - 5:
            self.rect_image.x += self.speed


