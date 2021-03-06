from random import randint
import json
from ShipProps import *
from Ship import *

class Game(ShipProps):
    ''' Game Class Runs Simulation of a battle '''
    def __init__(self, fleetOne=None, fleetTwo=None):
        ShipProps.__init__(self)
        self.battleLog = ''
        self.shipDestroyment = ''
        if fleetOne is None and fleetTwo is None:
            self.fleetOne = self.getFleet('ship_info/flota_1.txt')
            self.fleetTwo = self.getFleet('ship_info/flota_2.txt')
        else:
            self.fleetOne = self.getFleetFromJson(fleetOne)
            self.fleetTwo = self.getFleetFromJson(fleetTwo)

    def getFleet(self, file):
        '''If self.fleetOne is None and self.fleetTwo is None it will read
        fleet from txt files'''

        fleetList = []
        with open(file,'r') as f:
            for line in f:
                elem = line.strip().split()
                if len(elem) == 2 and elem[1].isdigit():
                    if int(elem[1]) != 0:
                        fleetList.append(elem)
        return self.makeInstanceOfShips(fleetList)

    def getFleetFromJson(self, fleet):
        '''generate fleet if comes from json request'''
        fleetList = []
        for key, value in fleet.items():
            if int(value) > 0:
                fleetList.append([key[:key.index('_')], value])
        return self.makeInstanceOfShips(fleetList)


    def makeInstanceOfShips(self, fleet):
        '''Creates instance of specific ship Type example: ['mt', 20] will create
        20 ship instances of mt ship type'''

        for ship in range(len(fleet)):
            for number in range(int(fleet[ship][1])):
                specificShipProp = (self.shipProps[self.shipNames.index(fleet[ship][0])])
                specificShipAtkChance = (self.shipAtkChance[self.shipNames.index(fleet[ship][0])])
                fleet[ship].append(Ship(specificShipProp, self.shipNames, specificShipAtkChance))
        return fleet

    def printship(self, fleet):
        '''prints every ship sp points'''
    
        self.shipDestroyment += "--"*20
        # print("--"*20)
        for type in fleet:
            for ship in type:
                self.shipDestroyment += "\n %s" % (ship)
                # print(ship)

    def battle(self):
        '''Two fleets fight for 6 rounds order of ship attack is determined by
           [mt dt lm cm kr ow sk re ss b n gs p]'''
        rounds = 1
        while (rounds != 6):
            self.printship(self.fleetOne)
            for shipType in self.fleetOne:
                # print("Rodzaj statku teraz", shipType[0])
                for shipInstance in shipType:
                    if type(shipInstance).__name__ == 'instance':
                        # randomly chooseShip from enemy ship
                        while (True):
                            enemyShipType = self.fleetTwo[randint(0, len(self.fleetTwo)-1)]
                            chooseShip = enemyShipType[randint(2, len(enemyShipType)-1)]
                            attackResult = shipInstance.attackShip(chooseShip)
                            if not attackResult:
                                break

            for shipType in self.fleetTwo:
                for shipInstance in shipType:
                    if type(shipInstance).__name__ == 'instance':
                        while (True):
                            enemyShipType = self.fleetOne[randint(0, len(self.fleetOne)-1)]
                            chooseShip = enemyShipType[randint(2, len(enemyShipType)-1)]
                            if not shipInstance.attackShip(chooseShip):
                                break

            # end of Round delete theese ships that are destroyed or end fight
            if self.clearDestroyedShips(self.fleetOne, 1):
                self.showAllFleet(rounds)
                break
            if self.clearDestroyedShips(self.fleetTwo, 2):
                self.showAllFleet(rounds)
                break
            self.showAllFleet(rounds)
            self.printship(self.fleetOne)
            self.printship(self.fleetTwo)
            rounds += 1


    def clearDestroyedShips(self, fleet, fleetNumber):
        '''Checks wich Ships are destroyed after round and remove it also
           set default sp and armor for the next round!'''
        iterator_of_shipType = 0
        for shipType in fleet:
            tmp_instance = []
            for shipInstance in shipType:
                if type(shipInstance).__name__ == 'instance':
                    if shipInstance.sp > 0:
                        shipInstance.armor = shipInstance.shipProps[3]
                        tmp_instance.append(shipInstance)
            fleet[iterator_of_shipType] = shipType[:2] + tmp_instance
            iterator_of_shipType += 1;

        if len(fleet) <= 1 and len(fleet[0]) == 2:
            '''IF there's no ship instances for specific Ship Type it
               means that battle is over'''
            return True
        else:
            tmp = []
            for i in range(len(fleet)):
                '''Clear Ship Type from Fleet if there's no instances of its ship
                   type'''
                if len(fleet[i]) != 2:
                    tmp.append(fleet[i])
            fleet = tmp
            if fleetNumber == 1:
                self.fleetOne = fleet
            else:
                self.fleetTwo = fleet
            return False

    def showAllFleet(self, rounds):
        self.battleLog += "\n> Round %s" % (rounds)
        self.battleLog += "\n One: "

        # print("\n> Round %s" % (rounds))
        # print("One: ")
        self._showAllFleet(self.fleetOne)
        self.battleLog += "\n Two: "
        # print("Two: ")
        self._showAllFleet(self.fleetTwo)


    def _showAllFleet(self, fleet):
        if len(fleet) <= 1 and len(fleet[0]) == 2:
            self.battleLog += "\n FLEET DESTROYED"
        else:
            for shipType in fleet:
                self.battleLog += "\n %s %s" %(shipType[0], len(shipType[2:]))
                # print(shipType[0], len(shipType[2:]))


# g = Game()
# g.battle()
