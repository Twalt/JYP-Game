class Location(object):
    def __init__(self, x=-2, y=-2):
        self.x, self.y = x, y
    def __str__(self):
        return "%d, %d" % (self.x, self.y)
 
class Item(object):
    def __init__(self, loc):
        self.loc = loc
    def setLoc(self, loc):
        self.loc = loc
