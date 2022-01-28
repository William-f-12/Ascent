#! python3.8 - obstacle class for the game

import pygame


class Obstacle:

    def __init__(self, image, rect):
        self.__image = image
        self.__rect = rect
