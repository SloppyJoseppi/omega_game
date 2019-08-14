import pygame
import random

ENEMY = pygame.image.load('assets/enemy.png')
DESTRO_ENEMY = pygame.image.load('assets/destro_enemy.png')

class Enemy(pygame.sprite.Sprite):
    """ represents the enemy """

    def __init__(self):
        super().__init__()

        self.image = ENEMY
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.time = None
        self.speed = random.randrange(1, 4)
        self.direction = random.randrange(0, 2)
        self.destruction_sound = pygame.mixer.Sound('assets/sounds/enemy_hit.ogg')
        self.hit = False
        self.attacking = False
        self.alive = True
        self.attack_timing = random.randrange(300, 850)
        self.timer = 0
        self.timer_active = False
        self.starting_y = self.rect.y


    def explode(self):
        """ mark enemy as hit """

        self.hit = True
        self.destruction_sound.play()
        self.time = pygame.time.get_ticks()
        self.image = DESTRO_ENEMY

    def start_timer(self):
        self.timer_active = True
        if self.timer_active:
            self.timer += 1

    def reset_timer(self):
        self.timer_active = False
        self.timer = 0

    def attack(self):
        """ attempt to attack the player """

        if self.rect.y == self.starting_y and not self.attacking:
            self.attacking = True



    def swoop_animation(self):
        """ handles attack animation """
        if self.attacking and self.rect.y <= 315 and not self.hit:
            self.rect.y += self.speed
        elif self.attacking and self.rect.y > self.starting_y and not self.hit:
            self.attacking = False

        if not self.attacking and self.rect.y != self.starting_y and not self.hit:
            self.rect.y -= self.speed


    def death_animation(self, current_ticks):
        if (current_ticks - self.time) < 500:
            if self.direction == 0:
                self.rect.x += 1
            else:
                self.rect.x -= 1
            self.rect.y += 1
        else:
            self.alive = False
            self.kill()

    def update(self):
        """ update movement and state of enemy """

        current_ticks = pygame.time.get_ticks()

        self.start_timer()

        if self.timer >= self.attack_timing:
            self.attack()
            self.reset_timer()
        self.swoop_animation()

        if self.time and self.hit:
            self.death_animation(current_ticks)

        elif self.direction == 0:
            self.rect.x += self.speed

            if self.rect.x > 700:
                self.rect.x = -20
        elif self.direction == 1:
            self.rect.x -= self.speed

            if self.rect.x < -20 :
                self.rect.x = 720
