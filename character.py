from item import Location
from item import Item

class Character(Item):
	def __init__(self, loc, compass):
		self.loc = loc
		self.compass = compass

class Compass(object):
    def __init__(self, direction = 0):
        self.direction = direction
        
    def __str__(self):
        retVal = ""
        if self.direction == 0:
            retVal = "North"
        elif self.direction == 1:
            retVal = "East"
        elif self.direction == 2:
            retVal = "South"
        elif self.direction == 3:
            retVal = "West"
        return retVal
