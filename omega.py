
import pygame
import random
import time
from background import Background
from enemy import Enemy
from player import Player
from bullet import Bullet
from hud import Hud
from score import Score
from wobble import Wobble_shot
# from asteroid import Asteroid

# create a file for constant vars colors bgs etc
# create a game class!!!

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
BACKGROUND = 'assets/background.png'
START_BG = 'assets/start_bg.png'
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.mixer.pre_init(frequency=22050, size=8, channels=2, buffer=1024)
# init pygame
pygame.init()
pygame.mixer.music.load('assets/music/Omega.ogg')
# by default hide mouse
pygame.mouse.set_visible(False)
pygame.display.set_caption('OMEGA!')
clock = pygame.time.Clock()
# global obj to track high scores
scores = Score()

sounds = {
    'wobble_shot': pygame.mixer.Sound('assets/sounds/wobble.ogg')
}

# creates 'text objects' for displaying messages
# handy functions from a tutorial needs re-write to better suit my needs
def text_objects(text, font, color):
    text_surf = font.render(text, True, color)
    return text_surf, text_surf.get_rect()

# uses text objects to display messages on screen
# same here, ok for now...
def message_display(text, color):
    large_text = pygame.font.Font('freesansbold.ttf',30)
    # create text 'objects'
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = ((screen_width/2),(screen_height/2))
    # blit the text object to the screen
    screen.blit(text_surf, text_rect)
    # update the screen to show new text
    pygame.display.update()
    # pause for a moment to allow player to see message
    time.sleep(3)


# create a button class rather than this function
def button(msg, x, y, width, height, colors, action=None):
    """ function to easily create functional buttons """

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, colors[0], (x, y, width, height))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, colors[1], (x, y, width, height))

    small_text = pygame.font.Font('freesansbold.ttf',20)
    text_surf, text_rect = text_objects(msg, small_text, colors[2])
    text_rect.center = ((x + (width/2)),(y + (height / 2)))

    screen.blit(text_surf, text_rect)

    pygame.display.update()


def start_loop():
    selected = False
    background = Background(START_BG, [0, 0])
    top_score = Hud(10, 350, 200, 40, "TOP SCORE")

    while not selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                selected = True

        top_score.prop = scores.top_score
        clock.tick(20)
        pygame.mouse.set_visible(True)
        screen.blit(background.image, background.rect)

        large_text = pygame.font.Font('freesansbold.ttf',80)
        text_surf, text_rect = text_objects("OMEGA!", large_text, (210,208,224))
        text_rect.center = ((screen_width/2),(screen_height/2.75))
        screen.blit(text_surf, text_rect)

        top_score.print_prop(screen)

        button('PLAY', ((screen_width/2) - 50), 240, 100, 40,
              ((37,31,71), (108,100,153), (210,208,224)), game_loop)


