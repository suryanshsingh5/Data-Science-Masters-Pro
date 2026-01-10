# Properties and Methods in Class
class Car:
    def __init__( self, brand="BMW", color="Grey", price=45497832878 ):
        print("Hiii, I am a car")
        self.brand = brand
        self.color = color
        self.price= price
    def acc(self):
        print ( "Accelerating the car")
car1=Car("audi", "red", 3000000)
car1.brand, car1.color, car1.price
car1.acc()
car2=Car()
car2.brand, car2.color, car2.price
car2.acc()