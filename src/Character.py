#! python3.8 - class for character in the game

import pygame
from Static_Value import StaticValue

SV = StaticValue()


class Character:

    __img = {"Stand": pygame.image.load(SV.LOCATION + "character_stand.png"),
             "Run": pygame.image.load(SV.LOCATION + "character_stand.png"),
             "Jump": pygame.image.load(SV.LOCATION + "character_stand.png"),
             "Fall": pygame.image.load(SV.LOCATION + "character_stand.png"), }

    def __init__(self):
        self.__rect = pygame.Rect(528, 350, 42, 42)
        self.__speed = 2
        self.__yspeed = 0
        self.__jumpMax = 20
        self.__jumpTime = 20
        self.__left = False
        self.__right = False
        self.__jump = False
        self.__isStand = False
        self.__isLeft = False
        self.__status = "Stand"  # status: Stand, Run, Jump, Fall
        self.__coNums = 0
        self.__hp = 3

    def update(self, obstacle, obs_list, cos_list):
        """
        update the character state in the game
        this function is very complex, I don't even want to explain it
        """

        # check if the character is standing first
        self.checkStand(obstacle, obs_list)
        self.__status = "Stand"

        # move left or right
        if self.__left:
            self.__status = "Run"
            self.__isLeft = True
            self.__rect.left -= self.__speed
        if self.__right:
            self.__status = "Run"
            self.__isLeft = False
            self.__rect.left += self.__speed

        # jump and fall
        if self.__jump and (self.__isStand or self.__jumpTime > 0):
            self.__status = "Jump"
            self.__yspeed = -8
            self.__rect.top += self.__yspeed
            self.__isStand = False
        if not self.__isStand:
            if self.__jumpTime <= 0 or not self.__jump:
                self.__status = "Fall"
                self.__yspeed += 1
                self.__yspeed = min(self.__yspeed, 6)
                self.__rect.top += self.__yspeed
                self.__jumpTime = 0
            self.__jumpTime -= 1
            self.checkStand(obstacle, obs_list)
        if self.__isStand and (self.__jumpTime != self.__jumpMax or self.__yspeed != 0):
            self.__jumpTime = self.__jumpMax
            self.__yspeed = 0

        # check character's interaction with obstacles
        for obs in obs_list:
            if self.__rect.colliderect(obs.rect):
                if self.__rect.centery < obs.rect.top:
                    self.__rect.bottom = obs.rect.top
                elif self.__rect.centery > obs.rect.bottom:
                    self.rect.top = obs.rect.bottom
                    self.__jumpTime = 0
                    self.__yspeed = 0
                    if self.__isStand:
                        self.__right = False
                        self.__rect.left -= self.__speed
                elif self.__rect.centerx < obs.rect.left:
                    self.__rect.right = obs.rect.left
                elif self.__rect.centerx > obs.rect.right:
                    self.__rect.left = obs.rect.right
                break

        # check and collect collectors
        for co in cos_list:
            if self.__rect.colliderect(co.rect):
                cos_list.remove(co)
                co.sound.play()
                self.__coNums += co.point

    def img_correct(self):
        cor_x = 528 - self.__rect.left
        self.__rect.left = 528
        return cor_x

    def draw(self, DISPLAYSURF):
        if self.__isLeft:
            DISPLAYSURF.blit(pygame.transform.flip(self.__img[self.__status], True, False), self.__rect)
        else:
            DISPLAYSURF.blit(self.__img[self.__status], self.__rect)
        # pygame.draw.rect(DISPLAYSURF, (200, 0, 0), self.__rect)

    def checkStand(self, obstacle_top, obs_list):
        if self.__rect.bottom == obstacle_top:
            self.__isStand = True
            return
        elif self.__rect.bottom > obstacle_top:
            self.__isStand = True
            self.__rect.bottom = obstacle_top
            return
        for obs in obs_list:
            if self.__rect.colliderect(obs.rect):
                if self.__rect.centery < obs.rect.top:
                    self.__isStand = True
                    self.__rect.bottom = obs.rect.top
                    return
        self.__isStand = False

    def loseHp(self):
        """player lose one hp"""

        if self.__hp >= 1:
            self.__hp -= 1

    @property
    def rect(self):
        return self.__rect

    @property
    def coNums(self):
        return self.__coNums

    @property
    def hp(self):
        return self.__hp

    @property
    def isStand(self):
        return self.__isStand

    @isStand.setter
    def isStand(self, value: bool):
        self.__isStand = value

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
