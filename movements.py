import pygame
import sys
import time

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

def update_bullets(screen, enemys, bullets):
    """обновление позиции снаряда"""

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)

    if len(enemys) == 0:
        bullets.empty()
        spawn_enemys(screen, enemys)

def player_kill(stats, screen, Player, enemys, bullets):
    """Столкновение игрока и противника"""

    stats.player_left -= 1

    enemys.empty()

    bullets.empty()

    spawn_enemys(screen, enemys)

    Player.create_player()

    time.sleep(1) #После смерти игрока, юудет задержка в 1 секунду

def update_enm(stats, screen, Player, enemys, bullets):

    """Обновление позиции противника"""
    enemys.update()

    if pygame.sprite.spritecollideany(Player, enemys):
        player_kill(stats, screen, Player, enemys, bullets)
    enemys_check(stats, screen, Player, enemys, bullets)

def enemys_check(stats, screen, Player, enemys, bullets):
    """Проверка, на край экрана (если противник дошёл до края)"""

    screen_rect = screen.get_rect()

    for Enm in enemys.sprites():
        if Enm.rect.bottom >= screen_rect.bottom:
            player_kill(stats, screen, Player, enemys, bullets)
            break


def spawn_enemys(screen, enemys):

    """Спавн противника"""

    """Тут же будет расчёт, сколько противников поместится в ширину и в высоту. Так же можно уменьшать и увеличивать высоту волны"""

    enm = Enm(screen)

    enm_width = enm.rect.width

    number_enm_x = int((800 - 2 * enm_width) / enm_width) #Ищем сколько противников поместится в ширину

    enm_height = enm.rect.height

    number_enm_y = int((800 - 100 - 2 * enm_height) / enm_height)

    """Количество полос в волне изменятеся строкой ниже. Меняйте значение 5 на большее чтобы сделать меньше полос"""

    for row_num in range(number_enm_y - 5):

        for enm_nums in range(number_enm_x):
            enm = Enm(screen)
            enm.x = enm_width + (enm_width * enm_nums)
            enm.y = enm_height + (enm_height * row_num)
            enm.rect.x = enm.x
            enm.rect.y = enm.rect.height + (enm.rect.height * row_num)

            enemys.add(enm)