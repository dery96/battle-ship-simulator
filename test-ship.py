from random import randint

from ShipProps import *
from Ship import *

class Game(ShipProps):
    ''' Game Class Runs Simulation of a battle '''
    def __init__(self):
        ShipProps.__init__(self)
        self.fleetOne = self.getFleet('flota_1.txt')
        self.fleetTwo = self.getFleet('flota_2.txt')

    def getFleet(self, file):
        fleetList = []
        with open(file,'r') as f:
            for line in f:
                elem = line.strip().split()
                if len(elem) == 2 and elem[1].isdigit():
                    if int(elem[1]) != 0:
                        fleetList.append(elem)
        return self.makeInstanceOfShips(fleetList)


    def makeInstanceOfShips(self, fleet):
        for ship in range(len(fleet)):
            for number in range(int(fleet[ship][1])):
                specificShipProp = (self.shipProps[self.shipNames.index(fleet[ship][0])])
                specificShipAtkChance = (self.shipAtkChance[self.shipNames.index(fleet[ship][0])])
                fleet[ship].append(Ship(specificShipProp, self.shipNames, specificShipAtkChance))
        return fleet

g = Game()

def printship(g=Game()):
    print("--"*20)
    print("FIRST FLEET")
    for type in g.fleetOne:
        for ship in type:
            print(ship)

    print("--"*20)
    print("SECOND FLEET")
    for type in g.fleetTwo:
        for ship in type:
            print(ship)

one = g.fleetOne[0][2]
enemy = g.fleetTwo[0][2]
print(one.checkIfCanAttackAgain(enemy))
# while (True):
#     wynik = one.attackShip(enemy)
#     if not wynik:
#         break
# print(one)
# print enemy, "enemy"
# print wynik
# printship(g)
