from item import Item
from orderdetail import OrderDetail
from payment import Payment
from customer import Customer

class Order:
    def __init__(self):
        self.orderItems=[]

    def addItems(self, orderitem):
        self.orderItems.append(orderitem)

    def getItems(self):
        return self.orderItems

    def calculateTotal(self):
        total=0.0
        for i in self.orderItems:
            total+=i.getItem().itemprice * i.quantity
        payment=Payment(total)
        return payment
