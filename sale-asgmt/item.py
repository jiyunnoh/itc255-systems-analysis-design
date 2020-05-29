class Item:
    def __init__(self, itemid, itemname, itemprice):
        self.itemid=itemid
        self.itemname=itemname
        self.itemprice=itemprice

    def getItemId(self):
        return self.itemid

    def getItemPrice(self):
        return self.itemprice

    def setItemPrice(self, itemprice):
        self.itemprice=itemprice

    