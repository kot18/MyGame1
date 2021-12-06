import pygame
import movements

from Player import player
from pygame.sprite import Group
from stats import Stats
from scores import  Scores

def start_game():

    pygame.init()

    screen = pygame.display.set_mode((800, 900))

    pygame.display.set_caption("Space Invaders")

    bg_color = (224, 255, 255)

    Player = player(screen)

    bullets = Group()

    enemys = Group()

    movements.spawn_enemys(screen, enemys)

    stats = Stats()

    sc = Scores(screen, stats)

    while True:

        movements.events(screen, Player, bullets)

        if stats.run_game:

            Player.update_position_player()

            movements.update(bg_color, screen, stats, sc, Player, enemys, bullets)

            movements.update_bullets(screen, stats, sc, enemys, bullets)

            movements.update_enm(stats, screen, sc, Player, enemys, bullets)

start_game()