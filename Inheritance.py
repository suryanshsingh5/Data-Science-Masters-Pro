# Inheritance and Introduction
class iNeuron:
    def __init__(self):
        self.website="www.ineuron.ai"
        self.__field="AI"
        
    def login(self):
        print("logged in ")
    def logout(self):
        print ( "logged out")
class mentor(iNeuron):
    pass
class student(iNeuron):
    pass
m1=mentor()
m1.login()
m1.website


