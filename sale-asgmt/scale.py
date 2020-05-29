from item import Item

class Scale:
    def __init__(self, Item, weight):
        self.item=Item
        self.weight=weight

    def setWeight(self, weight):
        self.weight=weight

    def getWeight(self):
        return self.weight