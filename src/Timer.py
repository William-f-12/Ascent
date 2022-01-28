#! python3.8 - the timer class for the game


class Timer:

    def __init__(self):
        self.__time = 0

    def count(self):
        """increase the timer by 1, but no more than 100000000"""

        self.__time += 1
        if self.__time == 100000000:
            self.__time = 0

    def Func1(self):
        """return true or false, according to if the time mod 10"""

        if self.__time % 10 == 0:
            return True
        else:
            return False
