from __future__ import print_function

class ShipProps(object):
    '''ShipProps reads every property that's written for specific ship in txt
       file and write it to list'''
    def __init__(self):
        self.shipProps = self.getShipProps()[1:]
        self.shipNames = self.getShipNames()
        self.shipAtkChance = self.getShipAtkChance()[1:]

    def show(self, listName):
        ''' Show list in readable style '''
        # print(listName)
        if type(listName) is list:
            tmp = ('\n'.join(str(p) for p in listName))
            print(tmp)

    def getShipProps(self):
        '''Takes all Ship type from txt file and create list of values for
           specific ship type'''
        shipProps = []
        with open('ship_info/dane_statkow.txt','r') as f:
            for line in f:
                shipProp = line.strip().split()
                for i in range(len(shipProp)):
                    if shipProp[i].isdigit():
                        shipProp[i] = int(shipProp[i])
                shipProps.append(shipProp)
        return shipProps

    def getShipNames(self):
        ''' List of Ship Shortcodes '''
        return [ship[0] for ship in self.shipProps]

    def getShipAtkChance(self):
        ''' Every ship have chance for re attack based on ship type
            it returns list of that chances '''
        with open('ship_info/szybkie_dziala.txt','r') as f:
            return [list(line.strip().split()) for line in f]
