# Complex Numbers 
a= complex(2,4)
b= complex(3,8)
print(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
assert str(a)== "(2+4j)" 

# creating complex number program
class complexNumber:
    def __init__(self, real=0, imaginary=0):
        print ( " under the init of complexNumber")
        self.real= real
        self.imaginary=imaginary
    def __str__(self):
        if (self.real==0):
            return (f"{self.imaginary}j")
        if ( self.imaginary<0):
            return (f"{self.real}{self.imaginary}j")
        return (f"{self.real}+{self.imaginary}j")
    def __add__(self, other):
        newReal=self.real+other.real
        newImaginary=self.imaginary+other.imaginary
        return complexNumber(newReal, newImaginary)

    def __sub__(self, other):
        newReal=self.real-other.real
        newImaginary=self.imaginary-other.imaginary
        return complexNumber(newReal, newImaginary)
    def __eq__(self, other):
        return self.real==other.real and self.imaginary==other.imaginary
    def __ne__(self, other):
        return not self.__eq__(other)

        
c1=complexNumber(1,2)
print(c1)
c2=complexNumber(2,4)
print(c2)
print(c1+c2)
print(c1-c2)
c1==c2
c1!=c2