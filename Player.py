import pygame
from pygame.sprite import Sprite

class player(Sprite):

    def __init__(self, screen):
        """Игрок"""

        super(player,self).__init__()

        self.screen = screen
        self.image = pygame.image.load('assets/player.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.mright = False
        self.mleft = False

    def visual_player(self):

        self.screen.blit(self.image, self.rect)

    def update_position_player(self):
        """Обновление позиции пушки"""

        if self.mright == True and self.rect.right < self.screen_rect.right:
            self.center += 1.1

        if self.mleft == True and self.rect.left > 0:
            self.center -= 1.1

        self.rect.centerx = self.center

    def create_player(self):
        """Спавн игрока в нулевой поциции"""

        self.center = self.screen_rect.centerx