#! python3.8 - flyer class for the game


class Flyer:

    def __init__(self, image, y, x, speed, num):
        self.__image = image
        self.__y = y
        self.__x = x
        self.__speed = speed
        self.__num = num
        self.__toplefts = []
        for i in range(num):
            if speed > 0:
                self.__toplefts.append([x + i * image.get_width(), y])
            else:
                self.__toplefts.append([x - i * image.get_width(), y])

    def move(self, *args):
        """let the flyer moves"""

        for i in range(self.__num):
            self.__toplefts[i][0] -= self.__speed

        if self.__toplefts[0][0] <= self.__x and self.__speed > 0:
            new_topleft = [self.__toplefts[-1][0] + self.__image.get_width(), self.__y]
            self.__toplefts.append(new_topleft)
            del self.__toplefts[0]
        elif self.__toplefts[0][0] >= self.__x and self.__speed < 0:
            new_topleft = [self.__toplefts[-1][0] - self.__image.get_width(), self.__y]
            self.__toplefts.append(new_topleft)
            del self.__toplefts[0]

    def draw(self, screen):
        """draw the flyer"""

        for topleft in self.__toplefts:
            screen.blit(self.__image, topleft)
