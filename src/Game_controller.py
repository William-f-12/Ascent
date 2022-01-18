#! python3.8 - game controller class for the game
#  the main file to run

import pygame, sys
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
        self.__tiemr = Timer()
        self.__level = SV.Level_1


    # public:
    def run(self):
        """to start the whole game!"""

        ## music
        pygame.mixer.music.load("./music/ArticBeat.wav")
        pygame.mixer.music.set_volume(.15)
        pygame.mixer.music.play(-1,0.0)


        while True:
             ## event handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.__terminate()
                    if (event.key == K_LEFT or event.key == K_a):
                        self.__boy.left = True
                    elif (event.key == K_RIGHT or event.key == K_d):
                        self.__boy.right = True
                    elif (event.key == K_SPACE or event.key == K_w or event.key == K_UP):
                        self.__boy.jump = True
                elif event.type == KEYUP:
                    if (event.key == K_LEFT or event.key == K_a):
                        self.__boy.left = False
                    elif (event.key == K_RIGHT or event.key == K_d):
                        self.__boy.right = False
                    elif (event.key == K_SPACE or event.key == K_w or event.key == K_UP):
                        self.__boy.jump = False


            ## update status
            self.__tiemr.count()
            self.__boy.update(self.__level.ground(self.__boy.rect.midbottom[0]))


            ## draw all images
            self.DISPLAYSURF.fill((0,0,50))
            self.__level.draw(self.DISPLAYSURF, self.__boy)
            self.__boy.draw(self.DISPLAYSURF)
            pygame.display.update()
            SV.FPSCLOCK.tick(SV.FPS)


    # private:
    def __terminate(self):
        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    game_controller = GameController()
    game_controller.run()