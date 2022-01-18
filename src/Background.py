#! python3.8 - background class for the game

import pygame

class Background:

    def __init__(self, image, topleft, speed, left_limit, right_limit, ifY = 1):
        """
        image: pygame image, topleft: list of the topleft position of the image,
        speed: the speed the image move, 
        left_limit: the left limit coordinate (x and y) of the image,
        right_limit: the right limit coordinate (x and y) of the image,
        ifY: if the image move in y direction (1 is yes, 0 is not)
        """
        self.__image = image
        self.__topleft = topleft
        self.__speed = speed
        self.__leftLimit = left_limit
        self.__rightLimit = right_limit
        self.__ifY = ifY


    def move(self, x, y):
        """move the picture"""

        if self.__topleft[0] >= self.__rightLimit[0] and self.__topleft[0] <= self.__leftLimit[0]:
            self.__topleft[0] += self.__speed * x
            self.__topleft[1] += self.__speed * y * self.__ifY
        elif self.__topleft[0] < self.__rightLimit[0]:
                self.__topleft[0] = self.__rightLimit[0]
                self.__topleft[1] = self.__rightLimit[1]
        elif self.__topleft[0] > self.__leftLimit[0]:
            self.__topleft[0] = self.__leftLimit[0]
            self.__topleft[1] = self.__leftLimit[1]


    def draw(self, screen):
        """draw the picture"""
        
        screen.blit(self.__image, self.__topleft)