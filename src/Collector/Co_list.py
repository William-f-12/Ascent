#! python3.8 - the class of a list of all obstacles


class Co_list:

    def __init__(self, *co):
        self.__Co_list = list(co)

    def move(self, x, y):
        for co in self.__Co_list:
            co.move(x, y)

    def draw(self, *args):
        # obs will be drawn by other part of program
        # this function is just needed to be here though it does nothing
        pass

    def remove(self, rev_co):
        self.__Co_list.remove(rev_co)

    @property
    def all(self):
        return self.__Co_list
