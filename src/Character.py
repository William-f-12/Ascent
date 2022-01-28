#! python3.8 - class for character in the game

import pygame
from Static_Value import StaticValue

SV = StaticValue()


class Character:

    def __init__(self):
        # private:
        self.__img = {"Stand": pygame.image.load(SV.LOCATION + "character.png"),
                      }
        self.__rect = pygame.Rect(528, 350, 32, 32)
        self.__speed = 2
        self.__yspeed = 0
        self.__jumpMax = 20
        self.__jumpTime = self.__jumpMax
        self.__left = False
        self.__right = False
        self.__jump = False
        self.__isStand = False
        self.__isLeft = False
        self.__status = "Stand"
        # status: Stand, Run, Jump

    def update(self, obstacle):
        self.checkStand(obstacle)
        # move left or right
        if self.__left:
            self.__isLeft = True
            self.__rect.left -= self.__speed
        if self.__right:
            self.__isLeft = False
            self.__rect.left += self.__speed

        # jump and fall
        if self.__jump and (self.__isStand or self.__jumpTime > 0):
            self.__yspeed = -8
            self.__rect.top += self.__yspeed
            self.__isStand = False
        if not self.__isStand:
            if self.__jumpTime <= 0 or not self.__jump:
                self.__yspeed += 1
                self.__yspeed = min(self.__yspeed, 6)
                self.__rect.top += self.__yspeed
                self.__jumpTime = 0
            self.__jumpTime -= 1
            self.checkStand(obstacle)
        if self.__isStand and (self.__jumpTime != self.__jumpMax or self.__yspeed != 0):
            self.__jumpTime = self.__jumpMax
            self.__yspeed = 0

    def img_correct(self):
        cor_x = 528 - self.__rect.left
        self.__rect.left = 528
        return cor_x

    def draw(self, DISPLAYSURF):
        if self.__isLeft:
            DISPLAYSURF.blit(pygame.transform.flip(self.__img[self.__status], True, False), self.__rect)
        else:
            DISPLAYSURF.blit(self.__img[self.__status], self.__rect)

    def checkStand(self, obstacle_top):
        if self.__rect.bottom == obstacle_top:
            self.__isStand = True
        elif self.__rect.bottom > obstacle_top:
            self.__isStand = True
            self.__rect.bottom = obstacle_top
        else:
            self.__isStand = False

    @property
    def rect(self):
        return self.__rect

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value: bool):
        if value:
            self.__left = True
        else:
            self.__left = False

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value: bool):
        if value:
            self.__right = True
        else:
            self.__right = False

    @property
    def jump(self):
        return self.__jump

    @jump.setter
    def jump(self, value: bool):
        if value:
            self.__jump = True
        else:
            self.__jump = False
