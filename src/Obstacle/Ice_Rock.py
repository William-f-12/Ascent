#! python3.8 - Obstacle: ice rock

import pygame
from src.Obstacle.ObsBase import ObsBase


class Ice_Rock(ObsBase):
    """use the image iceRock.png"""

    img = pygame.image.load("../img/iceRock.png")

    def init_rect(self, pos):
        """initialize the rect for ice rock"""

        return pygame.Rect(pos[0] + 10, pos[1] + 5, 80, 30)

    def reset_rect(self, pos):
        """update the position of rect"""

        return [pos[0] + 10, pos[1] + 5]
