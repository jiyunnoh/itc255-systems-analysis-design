class Membership:
    def __init__(self, membershipid, joindate, level):
        self.membershipid=membershipid
        self.joindate=joindate
        self.level=level

    def getJoinDate(self):
        return self.joindate

    def setLevel(self, level):
        self.level=level