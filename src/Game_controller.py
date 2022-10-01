#! python3.8 - game controller class for the game
# @project: Ascent
# @author:  William Lu :)

__author__ = "William Lu"

import sys
import pygame
from pygame import *
from Static_Value import StaticValue
from Character import Character
from Flyer import Flyer
# from Timer import Timer

SV = StaticValue()


class GameController:
    # display surface
    DISPLAYSURF = pygame.display.set_mode((SV.WINDOWWIDTH, SV.WINDOWHEIGHT))
    pygame.display.set_caption("Ascent")
    # UI resource
    __img_ui = pygame.image.load(SV.LOCATION + "UI.png")
    __heart = pygame.image.load(SV.LOCATION + "heart.png")

    def __init__(self):
        # variables use in game control
        self.__levelChose = None
        self.__CosList = None
        self.__ObsList = None
        # self.__timer = None
        self.__level = None
        self.__win = None

    def initLevel1(self):
        SV.setLevel1()
        self.__win = False
        # self.__timer = Timer()
        self.__level = SV.Level_1
        self.__ObsList = SV.Obs_list
        self.__CosList = SV.Co_list

    def startScreen(self):
        """the start screen for the game, make player choose level"""

        # image
        start_back = pygame.image.load(SV.LOCATION + "start_back.png")
        start = pygame.image.load(SV.LOCATION + "start.png")
        starting_cloud = Flyer(pygame.image.load(SV.LOCATION + "starting_cloud.png"),
                               387, 1088, -.5, 2)

        # music
        pygame.mixer.music.load("../music/starting.wav")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(-1, 0.0)
        button = pygame.mixer.Sound("../music/button.wav")

        while True:
            # event handler
            click = False
            pos = pygame.mouse.get_pos()
            for Event in pygame.event.get():
                if Event.type == QUIT:
                    terminate()
                elif Event.type == KEYDOWN:
                    if Event.key == K_ESCAPE:
                        terminate()
                elif Event.type == MOUSEBUTTONDOWN:
                    click = True

            # update status
            starting_cloud.move()
            if click:
                # play
                if 85 < pos[0] < 335 and 470 < pos[1] < 580:
                    button.play()
                    break
                # reset the level information
                if 950 < pos[0] < 1000 and 525 < pos[1] < 575:
                    with open("Saving.txt", "w") as f:
                        f.write("1")

            # display
            self.DISPLAYSURF.blit(start_back, (0, 0))
            starting_cloud.draw(self.DISPLAYSURF)
            self.DISPLAYSURF.blit(start, (40, 465))
            pygame.draw.rect(self.DISPLAYSURF, (150, 150, 50), pygame.Rect(950, 525, 50, 50))
            # pygame.draw.rect(self.DISPLAYSURF, (200, 200, 0), pygame.Rect(85, 470, 250, 110))
            pygame.display.update()
            SV.FPSCLOCK.tick(SV.FPS)

    def levelChooseScreen(self):
        """let players choose the level they unlocked"""

        # image
        choices = pygame.image.load(SV.LOCATION + "choices.png")
        level1_img = pygame.image.load(SV.LOCATION + "level1_img.png")
        level2_img = pygame.image.load(SV.LOCATION + "level2_img.png")
        level3_img = pygame.image.load(SV.LOCATION + "level3_img.png")
        lock = pygame.image.load(SV.LOCATION + "lock.png")

        # sound
        button = pygame.mixer.Sound("../music/button.wav")

        # read saving
        with open("Saving.txt") as f:
            max_level = int(f.read())  # this txt file should only contain a number for the max level reached

        while True:
            # event handler
            click = False
            pos = pygame.mouse.get_pos()
            for Event in pygame.event.get():
                if Event.type == QUIT:
                    terminate()
                elif Event.type == KEYDOWN:
                    if Event.key == K_ESCAPE:
                        terminate()
                elif Event.type == MOUSEBUTTONDOWN:
                    click = True

            # update status
            if click:
                if 950 < pos[0] < 1000 and 525 < pos[1] < 575:
                    terminate()
                elif max_level >= 1 and 50 < pos[0] < 350 and 75 < pos[1] < 475:
                    self.__levelChose = 1
                    button.play()
                    break
                elif max_level >= 2 and 400 < pos[0] < 700 and 75 < pos[1] < 475:
                    self.__levelChose = 2
                    button.play()
                    break
                elif max_level >= 3 and 750 < pos[0] < 1050 and 75 < pos[1] < 475:
                    self.__levelChose = 3
                    button.play()
                    break

            # display
            self.DISPLAYSURF.blit(choices, (0, 0))
            self.DISPLAYSURF.blit(level1_img, (50, 75))
            # pygame.draw.rect(self.DISPLAYSURF, (100, 100, 100), pygame.Rect(50, 75, 300, 400))
            self.DISPLAYSURF.blit(level2_img, (400, 75))
            # pygame.draw.rect(self.DISPLAYSURF, (150, 50, 100), pygame.Rect(400, 75, 300, 400))
            self.DISPLAYSURF.blit(level3_img, (750, 75))
            # pygame.draw.rect(self.DISPLAYSURF, (50, 150, 50), pygame.Rect(750, 75, 300, 400))
            if max_level < 2:
                self.DISPLAYSURF.blit(lock, (400, 75))
            if max_level < 3:
                self.DISPLAYSURF.blit(lock, (750, 75))
            pygame.draw.rect(self.DISPLAYSURF, (200, 100, 100), pygame.Rect(950, 525, 50, 50))
            pygame.display.update()
            SV.FPSCLOCK.tick(SV.FPS)

    def endScreen(self):
        """end screen fot the game, show win or lose"""

        # image
        topped = pygame.image.load(SV.LOCATION + "camp_reached.png")
        fall = pygame.image.load(SV.LOCATION + "fall.png")

        # music
        win_sound = pygame.mixer.Sound(SV.LOCATION + "../music/win.wav")
        fall_sound = pygame.mixer.Sound(SV.LOCATION + "../music/fall.wav")
        button = pygame.mixer.Sound("../music/button.wav")

        if self.__win:
            win_sound.play()
            # update the max level reached
            with open("Saving.txt") as f:
                current_level = int(f.read())
            if self.__levelChose == current_level:
                with open("Saving.txt", "w") as f:
                    f.write(str(min(current_level + 1, 3)))
        else:
            fall_sound.play()

        while True:
            # event handler
            click = False
            pos = pygame.mouse.get_pos()
            for Event in pygame.event.get():
                if Event.type == QUIT:
                    terminate()
                elif Event.type == KEYDOWN:
                    if Event.key == K_ESCAPE:
                        terminate()
                elif Event.type == MOUSEBUTTONDOWN:
                    click = True

            # update status
            if click:
                if 355 < pos[0] < 720 and 435 < pos[1] < 550:
                    button.play()
                    break

            # display
            if self.__win:
                self.DISPLAYSURF.blit(topped, (0, 0))
            else:
                self.DISPLAYSURF.blit(fall, (0, 0))
            # pygame.draw.rect(self.DISPLAYSURF, (200, 200, 0), pygame.Rect(355, 435, 365, 115))
            pygame.display.update()
            SV.FPSCLOCK.tick(SV.FPS)

    def draw_UI(self, screen, gemNum, hp):
        """display information to players"""

        screen.blit(self.__img_ui, (850, 470))
        for i in range(hp):
            screen.blit(self.__heart, (870 + i * 30, 482 + i * 10))
        point = SV.FONT.render(str(gemNum), True, (250, 250, 250))
        screen.blit(point, (882, 525))

    # run the game:
    def run(self):
        """to start the whole game!"""

        # initialize level
        boy = Character()
        if self.__levelChose == 1:
            self.initLevel1()
        if self.__levelChose == 2:
            self.initLevel1()
        if self.__levelChose == 3:
            self.initLevel1()

        # music
        pygame.mixer.music.load("../music/ArticBeat.wav")
        pygame.mixer.music.set_volume(.15)
        pygame.mixer.music.play(-1, 0.0)

        while True:
            # event handler
            for Event in pygame.event.get():
                if Event.type == QUIT:
                    terminate()
                elif Event.type == KEYDOWN:
                    if Event.key == K_ESCAPE:
                        terminate()
                    if Event.key == K_LEFT or Event.key == K_a:
                        boy.left = True
                    elif Event.key == K_RIGHT or Event.key == K_d:
                        boy.right = True
                    elif Event.key == K_SPACE or Event.key == K_w or Event.key == K_UP:
                        boy.jump = True
                elif Event.type == KEYUP:
                    if Event.key == K_LEFT or Event.key == K_a:
                        boy.left = False
                    elif Event.key == K_RIGHT or Event.key == K_d:
                        boy.right = False
                    elif Event.key == K_SPACE or Event.key == K_w or Event.key == K_UP:
                        boy.jump = False

            # check winning
            if boy.hp <= 0:
                pygame.mixer.music.unload()
                break
            elif boy.rect.colliderect(self.__level.endpoint.rect):
                self.__win = True
                pygame.mixer.music.unload()
                break

            # update status
            # self.__timer.count()
            boy.update(self.__level.ground(boy.rect.midbottom[0]),
                       self.__ObsList.all, self.__CosList.all)
            self.__level.update(boy)

            # draw all images
            self.DISPLAYSURF.fill((0, 0, 50))
            self.__level.draw(self.DISPLAYSURF)
            SV.draw_obs(self.DISPLAYSURF)
            SV.draw_co(self.DISPLAYSURF)
            boy.draw(self.DISPLAYSURF)
            self.__level.Snowballs.draw(self.DISPLAYSURF)
            self.draw_UI(self.DISPLAYSURF, boy.coNums, boy.hp)
            # self.__level.endpoint.draw(self.DISPLAYSURF)
            pygame.display.update()
            SV.FPSCLOCK.tick(SV.FPS)

    def play(self):
        """handle the whole game"""

        self.startScreen()
        while True:
            self.levelChooseScreen()
            self.run()
            self.endScreen()


def terminate():
    pygame.quit()
    sys.exit()


# main
def main():
    game_controller = GameController()
    game_controller.play()


if __name__ == "__main__":
    main()
