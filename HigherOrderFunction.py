# Higher Order Function
def Hfunction( function, l1):
    for i in l1:
        print ( function (i)) # this is not indexing instead of that it is accepting values one by one
print ( " Now finding the square of numbers in a list ")
Hfunction ( lambda x : x**2, [ 1,2,3,4,55,66])
print ( " Now Checking those numbers who are divible by 2 or not")
Hfunction ( lambda x : x%2, [ 1,2,3,4,5,6,7,8,9,10])

print ( " Now printing only those numbers who are only divible by 2 ")
def myHigherFuntion ( function, l1 ):
    for i in l1:
        if function ( i ) % 2 ==0:
            print ( i )
myHigherFuntion ( lambda x : x%2, [ 1,2,3,4,5,6,7,8,9,10])