from item import Item

class OrderDetail:
    def __init__(self, Item, quantity):
        self.item=Item
        self.quantity=quantity

    def getItem(self):
        return self.item

    def getQuantity(self):
        return self.quantity