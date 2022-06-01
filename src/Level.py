#! python3.8 - game map for level 1

from Traps.SnowballGenerator import SnowballGenerator


class Level:

    def __init__(self, slope, ground_b, endpoint, *pics):
        self.a = slope
        self.b = ground_b
        self.endpoint = endpoint
        self.Snowballs = SnowballGenerator(slope)
        self.__pics = pics
        self.__x = 0
        self.__y = 0

    def update(self, character):
        self.__x = character.img_correct()
        self.__y = self.a * self.__x
        self.Snowballs.update(character, self.__x)
        self.endpoint.move(self.__x, self.__y)
        for pic in self.__pics:
            pic.move(self.__x, self.__y)

    def draw(self, DISPLAYSURF):
        for pic in self.__pics:
            pic.draw(DISPLAYSURF)

    def ground(self, x):
        y = self.a * x + self.b
        return y
