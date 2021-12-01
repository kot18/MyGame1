import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, Player):
        """снаряд"""

        super(Bullet, self).__init__()

        self.screen = screen

        self.rect = pygame.Rect(0, 0, 2, 12)

        self.color = 0, 0, 0

        self.speed = 3

        self.rect.centerx = Player.rect.centerx

        self.rect.top = Player.rect.top

        self.y = float(self.rect.y)

    def update(self):
        """Перемещение снаряда"""

        self.y -= self.speed

        self.rect.y = self.y

    def draw_bullet(self):
        """Рисуем снаряд"""

        pygame.draw.rect(self.screen, self.color, self.rect)