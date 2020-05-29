from customer import Customer
import datetime

class Payment:
    def __init__(self, totalAmount):
        self.totalAmount=totalAmount
        self.paymentdate=datetime.date.today()
        self.paymenttiem=datetime.time.strftime()
        
    def getTotalAmount(self):
        return self.totalAmount

    def __str__(self):
        return "The total amount is " + str(self.totalAmount)