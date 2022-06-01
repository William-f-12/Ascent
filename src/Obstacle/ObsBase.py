#! python3.8 - parent class for obstacle in the game

import abc


class ObsBase(metaclass=abc.ABCMeta):

    img = None

    def __init__(self, pos, leftLimit, rightLimit):
        self.__pos = pos
        self.__leftLimit = leftLimit
        self.__rightLimit = rightLimit
        self.__rect = self.init_rect(pos)

    def move(self, x, y):
        """move the picture"""

        if self.__rightLimit[0] <= self.__pos[0] <= self.__leftLimit[0]:
            self.__pos[0] += x
            self.__pos[1] += y
            self.__rect.topleft = self.reset_rect(self.__pos)
        elif self.__pos[0] < self.__rightLimit[0]:
            self.__pos[0] = self.__rightLimit[0]
            self.__pos[1] = self.__rightLimit[1]
        elif self.__pos[0] > self.__leftLimit[0]:
            self.__pos[0] = self.__leftLimit[0]
            self.__pos[1] = self.__leftLimit[1]

    @abc.abstractmethod
    def init_rect(self, pos):
        """set a rect for the obstacle"""

        pass

    @abc.abstractmethod
    def reset_rect(self, pos):
        """update the rect position"""

        pass

    @property
    def pos(self):
        return self.__pos

    @property
    def rect(self):
        return self.__rect
