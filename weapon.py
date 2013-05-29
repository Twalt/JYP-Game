import item
Item = item.Item
class weapon(Item):
	def setCoord(self, loc):
		Item.setCoord(self, loc)
	def getCoord(self):
		return Item.getCoord()
