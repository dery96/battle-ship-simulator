#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import random

class Ship():
    """docstring for Statek."""
    def __init__(self, shipProps, shipNames, shipAtkChance):
        self.shortcode = shipProps[0]
        self.name = shipProps[1] #full name of ship
        self.sp = shipProps[2] #strctural_point
        self.arm = shipProps[3] #armor
        self.atk = shipProps[4] #attack
        self.shipNames = shipNames #list of every ship type
        self.shipProps = shipProps #shipProps of specific ship
        self.shipAtkChance = shipAtkChance #shipAtkChance of specific ship
        self.destroy = False

    def __str__(self):
        ''' Returns ship status '''
        return "[%s] sp: %s arm: %s atk: %s " % (self.shortcode, self.sp, self.arm, self.atk)

    def attackShip(self, otherShip):
        ''' Attack OtherShip '''
        # check if you are not overload
        if self.atk > otherShip.arm*0.01:
            # if atk is bigger than 1% of armor hostile Ship we can attack
            self.fire(otherShip)
            otherShip.getDamagePercentage()
            if self.checkIfCanAttackAgain(otherShip):
                return True
            return False


    def fire(self, otherShip):
        ''' Fire missle to hostile Ship! '''
        tmpAtk = self.atk - otherShip.arm
        if (otherShip.arm - self.atk) <= 0:
            otherShip.arm = 0
            otherShip.sp -= tmpAtk
        else:
            otherShip.arm -= self.atk


    def checkIfCanAttackAgain(self, otherShip):
        ''' Fast Guns FOR specific ship determine if can attack again in the
            same round [mt dt lm cm kr ow sk re ss b n gs p]'''
        numbeOfFastGuns = self.shipAtkChance[self.shipNames.index(otherShip.shortcode)+1]
        chance = 1 - 1/float(numbeOfFastGuns)
        return (chance > random())


    def getDamagePercentage(self):
        '''Gets information about ship damage percentage
           (it means how much ship is destroyed)'''
        damage = 1 - ((self.sp)/float(self.shipProps[2]))
        if damage > 0.3 and damage < random():
            self.sp = 0
        return damage
