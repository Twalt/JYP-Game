from item import Location
class Obstacle(object):
	def __init__(self, loc):
		self.loc = loc
	
	def __str__(self):
		return "%d, %d" % (self.loc.x, self.loc.y)

class Wall(Obstacle):
	def __init__(self, loc):
		self.loc = loc
