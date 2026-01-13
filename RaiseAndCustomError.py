# Raise and Custom Error

# RAISE
a = int(input("enter the number a: "))
b = int(input("enter the number b: "))
try: 
    if (b==0):
        raise OverflowError
    ans = a/b 
except OverflowError as oe: 
    print( "There is an overflow error")

    
# CUSTOM ERROR
class SalaryHighError(Exception):
    def __init__(self, message):
        self.message=message
class EmployeeClass:
    def __init__(self, salary):
        self.salary= salary
    def getSalary(self):
        if ( self.salary> 1e8):
            raise SalaryHighError("The Salary is high" + str(self.salary))
        else:
            return self.salary
Person1=EmployeeClass(1000)
Person2=EmployeeClass(1e10)
try:
    Person1.getSalary(), Person2.getSalary()
except SalaryHighError as SHE:
    print(SHE)
else:
    print(Person1.getSalary(),Person2.getSalary())
finally:
    print( "Salary checking is done.")

