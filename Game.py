import pygame
import movements

from Player import player
from pygame.sprite import Group

def start_game():

    pygame.init()

    screen = pygame.display.set_mode((800, 900))

    pygame.display.set_caption("Space Invaders")

    bg_color = (224, 255, 255)

    Player = player(screen)

    bullets = Group()

    enemys = Group()

    movements.spawn_enemys(screen, enemys)

    while True:

        movements.events(screen, Player, bullets)

        Player.update_position_player()

        movements.update(bg_color, screen, Player, enemys, bullets)

        movements.update_bullets(bullets)

        movements.update_enm(enemys)

start_game()