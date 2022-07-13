import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores():
    """вывод игровой информации"""
    def __init__(self, screen: pygame.Surface, stats):
        """инциализируем подсчет очков"""
        self.score_img = None
        self.screen: pygame.Surface = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (245, 200, 111)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        """преобразовавыват текст счета в графиское изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (8, 12, 23))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 30
        self.score_rect.top = 20

    def image_high_score(self):
        """преобразует рекорд в крафическое изображжение"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (8, 12, 23))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_guns(self):
        """коллличесво жизней"""
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = self.screen.get_rect().right - (60 + gun_number * gun.rect.width)
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)

