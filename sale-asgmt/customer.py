from user import User
from membership import Membership

class Customer:
    def __init__(self, User, email, Membership):
        self.user=User
        self.membership=Membership
        self.email=email

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email=email

    def getMembership(self):
        return self.membership
    