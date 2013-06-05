class Location(object):
    def __init__(self, x=-2, y=-2):
        self.x, self.y = x, y
        
    def __str__(self):
        return "%d, %d" % (self.x, self.y)
        
    def __eq__(self, other): 
        if self.x == other.x:
            if self.y == other.y:
                return True
        return False

class Item(object):
    def __init__(self, loc):
        self.loc = loc
        
