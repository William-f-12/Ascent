#! python3.8 - Collector: gem

import pygame
from src.Collector.CoBase import CoBase
pygame.mixer.init()


class Gem(CoBase):
    """use the image gem.png"""

    img = pygame.image.load("../img/gem.png")
    sound = pygame.mixer.Sound("../music/gem_sound.wav")

    def init_rect(self, pos):
        """initialize the rect for gem"""

        return pygame.Rect(pos[0], pos[1], 50, 50)

    def init_point(self):
        """set the point of gem: 10"""

        return 1
