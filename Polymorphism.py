# Polymorphism
class iNeuron:
    def constructor1(self):
        print("ineuron constructor1")
        self.website="www.ineuron.ai"
    def constructor2(self, website=""):
        print("ineuron constructor2")
        self.website="www.gatewallah.ai"
    def __init__(self, website=""):
        if (website==""):
            self.constructor2()
        else:
            self.constructor1()
obj1=iNeuron()
obj2=iNeuron(website="HEllo")