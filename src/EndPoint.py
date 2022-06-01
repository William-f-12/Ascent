# python3.8 - the endpoint class for the game

import pygame


class EndPoint:

    def __init__(self, pos, l_limit, r_limit):
        self.__pos = pos
        self.__rect = pygame.Rect(pos[0], pos[1], 42, 42)
        self.__leftLimit = l_limit
        self.__rightLimit = r_limit

    def move(self, x, y):
        if self.__rightLimit[0] <= self.__pos[0] <= self.__leftLimit[0]:
            self.__pos[0] += x
            self.__pos[1] += y
            self.__rect.topleft = self.__pos
        elif self.__pos[0] < self.__rightLimit[0]:
            self.__pos[0] = self.__rightLimit[0]
            self.__pos[1] = self.__rightLimit[1]
        elif self.__pos[0] > self.__leftLimit[0]:
            self.__pos[0] = self.__leftLimit[0]
            self.__pos[1] = self.__leftLimit[1]

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 0, 200), self.__rect)

    @property
    def rect(self):
        return self.__rect
