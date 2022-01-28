#! python3.8 - game map for level 1

import pygame


class Level:

    def __init__(self, ground_a, ground_b, *pics):
        self.a = ground_a
        self.b = ground_b
        self.__pics = pics

    def draw(self, DISPLAYSURF, character):
        x = character.img_correct()
        y = self.ground(x) - self.b
        for pic in self.__pics:
            pic.move(x, y)
            pic.draw(DISPLAYSURF)

    def ground(self, x):
        y = self.a * x + self.b
        return y
