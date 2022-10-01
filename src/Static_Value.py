#! python3.8 - static value class for the game

import pygame
from Background import Background
from Flyer import Flyer
from Level import Level
from EndPoint import EndPoint
from Obstacle import *
from Collector import *


class StaticValue:

    def __init__(self):
        pygame.init()

        # general member:
        self.LOCATION = r"../img/"
        self.WINDOWWIDTH = 1088
        self.WINDOWHEIGHT = 608
        self.FONT = pygame.font.Font('freesansbold.ttf', 20)
        self.FPS = 60  # frame per second
        self.FPSCLOCK = pygame.time.Clock()

        # level 1
        self.L1_BACKGROUND = None
        self.endpoint = None
        self.Level_1 = None
        self.Co_list = None
        self.Obs_list = None
        self.L1_FRONTGROUND = None
        self.L1_COULD = None
        # self.setLevel1()

    def setLevel1(self):
        # level 1
        # - background
        self.L1_BACKGROUND = Background(pygame.image.load(self.LOCATION + "background.png"),
                                        [0, 0], 0.5, (0, 0), (-1088, 0), 0)
        # - endpoint
        self.endpoint = EndPoint([2700, -720], (2700, -720), (524, 237))
        # - flyer: cloud
        self.L1_COULD = Flyer(pygame.image.load(self.LOCATION + "cloud.png"),
                              0, 1088, -1, 3)
        # - frontground
        self.L1_FRONTGROUND = Background(pygame.image.load(self.LOCATION + "frontground.png"),
                                         [0, -1216], 1, (0, -1216), (-2176, -259))
        # - all traps

        # - all Obstacles
        self.Obs_list = Obs_list(Ice_Rock([600, 120], (600, 120), (-1576, 1077)),
                                 Ice_Rock([1100, -120], (1100, -120), (-1076, 837)),
                                 Ice_Rock([900, -200], (900, -200), (-1276, 757)),
                                 Ice_Rock([1300, -300], (1300, -300), (-876, 657)),
                                 Ice_Rock([1550, -250], (1550, -250), (-626, 707)),
                                 Ice_Rock([1700, -400], (1700, -400), (-476, 557)),
                                 Ice_Rock([1800, -500], (1800, -500), (-376, 457)),
                                 Ice_Rock([2000, -500], (2000, -500), (-176, 457)),
                                 Ice_Rock([2200, -700], (2200, -700), (24, 257)),
                                 Ice_Rock([2300, -800], (2300, -800), (124, 157)), )
        # - all collectors
        self.Co_list = Co_list(Gem([1000, 10], (1000, 10), (-1176, 967)),
                               Gem([925, -250], (925, -250), (-1251, 707)),
                               Gem([625, 70], (625, 70), (-1551, 1027)),
                               Gem([1325, -350], (1325, -350), (-851, 607)),
                               Gem([2325, -850], (2325, -850), (149, 107)), )
        # - level
        self.Level_1 = Level(-.44, 520, self.endpoint,
                             self.L1_BACKGROUND, self.L1_COULD, self.L1_FRONTGROUND, self.Obs_list, self.Co_list)

    def draw_obs(self, screen):  # this class here is in order to save some memory space
        """draw all obstacles"""

        for obs in self.Obs_list.all:
            screen.blit(obs.img, obs.pos)
            # pygame.draw.rect(screen, (0, 0, 0), obs.rect)

    def draw_co(self, screen):  # this class here is in order to save some memory space
        """draw all collectors"""

        for co in self.Co_list.all:
            screen.blit(co.img, co.pos)
            # pygame.draw.rect(screen, (0, 200, 0), co.rect)
