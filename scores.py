import pygame.font
from Player import player
from pygame.sprite import Group

class Scores():
    """Вывод рекорда"""

    def __init__(self, screen, stats):
        """инициалтзируем подсчёт очнов"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24)
        self.image_score()

        self.image_high_score()

        self.image_players()

    def image_score(self):
        """Приобразовывает текст счёта в граыическое изображение"""

        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (224, 255, 255))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """Преобразует рекорд в графику"""

        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (224, 255, 255))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top + 20

    def image_players(self):
        """количество жизней"""

        self.players = Group()

        for player_number in range(self.stats.player_left):
            one = player(self.screen)
            one.rect.x = 15 + player_number * one.rect.width
            one.rect.y = 20

            self.players.add(one)


    def shovw_score(self):
        """Вывод на экран счёта"""

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

        self.players.draw(self.screen)


