class Stats():
    """Статистика игрока"""

    def __init__(self):
        """Инициализация статистики"""

        self.Reset_stats()

        self.run_game = True

        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def Reset_stats(self):
        """Динамическое изменеие статистики в игре"""

        self.player_left = 3
        self.score = 0
