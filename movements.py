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

def update(bg_color, screen, stats, sc, Player, enemys, bullets):
    """Обновление экрана"""

    screen.fill(bg_color)

    sc.shovw_score()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    Player.visual_player()

    enemys.draw(screen)

    pygame.display.flip()

def update_bullets(screen, stats, sc, enemys, bullets):
    """обновление позиции снаряда"""

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)

    if collisions:

        for enemys in collisions.values():
            stats.score += 5 * len(enemys)

        stats.score += 5
        sc.image_score()

        check_high_score(stats, sc)

        sc.image_players()

    if len(enemys) == 0:
        bullets.empty()
        spawn_enemys(screen, enemys)

def player_kill(stats, screen, sc, Player, enemys, bullets):
    """Столкновение игрока и противника"""

    if stats.player_left > 0:


        stats.player_left -= 1

        sc.image_players()

        enemys.empty()

        bullets.empty()

        spawn_enemys(screen, enemys)

        Player.create_player()

        time.sleep(1) #После смерти игрока, юудет задержка в 1 секунду

    else:
        stats.run_game = False
        sys.exit()

def update_enm(stats, screen, sc, Player, enemys, bullets):

    """Обновление позиции противника"""
    enemys.update()

    if pygame.sprite.spritecollideany(Player, enemys):
        player_kill(stats, screen, sc, Player, enemys, bullets)
    enemys_check(stats, screen, sc, Player, enemys, bullets)

def enemys_check(stats, screen, sc, Player, enemys, bullets):
    """Проверка, на край экрана (если противник дошёл до края)"""

    screen_rect = screen.get_rect()

    for Enm in enemys.sprites():
        if Enm.rect.bottom >= screen_rect.bottom:
            player_kill(stats, screen, sc, Player, enemys, bullets)
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

def check_high_score(stats, sc):
    """Проверка новых рекордов"""

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()

        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))