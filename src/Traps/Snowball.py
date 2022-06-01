#! python3.8 - snowball class for the game

import pygame
from random import randint
pygame.mixer.init()


class Snowball:

    __img = pygame.image.load("../img/snowball.png")
    __sound = sound = pygame.mixer.Sound("../music/snowball_damage.wav")

    def __init__(self, slope):
        self.__speed = randint(1, 3) + 2
        self.__pos = [1100, -50]
        self.__slope = slope
        self.__rect = pygame.Rect(self.__pos[0] + 20, self.__pos[1] + 20, 60, 60)
        self.outOfScreen = False

    def update(self, player, x):
        """the method to run a snowball to player"""

        if self.__pos[0] >= -150:
            self.__pos[0] -= self.__speed - x
            self.__pos[1] -= (self.__speed - x) * self.__slope
            self.__rect.topleft = [self.__pos[0] + 20, self.__pos[1] + 20]
        else:
            self.outOfScreen = True

        if self.__rect.colliderect(player.rect):
            self.__sound.play()
            self.outOfScreen = True
            player.loseHp()

    def draw(self, screen):
        screen.blit(self.__img, self.__pos)
        # pygame.draw.rect(screen, (200, 200, 0), self.__rect)
