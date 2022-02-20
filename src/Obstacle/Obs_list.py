#! python3.8 - the class of a list of all obstacles

class Obs_list:

    def __init__(self, *obs):
        self.__Obs_list = obs

    def move(self, x, y):
        for obs in self.__Obs_list:
            obs.move(x, y)

    def draw(self, DISPLAYSURF):
        for obs in self.__Obs_list:
            obs.draw(DISPLAYSURF)

    @property
    def all(self):
        return self.__Obs_list
