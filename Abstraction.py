# Abstraction
from abc import ABC, abstractmethod
class iNeuron( ABC ):
    """
    we have to declare manually 
    that it is a abstract method
    """
    @abstractmethod
    def login(self):
        pass
class Mentor(iNeuron):
    def __init__(self):
        self.a=1
    def login(self):
        print("logged in ") 
        """
        the abstract method 
        which is defined by the decorator in the parent class 
        must be defined in the child class too 
        to follow the inheritance 
        otherwise it will casue error
        """

mentor1=Mentor()
mentor1.login()