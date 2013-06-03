from item import Location
from item import Item
import random

class armor(Item):
	#creates Item at location
	def __init__(self, loc = Location()):
		super(armor, self).__init__(loc)
		self.arVal = random.randint(self.__start__, self.__end__)

class boots(armor):
	def __init__(self, loc = Location()):
		super(boots, self).__init__(loc)
	__start__ = 2
	__end__ = 8
	
class gauntlets(armor):
	def __init__(self, loc = Location()):
		super(gauntlets, self).__init__(loc)
	__start__ = 3
	__end__ = 9
	
class legplates(armor):
	def __init__(self, loc = Location()):
		super(legplates, self).__init__(loc)
	__start__ = 7
	__end__ = 13
	
class shoulderplates(armor):
	def __init__(self, loc = Location()):
		super(shoulderplates, self).__init__(loc)
	__start__ = 9
	__end__ = 15
	
class helm(armor):
	def __init__(self, loc = Location()):
		super(helm, self).__init__(loc)
	__start__ = 10
	__end__ = 15
		
class breastplate(armor):
	def __init__(self, loc = Location()):
		super(breastplate, self).__init__(loc)
	__start__ = 12
	__end__ = 18
