# Destructor
from abc import ABC, abstractmethod
class tvremote(ABC):
    def __init__(self,name):
        self.name=name
        
    @abstractmethod
    def on(self):
        pass


        
class sonyTv(tvremote):
    def on(self):
        print("starting TV")
        
    def __del__(self):
        self.name=""
        print("destructor called")

s1=sonyTv("jvjhgfd")
s1.on()
del s1
s1