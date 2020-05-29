from user import User
from item import Item

class Employee:
    def __init__(self, User, position, hiredate):
        self.user=User
        self.position=position
        self.hiredate=hiredate

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position=position

    def getHireDate(self):
        return self.hiredate

    
    