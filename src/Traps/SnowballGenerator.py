#! python3.8 - generate snowball  for the game

import pygame
from .Snowball import Snowball
from random import randint
pygame.mixer.init()


class SnowballGenerator:

    __sound = sound = pygame.mixer.Sound("../music/snowball_generator.wav")

    def __init__(self, slope):
        self.snowballList = []
        self.__slope = slope

    def update(self, player, x):
        """update the states of all snowball"""

        # add snowball to the list randomly
        if randint(1, 150) == 1:
            self.__sound.play()
            self.snowballList.append(Snowball(self.__slope))

        # keep the snowball going
        i = 0
        while i < len(self.snowballList):
            self.snowballList[i].update(player, x)
            if self.snowballList[i].outOfScreen:
                del self.snowballList[i]
                i -= 1
            i += 1

    def draw(self, screen):
        """draw all snowballs"""

        for sb in self.snowballList:
            sb.draw(screen)