def game_loop():
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)
    background = Background(BACKGROUND, [0,0])

    pygame.mouse.set_visible(False)

    #  list of every sprite
    all_sprites_list = pygame.sprite.Group()
    # list of each enemy in the game
    enemy_list = pygame.sprite.Group()
    # list of each bullet - rename projectile?
    bullet_list = pygame.sprite.Group()

    asteroid_list = pygame.sprite.Group()

    # --- Create the sprites
    num_of_enemies = 20

    # create all enemies
    for i in range(num_of_enemies):
        enemy = Enemy()

        # set a random location for the enemy
        # *maybe* in the future have them all start off screen
        enemy.rect.x = random.randrange(screen_width)
        enemy.rect.y = random.randrange(300)

        # Add the enemy to the appropriate lists of sprites
        enemy_list.add(enemy)
        all_sprites_list.add(enemy)

    #create game class

    # create a player
    player = Player()
    all_sprites_list.add(player)

    score = 0
    shots_fired = 0
    player.rect.y = 330
    ammo = int(num_of_enemies * 100)
    streak = 0
    misses = 0

    hud_items = pygame.sprite.Group()

    hud_score = Hud(570, 350, 120, 40, 'SCORE')
    hud_ammo = Hud(570, 300, 120, 40, 'AMMO')
    hud_multiplier = Hud(510, 350, 50, 40, '', 'x', True)
    hud_items.add(hud_score)
    hud_items.add(hud_ammo)

    # asteroid = Asteroid((60, 60), 20, 350, -40, 4)
    # asteroid2 = Asteroid((50, 50), 35, 250, -40)
    # asteroid3 = Asteroid((50, 50), 35, 100, -40, 1)
    # all_sprites_list.add(asteroid)
    # all_sprites_list.add(asteroid2)
    # all_sprites_list.add(asteroid3)
    # asteroid_list.add(asteroid)
    # asteroid_list.add(asteroid2)
    # asteroid_list.add(asteroid3)

    # -------- Main Program Loop -----------
    game_over = False
    while not game_over:
        multiplier = int(streak/2) or 1
        total_score = score * 100 or 0
        hud_ammo.prop = ammo
        hud_score.prop = total_score
        hud_multiplier.prop = multiplier

        # --- Event Processing
        for event in pygame.event.get():
            player_pos = (player.rect.x + 30, player.rect.y + 10)

            # print(event)

            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                game_over = True
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                can_fire = ammo > 0

                if can_fire and event.button == 1:
                    bullet = Bullet(player_pos)
                    # add the bullet to lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                    shots_fired += 1
                    ammo -= 1

                elif can_fire and event.button == 3:
                    bullet = Wobble_shot(player_pos)
                    # add the bullet to lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                    shots_fired += 1
                    ammo -= 1

                elif event.button == 2:
                    ammo += 30

                elif not can_fire:
                    print('you loose')
                    pygame.mixer.music.fadeout(1000)
                    message_display('YOU LOOSE OUT OF AMMO!!!', WHITE)

                    game_over = True


        # --- Game logic

        # call the update method on all the sprites
        all_sprites_list.update()

        player_hit_list = pygame.sprite.spritecollide(
            player, asteroid_list, False)

        if player_hit_list:
            pygame.mixer.music.fadeout(1000)
            message_display('YOU LOOSE HIT BY ASTEROID!!!', WHITE)

            game_over = True

        # calculate mechanics for each bullet
        for bullet in bullet_list:

            # see if bullet hit a enemy
            enemy_hit_list = pygame.sprite.spritecollide(
                bullet, enemy_list, False)

            # see if asteroid hit ship
            asteroid_hit_list = pygame.sprite.spritecollide(
                bullet, asteroid_list, False)

            for asteroid in asteroid_hit_list:
                asteroid.hp -= 3
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

            # for each enemy hit, remove the bullet and add to the score
            for enemy in enemy_hit_list:

                if not enemy.hit:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                    score += (1 * multiplier)
                    streak += 1
                    enemy.explode()

             # remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                streak = 0
                misses += 1

        # checking enemy list is empty ensures that the last explode() has completed ;)
        if not enemy_list:
            print('winner',shots_fired, score, total_score)
            pygame.mixer.music.fadeout(1000)
            if total_score > scores.top_score:
                scores.update_ts(total_score)

            if shots_fired <= num_of_enemies and not misses:
                message_display('PERFECT!! YOU WIN!! score: {}'
                    .format(str(total_score)), WHITE)
            elif ammo == 0:
                message_display('CLOSE ONE, YOU WIN!! score: {}'
                    .format(str(total_score)), WHITE)
            else:
                message_display('YOU WIN!!! total score: {}'
                    .format(str(total_score)), WHITE)
            game_over = True

        # clear the screen
        screen.fill(WHITE)
        # then background
        screen.blit(background.image, background.rect)

        # draw all the spites
        # draw hud items on top of background
        hud_ammo.print_prop(screen)
        hud_score.print_prop(screen)
        hud_multiplier.print_prop(screen)
        # asteroid.draw(screen)
        # followed by enemies
        all_sprites_list.draw(screen)
        # and finally player on top
        player.draw(screen)

        # update the screen
        pygame.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    start_loop()

pygame.quit()
quit()
