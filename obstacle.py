from item import Location
class Obstacle(object):
	def __init__(self, loc):
		self.loc = loc
	
	def __str__(self):
		return "%d, %d" % (self.loc.x, self.loc.y)

class Wall(Obstacle):
	def __init__(self, loc):
		self.loc = loc

	def __str__(self):
		return "wall"
		
class Landmark(Obstacle):
	def __init__(self,loc , lType):
		self.loc = loc
		self.lType = lType
		
	def __str__(self):
		return "%s" % (self.lType)
		
	def toStr(self):
		return "%s" % (self.lType)
