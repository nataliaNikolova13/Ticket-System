from event import Category
from users import Role

class Controler():
    def __init__(self):
        self.currentUser = False
        self.currentCategory = Category.UNKNOWN


    def passLogInInfo(self, username, password, role):
        print("Username %s Password %s Role %s"%(username, password, Role(int(role)).name))  

    def validateInfo(self):
        pass

    def register(self):
        pass  

    def passRegistrationInfo(self, username, email, password, role):
        pass

