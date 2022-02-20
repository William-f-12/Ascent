#! python3.8 - game controller class for the game
# @project: Ascent
# @author:  William Lu

__author__ = "William Lu"

import sys
import pygame
from pygame import *
from Static_Value import StaticValue
from Character import Character
from Timer import Timer

pygame.init()
SV = StaticValue()


class GameController:

    def __init__(self):
        # public:
        self.DISPLAYSURF = pygame.display.set_mode((SV.WINDOWWIDTH, SV.WINDOWHEIGHT))
        pygame.display.set_caption("Ascent")

        # private:
        self.__boy = Character()
        self.__timer = Timer()
        self.__level = SV.Level_1
        self.__ObsList = SV.Obs_list

    # public:
    def run(self):
        """to start the whole game!"""

        # music
        pygame.mixer.music.load("./music/ArticBeat.wav")
        pygame.mixer.music.set_volume(.15)
        pygame.mixer.music.play(-1, 0.0)

        while True:
            # event handler
            for Event in pygame.event.get():
                if Event.type == QUIT:
                    terminate()
                elif Event.type == KEYDOWN:
                    # if Event.key == K_ESCAPE:
                    #     terminate()
                    if Event.key == K_LEFT or Event.key == K_a:
                        self.__boy.left = True
                    elif Event.key == K_RIGHT or Event.key == K_d:
                        self.__boy.right = True
                    elif Event.key == K_SPACE or Event.key == K_w or Event.key == K_UP:
                        self.__boy.jump = True
                elif Event.type == KEYUP:
                    if Event.key == K_LEFT or Event.key == K_a:
                        self.__boy.left = False
                    elif Event.key == K_RIGHT or Event.key == K_d:
                        self.__boy.right = False
                    elif Event.key == K_SPACE or Event.key == K_w or Event.key == K_UP:
                        self.__boy.jump = False

            # update status
            self.__timer.count()
            self.__boy.update(self.__level.ground(self.__boy.rect.midbottom[0]), self.__ObsList.all)

            # draw all images
            self.DISPLAYSURF.fill((0, 0, 50))
            self.__level.draw(self.DISPLAYSURF, self.__boy)
            self.__boy.draw(self.DISPLAYSURF)
            pygame.display.update()
            SV.FPSCLOCK.tick(SV.FPS)


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_controller = GameController()
    game_controller.run()
