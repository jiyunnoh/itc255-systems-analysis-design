from user import User
from membership import Membership

class Customer:
    def __init__(self, User, email, creditCardInfo, Membership):
        self.user=User
        self.membership=Membership
        self.email=email
        self.creditCardInfo=creditCardInfo

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email=email

    def getMembership(self):
        return self.membership

    def getCreditCardInfo(self):
        return self.creditCardInfo

    def setCreditCardInfo(self, creditCardInfo):
        self.creditCardInfo=creditCardInfo
    