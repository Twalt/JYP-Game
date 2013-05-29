from item import Item

class armor(Item):
	def getArVal(self):
		return self.arVal

class boots(armor):
	def __init__(self):
		self.arVal = randint(2, 8)
	
class gauntlets(armor):
	def __init__(self):
		self.arVal = randint(3, 9)
	
class legplates(armor):
	def __init__(self):
		self.arVal = randint(7, 13)
	
class shoulderplates(armor):
	def __init__(self):
		self.arVal = randint(9, 15)
	
class helm(armor):
	def __init__(self):
		self.arVal = randint(10, 16)
		
class breastplate(armor):
	def __init__(self):
		self.arVal = randint(12, 18)
