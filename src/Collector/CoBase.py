#! python3.8 - parent class for collectors

import abc


class CoBase:

    def __init__(self, image, pos, leftLimit, rightLimit):
        self.__image = image
        self.__pos = pos
        self.__leftLimit = leftLimit
        self.__rightLimit = rightLimit
        self.__rect = self.init_rect(pos)
        self.__point = self.init_point()

    def move(self, x, y):
        """move the picture"""

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

    @abc.abstractmethod
    def init_rect(self, pos):
        """set a rect for the collector"""
        pass

    @abc.abstractmethod
    def init_point(self):
        """set the point for the collector"""
        pass

    @property
    def image(self):
        return self.__image

    @property
    def pos(self):
        return self.__pos

    @property
    def rect(self):
        return self.__rect

    @property
    def point(self):
        return self.__point
