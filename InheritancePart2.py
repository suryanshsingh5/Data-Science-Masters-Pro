# Inheritance Continue
class iNeuron:
    def __init__(self):
        self.website="www.ineuron.ai"
        self._field="AI" # protected member 
    def login(self):
        print("logged in ")
    def logout(self):
        print ( "logged out")
        
class mentor(iNeuron):
    def login(self):
        print("mentor logged in ")
        
class student(iNeuron):
    def __init__(self):
        print("Student")
        super().__init__()
        super().login()
m1=mentor()
m1.login()
m1.website

s1=student()