#! python3.8 - static value class for the game

import pygame
from Background import Background
from Flyer import Flyer
from Level import Level

class StaticValue:

    def __init__(self):
        # public static:
        self.LOCATION = r"img/"
        self.WINDOWWIDTH = 1088
        self.WINDOWHEIGHT = 608
        self.FPS = 60 # frame per second
        self.FPSCLOCK = pygame.time.Clock()

        ## level 1
        # - background
        image = pygame.image.load(self.LOCATION + "background.png")
        self.L1_BACKGROUND = Background(image,[0, 0], 0.5, [0, 0], [-1088, 0], 0)
        # - flyer: cloud
        image = pygame.image.load(self.LOCATION + "cloud.png")
        self.L1_COULD = Flyer(image, 0, 1088, -1, 3)
        # - frontground
        image = pygame.image.load(self.LOCATION + "frontground.png")
        self.L1_FRONTGROUND = Background(image, [0, -1216], 1, [0, -1216], [-2176, -259])
        # - level
        self.Level_1 = Level(-.44, 520, self.L1_BACKGROUND, self.L1_COULD, self.L1_FRONTGROUND)