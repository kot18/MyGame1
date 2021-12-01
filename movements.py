import pygame
import sys

from bullet import Bullet
from enemy import Enm

def events(screen, Player, bullets):
    "обработка событий"

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                Player.mright = True

            elif event.key == pygame.K_LEFT:
                Player.mleft = True

            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, Player)

                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT:
                Player.mright = False

            elif event.key == pygame.K_LEFT:
                Player.mleft = False

def update(bg_color, screen, Player, enemys, bullets):
    """Обновление экрана"""

    screen.fill(bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    Player.visual_player()

    enemys.draw(screen)

    pygame.display.flip()

def update_bullets(bullets):
    """обновление позиции снаряда"""

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_enm(enemys):
    enemys.update()

def spawn_enemys(screen, enemys):

    enm = Enm(screen)

    enm_width = enm.rect.width

    number_enm_x = int((800 - 2 * enm_width) / enm_width) #ищем сколько противников поместится в ширину

    enm_height = enm.rect.height

    number_enm_y = int((800 - 100 - 2 * enm_height) / enm_height)

    for row_num in range(number_enm_y - 5):

        for enm_nums in range(number_enm_x):
            enm = Enm(screen)
            enm.x = enm_width + (enm_width * enm_nums)
            enm.y = enm_height + (enm_height * row_num)
            enm.rect.x = enm.x
            enm.rect.y = enm.rect.height + (enm.rect.height * row_num)

            enemys.add(enm)