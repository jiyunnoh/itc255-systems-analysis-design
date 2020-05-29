class User:
    def __init__(self, userid, username, userphone):
        self.userid=userid
        self.username=username
        self.userphone=userphone

    def getUserId(self):
        return self.userid

    def getUserName(self):
        return self.username

    def getUserPhone(self):
        return self.userphone

    def setUserPhone(self, userphone):
        self.userphone=userphone

    def __str__(self):
        return self.userid