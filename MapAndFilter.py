# Map Functions
def square ( x ):
    return x*x
l1 = [ 1,3,4]
map( square, l1 ) # this data is the object of map function
list( map( square, l1 ) ) # typecasting of the map object
tuple( map( square, l1 ) )

list( map ( lambda x : x**2, [ 343,343,453,24,4546]))

# Filter Functions

l1 = [ 1,3,4]
list( filter ( lambda x : x%2==0, l1))