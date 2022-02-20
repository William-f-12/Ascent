#! python3.8 - parent class for collectors

import abc


class CoBase(metaclass=abc.ABCMeta):

    def __init__(self, image, pos):
        self.__image = image
        self.__pos = pos

    def draw(self, DISPLAYSURF):
        DISPLAYSURF.blit(self.__image, self.__pos)