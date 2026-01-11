# Encapsulation and Class Variable
class Car:
    def __init__( self, brand="BMW", color="Grey", price=45497832878 ):
        print("Hiii, I am a car")
        self.__brand = brand
        self.__color = color
        self.__price= price
        print(self.__brand, self.__color, self.__price)
    def acc(self):
        print ( "Accelerating the car")
        
    def getPrice(self):
        return( self.__price)
    def setPrice(self, newPrice):
        pin=int(input("enter the pin"))
        if pin!= 0000:
                return ("The pin is incorrect")
        else:
            self.__price=newPrice
            return self.__price

        """
        ANOTHER METHOD FOR SETTER, DIRECTLY SETTING PRICE
         def setPrice(self, pin, newPrice):
        
        if pin!= 0000:
                return ("The pin is incorrect")
        else:
            self.__price=newPrice
            return self.__price
        """
        
car1=Car("audi", "red", 3000000)
# car1.__brand, car1.__color, car1.__price THIS WILL GIVE ERROR BECAUSE OF ACCESS MODIFIER
car1.acc()
car1.getPrice()
car1.setPrice(34534623542)